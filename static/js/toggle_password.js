document.querySelectorAll('.toggle-password').forEach(function (button) {
    button.addEventListener('click', function () {
        const passwordField = button.previousElementSibling;
        const toggleIcon = button.querySelector('i');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        toggleIcon.classList.toggle('bi-eye');
        toggleIcon.classList.toggle('bi-eye-slash');
    });
});