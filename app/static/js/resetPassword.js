import { AUTH_ENDPOINTS } from './endpoints.js';

document.getElementById("changePasswordForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');

    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (password.trim() === '' || confirmPassword.trim() === '') {
        showNotification("Password cannot be empty", "warning");
        return;
    }

    if (password !== confirmPassword) {
        showNotification("Passwords do not match", "warning");
        return;
    }

    let formData = new FormData();
    formData.append('password', password);
    formData.append('token', token);

    fetch(AUTH_ENDPOINTS.RESET_PASSWORD, {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        showNotification(data.message, data.category);
        if (data.category === "success") {
            document.getElementById("changePasswordForm").reset();
            setTimeout (function() {
                window.location.href = data.redirect_url;
            }, 3800);
        }
    })
    .catch(function(error) {
        console.error('Error:', error);
    });
});