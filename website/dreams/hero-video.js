(() => {
  const video = document.querySelector(".hero-media video");
  const button = document.querySelector(".hero-play");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (!video || !button) return;

  const play = () => {
    if (reducedMotion.matches) return;
    video.muted = true;
    const attempt = video.play();
    if (attempt) attempt.then(() => { button.hidden = true; })
      .catch(() => { if (video.paused && !reducedMotion.matches) button.hidden = false; });
  };

  button.addEventListener("click", play);
  video.addEventListener("playing", () => { button.hidden = true; });
  reducedMotion.addEventListener("change", () => {
    if (reducedMotion.matches) {
      video.pause();
      button.hidden = true;
    } else {
      play();
    }
  });
  play();
})();
