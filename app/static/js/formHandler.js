document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (email.trim() === '' || password.trim() === '') {
        showNotification("Email or password cannot be empty", "warning");
        document.getElementById("loginform").reset();
        return;
    }

    let formData = new FormData();
    formData.append('email', email);
    formData.append('password', password);

    fetch('/checkpoint', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        showNotification(data.message, data.category);

        /* if (data.redirect) {
            window.location.href = data.redirect;
        } */

        if (data.redirect) {
            setTimeout(function() {
                window.location.href = data.redirect;
            }, 1500); // Adding a slight delay to show the notification
        }
    })
    .catch(function(error) {
        console.error('Error:', error);
    });
});