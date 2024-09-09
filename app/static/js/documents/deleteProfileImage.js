import { USER_ENDPOINTS } from "../endpoints.js";

document.getElementById("thrashPicture").addEventListener("click", (event) => {
  event.preventDefault();

  fetch(USER_ENDPOINTS.DELETE_PROFILE_IMAGE, {
    method: "DELETE",
    /* headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        }, */
  })
    .then((response) => {
      if (!response.ok) {
        showNotification("Profile Image delete failed", "info");
      }

      return response.json();
    })
    .then((data) => {
      showNotification(data.message, data.category);

      if (data.category === "success") {
        setTimeout(() => {
          window.location.reload();
        }, 1500);
      }
    })
    .catch((error) => {
      showNotification(error, "danger");
    });
});
