import { AUTH_ENDPOINTS } from '../endpoints.js';;

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;

    let formData = new FormData();
    formData.append("email", email);

    document.getElementById('spinner').style.display = "block";

    fetch(AUTH_ENDPOINTS.RESET_PASSWORD_REQUEST, {
        method: "POST",
        body: formData
    })
    .then(response => {
        /*if (!response.ok) {
            // show server message not the hard coded message
            showNotification("Invalid email address", "warning");
            return;
        }8*/
        return response.json();
    })
    .then(data => {
        /* 
            - display a loading icon before response from the server
            - show the notification
        */
        document.getElementById('spinner').style.display = "none";
        showNotification(data.message, data.category);
        if (data.category === "info") {
            document.getElementById("loginForm").reset();
        }
    })
    .catch(err => {
        document.getElementById('spinner').style.display = "none";
        showNotification(err, "error");
    });
});