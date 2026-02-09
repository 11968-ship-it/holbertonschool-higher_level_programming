document.addEventListener('DOMContentLoaded', function () {
  const button = document.getElementById('btn_translate');
  const select = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  button.addEventListener('click', function () {
    const lang = select.value;

    if (lang === '') {
      helloDiv.textContent = '';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(() => {
        helloDiv.textContent = '';
      });
  });
});
