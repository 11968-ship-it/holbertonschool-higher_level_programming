const updateBtn = document.getElementById('update_header');
const header = document.querySelector('header');

updateBtn.addEventListener('click', function() {
  header.textContent = 'New Header!!!';
});
