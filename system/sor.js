/* Seeds of Renaissance behaviours. Small and optional: pages read fine without it. */
(function () {
  // Selected work: hovering, focusing or clicking an item swaps the picture and caption.
  document.querySelectorAll('.selected').forEach(function (sel) {
    var items = sel.querySelectorAll('li[data-img]'), img = sel.querySelector('.picture img'), cap = sel.querySelector('.picture .caption');
    function pick(li) {
      items.forEach(function (x) { x.removeAttribute('aria-current') });
      li.setAttribute('aria-current', 'true');
      if (img) { img.src = li.dataset.img; img.alt = li.dataset.alt || '' }
      if (cap) cap.textContent = li.dataset.cap || '';
    }
    items.forEach(function (li) { ['mouseenter', 'focus', 'click'].forEach(function (ev) { li.addEventListener(ev, function () { pick(li) }) }) });
  });
})();
