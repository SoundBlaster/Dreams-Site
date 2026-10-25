(() => {
  const requested = new URL(location.href).searchParams.get('lang');
  const language = requested === 'ru' || requested === 'en'
    ? requested : (navigator.language.toLowerCase().startsWith('ru') ? 'ru' : 'en');
  document.documentElement.lang = language;
  document.querySelectorAll('[data-language]').forEach(section => {
    section.hidden = section.dataset.language !== language;
  });
  document.querySelectorAll('[data-language-choice]').forEach(link => {
    if (link.dataset.languageChoice === language) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });
  document.querySelectorAll('a[data-local]').forEach(link => {
    const target = new URL(link.getAttribute('href'), location.href);
    target.searchParams.set('lang', language);
    link.href = target.href;
  });
  document.title = document.querySelector('[data-language="' + language + '"]').dataset.title;
})();
