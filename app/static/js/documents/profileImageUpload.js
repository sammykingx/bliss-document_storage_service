import { USER_ENDPOINTS } from "../endpoints.js";

document
  .getElementById("profileImageUpload")
  .addEventListener("submit", (event) => {
    event.preventDefault();

    const profileImage = document.getElementById("profileImage").files[0];

    if (profileImage.size > 3 * 1024 * 1024) {
      showNotification("File size should be less than 3MB", "danger");
      return;
    }

    const formData = new FormData();
    formData.append("profile_image", profileImage);

    fetch(USER_ENDPOINTS.USER_PROFILE_IMAGE, {
      method: "PATCH",
      body: formData,
      /*  headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    */
    })
      .then((response) => {
        if (!response.ok) {
          showNotification("Profile Image upload failed", "info");
        } else {
          showNotification("Profile Image uploaded successfully", "success");
          setTimeout(() => {
            window.location.reload();
          }, 1500);
        }
      })
      .catch((error) => {
        showNotification(error, "danger");
      });
  });
