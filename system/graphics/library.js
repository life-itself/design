/* Graphics library pages: ground and ink switchers, per-element versions, search, copy path.
   A Flowershow page script (frontmatter `scripts:`): it runs on every visit, so it is wrapped
   and safe to run again. The pages read fine without it: first version shown, all files listed. */
(function () {
  if (document.currentScript && !document.currentScript.isConnected) return;
  var sg = document.querySelector('.sg[data-sg]');
  if (!sg || sg.dataset.ready) return;
  sg.dataset.ready = '1';
  var KEY = 'sg-ground';

  function press(sel, val, attr) {
    sg.querySelectorAll(sel).forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute(attr) === val ? 'true' : 'false') });
  }
  function ground(g) {
    if (!sg.querySelector('[data-ground-btn="' + g + '"]')) return;
    sg.dataset.ground = g;
    press('[data-ground-btn]', g, 'data-ground-btn');
    try { localStorage.setItem(KEY, g) } catch (e) {}
  }
  // Show one version of an element: its image on the stage, its row marked
  function show(el, v) {
    var art = el.querySelectorAll('.sg-stage > [data-v]');
    if (![].some.call(art, function (a) { return a.dataset.v === v })) return false;
    art.forEach(function (a) { a.hidden = a.dataset.v !== v });
    el.querySelectorAll('button.sg-v').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.v === v ? 'true' : 'false') });
    return true;
  }
  function ink(v) {
    press('[data-ink-btn]', v, 'data-ink-btn');
    if (sg.dataset.render === 'img') {
      sg.querySelectorAll('.sg-el').forEach(function (el) { if (v !== 'all') show(el, v) });
    } else {
      if (v === 'all' || v === 'ground') delete sg.dataset.tint; else sg.dataset.tint = v;
    }
  }
  var q = sg.querySelector('.sg-find'), count = sg.querySelector('.sg-count'), none = sg.querySelector('.sg-none');
  var els = [].slice.call(sg.querySelectorAll('.sg-el'));
  function find() {
    var t = (q ? q.value : '').trim().toLowerCase(), n = 0;
    els.forEach(function (el) { var hit = !t || el.dataset.q.indexOf(t) > -1; el.hidden = !hit; if (hit) n++ });
    if (count) count.textContent = n + ' of ' + els.length;
    if (none) none.hidden = n > 0;
  }

  sg.addEventListener('click', function (ev) {
    var b = ev.target.closest('button');
    if (!b || !sg.contains(b)) return;
    if (b.dataset.groundBtn) ground(b.dataset.groundBtn);
    else if (b.dataset.inkBtn) ink(b.dataset.inkBtn);
    else if (b.classList.contains('sg-v')) show(b.closest('.sg-el'), b.dataset.v);
    else if (b.classList.contains('sg-cp')) {
      var t = b.dataset.copy, old = b.textContent;
      var done = function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = old }, 1200) };
      var fallback = function () { window.prompt('Copy:', t) };
      try { navigator.clipboard.writeText(t).then(done, fallback) } catch (e) { fallback() }
    }
  });
  if (q) q.addEventListener('input', find);
  // Turn the static version labels into buttons only once the script runs
  sg.querySelectorAll('span.sg-v').forEach(function (s, i) {
    var el = s.closest('.sg-el');
    if (!el || el.querySelectorAll('.sg-stage > [data-v]').length < 2) return;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'sg-v'; b.dataset.v = s.dataset.v; b.innerHTML = s.innerHTML;
    b.setAttribute('aria-pressed', s.closest('.sg-row') === el.querySelector('.sg-row') ? 'true' : 'false');
    s.replaceWith(b);
  });
  sg.querySelectorAll('.sg-bar[hidden]').forEach(function (b) { b.hidden = false });
  try { var g = localStorage.getItem(KEY); if (g) ground(g) } catch (e) {}
  find();
})();
