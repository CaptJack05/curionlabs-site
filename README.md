# Curion Labs

A static, responsive website for **curionlabs.in**. The publishable website is entirely in `dist/`; there is no install step, JavaScript bundle, or backend.

## Preview locally

From this `Site` folder:

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:4173.

## Product links

- Adaline prebooking: https://forms.gle/d9JFSauJjWWg32ok8 — verified as the “Reserve an ADALINE Motion 30D” form.
- Perceptron quote: https://www.linkedin.com/company/curion-robotics/ — currently directs visitors to the company page, explicitly labelled “Talk to us on LinkedIn.” Replace this button's `href` in `dist/index.html` if a dedicated quote form or business email is provided.
- LinkedIn: https://www.linkedin.com/company/curion-robotics/.

## Deploy

Deploy the contents of **`dist`**, not the whole workspace. Any static host can serve these files. No build command or environment variables are needed. The included Netlify and Vercel configurations set the publish directory to `dist` when the project root is this `Site` folder.

For a manual upload host, upload `dist` or the contents of the deployment ZIP. For ordinary web hosting, place its contents in the domain's public web directory (often `public_html`).

Add `curionlabs.in` in your hosting provider's custom-domain settings, then copy the exact DNS records it returns into the domain registrar's DNS panel. Do not guess A/CNAME targets or replace existing email-related MX/TXT records. Enable HTTPS and redirect `www.curionlabs.in` to the apex if you add the www hostname.

Canonical, social-preview and sitemap URLs are already set to `https://curionlabs.in/`. DNS and public hosting must be connected before that URL is live.

## Editing

- Copy, links, page title and metadata: `dist/index.html`
- Layout, colours, responsive breakpoints: `dist/styles.css`
- Product photographs/renders and existing logo: `dist/assets/`
- Search engine files: `dist/robots.txt`, `dist/sitemap.xml`
- Error page: `dist/404.html`

Product copy comes from the supplied Curion Labs materials. Images are the supplied CAD and board previews, labelled accordingly. No prices, delivery promises, testimonials, analytics, cookies or payment processing are added. Google Forms handles Adaline reservations; LinkedIn handles contact enquiries. Site links work without JavaScript.
