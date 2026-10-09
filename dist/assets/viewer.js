const card = document.getElementById('pv-card');
const mv = document.getElementById('pv-mv');
const views = card.querySelectorAll('.pv-view');
views.forEach(b => b.addEventListener('click', () => {
  mv.cameraOrbit = b.dataset.orbit; mv.fieldOfView = 'auto';
  views.forEach(x => x.classList.toggle('pv-on', x === b));
}));
const spin = document.getElementById('pv-spin');
spin.addEventListener('click', () => { mv.autoRotate = !mv.autoRotate; spin.classList.toggle('pv-on', mv.autoRotate); });
const labels = document.getElementById('pv-labels');
labels.addEventListener('click', () => labels.classList.toggle('pv-on', !card.classList.toggle('pv-nolabels')));

// hide labels of points on the far side of the robot
const spots = [...card.querySelectorAll('.pv-spot')].map(h => [h, h.dataset.normal.split(' ').map(parseFloat)]);
const update = () => {
  const { theta, phi } = mv.getCameraOrbit();
  const e = [Math.sin(phi) * Math.sin(theta), Math.cos(phi), Math.sin(phi) * Math.cos(theta)];
  for (const [h, n] of spots) h.classList.toggle('pv-back', n[0]*e[0] + n[1]*e[1] + n[2]*e[2] < 0.15);
};
mv.addEventListener('camera-change', update);

// LED strips on/off (materials led_white / led_red / led_blue in the .glb)
const leds = document.getElementById('pv-leds'); const saved = new Map(); let on = true;
mv.addEventListener('load', () => {
  requestAnimationFrame(update);
  for (const m of mv.model.materials) if (m.name.startsWith('led_')) saved.set(m, [...m.emissiveFactor]);
  if (!saved.size) leds.style.display = 'none';
});
leds.addEventListener('click', () => {
  on = !on; leds.classList.toggle('pv-on', on);
  for (const [m, e] of saved) m.setEmissiveFactor(on ? e : [0, 0, 0]);
});
