const previews = [...document.querySelectorAll('.video-card video')];
const viewer = document.querySelector('.viewer');
const content = viewer.querySelector('.viewer-content');
const title = document.querySelector('#viewer-title');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let lastTrigger;

function loadVideo(video) {
  if (!video.getAttribute('src')) video.src = video.dataset.src;
}

// Only download and play the samples that are actually in view.
const observer = new IntersectionObserver(entries => {
  entries.forEach(({ target, isIntersecting }) => {
    target.dataset.visible = String(isIntersecting);
    target.parentElement.classList.toggle('is-paused', reduceMotion.matches);
    if (isIntersecting && !reduceMotion.matches && !viewer.open && !document.hidden) {
      loadVideo(target);
      target.play().catch(() => target.parentElement.classList.add('is-paused'));
    } else target.pause();
  });
}, { threshold: .25 });
previews.forEach(video => observer.observe(video));

function openViewer(trigger) {
  lastTrigger = trigger;
  previews.forEach(video => video.pause());
  title.textContent = trigger.dataset.title;
  content.replaceChildren();
  const preview = trigger.parentElement.querySelector('video');
  const player = document.createElement('video');
  player.src = preview.dataset.src;
  player.poster = preview.poster;
  player.controls = true;
  player.playsInline = true;
  player.setAttribute('aria-label', trigger.dataset.title);
  player.addEventListener('error', () => {
    const message = document.createElement('p');
    message.className = 'media-error';
    message.textContent = 'This video could not be played. ';
    const link = document.createElement('a');
    link.href = preview.dataset.src;
    link.textContent = 'Open the video file';
    message.append(link);
    content.replaceChildren(message);
  }, { once: true });
  content.append(player);
  player.play().catch(() => { /* Native controls remain available. */ });
  document.body.classList.add('viewer-open');
  viewer.showModal();
  viewer.querySelector('.close-viewer').focus();
}

document.querySelectorAll('.watch-video').forEach(button => {
  button.addEventListener('click', () => openViewer(button));
});
viewer.querySelector('.close-viewer').addEventListener('click', () => viewer.close());
viewer.addEventListener('click', event => {
  if (event.target !== viewer) return;
  const rect = viewer.getBoundingClientRect();
  if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) viewer.close();
});

function resumePreviews() {
  previews.forEach(video => {
    if (video.dataset.visible === 'true' && !document.hidden && !viewer.open && !reduceMotion.matches) {
      loadVideo(video);
      video.play().catch(() => video.parentElement.classList.add('is-paused'));
    } else video.pause();
  });
}
viewer.addEventListener('close', () => {
  const player = content.querySelector('video');
  if (player) { player.pause(); player.removeAttribute('src'); player.load(); }
  content.replaceChildren();
  document.body.classList.remove('viewer-open');
  lastTrigger?.focus({ preventScroll: true });
  resumePreviews();
});
document.addEventListener('visibilitychange', resumePreviews);
document.addEventListener('visibilitychange', () => {
  if (document.hidden) content.querySelector('video')?.pause();
});
reduceMotion.addEventListener('change', resumePreviews);

const topButton = document.querySelector('.back-to-top');
const updateTopButton = () => { topButton.hidden = window.scrollY < window.innerHeight; };
window.addEventListener('scroll', updateTopButton, { passive: true });
window.addEventListener('pageshow', updateTopButton);
topButton.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reduceMotion.matches ? 'instant' : 'smooth' }));
