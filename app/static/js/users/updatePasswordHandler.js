import { USER_ENDPOINTS } from "../endpoints.js";

document.getElementById("updatePasswordForm").addEventListener("submit", (event) => {
    event.preventDefault();

    const newPassword = document.getElementById("newPassword").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();
    const currentPassword = document.getElementById("currentPassword").value.trim();

    if (newPassword === "" || currentPassword === "" || confirmPassword === "") {
        showNotification("Enter a valid password character", "warning");
        return;
    } else if (newPassword !== confirmPassword) {
        showNotification("Passwords Doesn't match", "info");
        return;
    }

    const payload = new FormData();
    payload.append("current_pwd", currentPassword);
    payload.append("new_pwd", newPassword);
    payload.append("validate_pwd", confirmPassword);

    fetch(USER_ENDPOINTS.USER_PROFILE_PASSWORD, {
        method: "POST",
        body: payload,
    })

    .then(res => {
        if (!res.ok) {
            showNotification("Unexpected response from server", "warning");
            return;
        }

        return res.json();
    })
    .then(data => {
        showNotification(data.message, data.category);
        if (data.category === "success") {
            window.location.reload();
        }
    })
    .catch(err => {
        showNotification(err, "error");
    })

});