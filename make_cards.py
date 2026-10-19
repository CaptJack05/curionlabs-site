"""Generate the digital visiting cards and their vCards into dist/card/.

One directory per person so the URL is clean (/card/yadi/). No JavaScript:
the site's CSP is script-src 'self' and a contact card does not need any.
"""
import pathlib, html

SITE = "curionlabs.in"
LINKEDIN = "https://www.linkedin.com/company/curion-robotics/"
DIST = pathlib.Path(__file__).resolve().parent / "dist" / "card"

PEOPLE = [
    {
        "slug": "hemchandra",
        "first": "Hemchandra", "last": "Jha",
        "name": "Hemchandra Jha",
        "title": "Co-founder",
        "phone": "+919818096872",
        "phone_display": "+91 98180 96872",
        "email": "hcjha05@gmail.com",
    },
    {
        "slug": "yadi",
        "first": "Yadi", "last": "Choudhary",
        "name": "Yadi Choudhary",
        "title": "Co-founder",
        "phone": "+917818071134",
        "phone_display": "+91 78180 71134",
        "email": "yadichoudhary12@gmail.com",
    },
]

VCARD = """BEGIN:VCARD
VERSION:3.0
N:{last};{first};;;
FN:{name}
ORG:Curion Labs
TITLE:{title}
TEL;TYPE=CELL:{phone}
EMAIL;TYPE=WORK:{email}
URL:https://{site}
NOTE:Robot control electronics and autonomous mobile robots, designed and built in India.
END:VCARD
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — Curion Labs</title>
<meta name="description" content="{name}, {title} at Curion Labs. Robot control electronics and autonomous mobile robots, designed and built in India.">
<meta name="robots" content="noindex">
<link rel="stylesheet" href="../card.css">
</head>
<body>
<main class="card">
  <header>
    <img class="mark" src="../../assets/curion-mark.png" alt="">
    <div>
      <div class="brand">Curion Labs</div>
      <div class="brand-sub">Robotics · AI · Curiosity</div>
    </div>
  </header>

  <h1>{name}</h1>
  <p class="role">{title}</p>

  <a class="save" href="contact.vcf" download>Save to contacts</a>

  <ul class="links">
    <li><a href="tel:{phone}"><span class="k">Phone</span><span class="v">{phone_display}</span></a></li>
    <li><a href="mailto:{email}"><span class="k">Email</span><span class="v">{email}</span></a></li>
    <li><a href="https://{site}"><span class="k">Website</span><span class="v">{site}</span></a></li>
    <li><a href="{linkedin}"><span class="k">LinkedIn</span><span class="v">Curion Labs</span></a></li>
  </ul>

  <p class="tag">We build the electronics and the autonomy stack that mobile
  robots need. Designed and built in India.</p>
</main>
</body>
</html>
"""

CSS = """:root {
  --void: #080b12;
  --panel: #0e1626;
  --line: rgba(120,160,210,.18);
  --text: #e8eef7;
  --muted: #8296b4;
  --cyan: #38bdf8;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--void); color: var(--text);
  font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased; }
body { display: flex; justify-content: center; padding: 28px 18px 48px; }
.card { width: 100%; max-width: 420px; }
header { display: flex; align-items: center; gap: 14px; padding-bottom: 20px;
  border-bottom: 1px solid var(--line); }
.mark { width: 46px; height: 46px; }
.brand { font-size: 15px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
.brand-sub { font-size: 10.5px; letter-spacing: .2em; text-transform: uppercase;
  color: var(--muted); margin-top: 4px; }
h1 { font-size: 34px; line-height: 1.1; margin: 26px 0 6px; letter-spacing: -.02em; }
.role { margin: 0; color: var(--cyan); font-size: 15px; letter-spacing: .04em; }
.save { display: block; margin: 26px 0 22px; padding: 15px 20px; text-align: center;
  background: var(--cyan); color: #04131d; font-weight: 700; font-size: 16px;
  text-decoration: none; border-radius: 10px; }
.save:active { opacity: .85; }
.links { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--line); }
.links li { border-bottom: 1px solid var(--line); }
.links a { display: flex; justify-content: space-between; gap: 14px; align-items: baseline;
  padding: 15px 2px; text-decoration: none; color: var(--text); }
.links .k { font-size: 11px; letter-spacing: .18em; text-transform: uppercase;
  color: var(--muted); flex: none; }
.links .v { font-size: 15px; text-align: right; word-break: break-word; }
.tag { margin-top: 26px; font-size: 13px; line-height: 1.6; color: var(--muted); }
"""


def main():
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "card.css").write_text(CSS, encoding="utf-8")
    for p in PEOPLE:
        d = DIST / p["slug"]
        d.mkdir(exist_ok=True)
        (d / "contact.vcf").write_text(
            VCARD.format(site=SITE, **p), encoding="utf-8", newline="\r\n")
        (d / "index.html").write_text(
            PAGE.format(site=SITE, linkedin=LINKEDIN,
                        **{k: html.escape(str(v)) for k, v in p.items()}),
            encoding="utf-8")
        print(f"/card/{p['slug']}/  ->  {p['name']}")


if __name__ == "__main__":
    main()
