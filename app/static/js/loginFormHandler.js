import { AUTH_ENDPOINTS } from "./endpoints.js";

document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (email.trim() === "" || password.trim() === "") {
      showNotification("Email or password cannot be empty", "warning");
      return;
    }

    let formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    document.getElementById("spinner").style.display = "block";

    fetch(AUTH_ENDPOINTS.LOGIN, {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        document.getElementById("spinner").style.display = "none";
        showNotification(data.message, data.category);

        /* if (data.redirect) {
            window.location.href = data.redirect;
        } */

        if (data.redirect) {
          setTimeout(function () {
            window.location.href = data.redirect;
          }, 1500); // Adding a slight delay to show the notification
        }
      })
      .catch(function (error) {
        document.getElementById("spinner").style.display = "none";
        console.error("Error:", error);
      });
  });
