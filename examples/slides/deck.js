// Example page chrome: builds the thumbnail strip from the slides on the page, and a present mode (arrows, space, Esc).
(() => {
  const slides = [...document.querySelectorAll('#slides > figure > .slide-frame > .slide')];
  const names = [...document.querySelectorAll('#slides > figure > figcaption b')].map(b => b.textContent.replace(/\.$/, ''));
  const strip = document.getElementById('strip');
  slides.forEach((s, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', 'Present from slide ' + (i + 1));
    const f = document.createElement('div');
    f.className = 'slide-frame';
    f.appendChild(s.cloneNode(true));
    const label = document.createElement('small');
    label.textContent = names[i];
    b.append(f, label);
    b.addEventListener('click', () => open(i));
    strip.appendChild(b);
  });

  const pres = document.getElementById('present'), frame = document.getElementById('present-frame');
  let at = 0;
  const show = i => { at = (i + slides.length) % slides.length; frame.replaceChildren(slides[at].cloneNode(true)) };
  function open(i) {
    show(i); pres.hidden = false;
    pres.requestFullscreen?.().catch(() => {});
  }
  function close() {
    pres.hidden = true;
    if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
  }
  document.getElementById('present-btn').addEventListener('click', () => open(0));
  document.getElementById('present-close').addEventListener('click', close);
  frame.addEventListener('click', () => show(at + 1));
  document.addEventListener('fullscreenchange', () => { if (!document.fullscreenElement && !pres.hidden) pres.hidden = true });
  document.addEventListener('keydown', e => {
    if (pres.hidden) return;
    if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(at + 1) }
    else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(at - 1) }
    else if (e.key === 'Escape') close();
  });
})();
