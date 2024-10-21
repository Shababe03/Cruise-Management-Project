// Optional JavaScript for Form Validation
const loginForm = document.querySelector('form');
loginForm.addEventListener('submit', function(event) {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username.trim() === "" || password.trim() === "") {
        alert("Please fill in all fields");
        event.preventDefault();
    }
});
