import { USER_ENDPOINTS } from "../endpoints.js";

const about = document.getElementById("about");
const maxLength = 199;

about.addEventListener("input", () => {
  if (about.value.length > maxLength) {
    showNotification(
      `Maximum length reached! You have ${
        maxLength - about.value.length
      } more characters left.`,
      "warning"
    );
    about.value = about.value.substring(0, maxLength);
  }
});

// On form Submit
document.getElementById("updateProfile").addEventListener("submit", (event) => {
  event.preventDefault();

  const about = document.getElementById("about").value.trim();
  const facebook = document.getElementById("Facebook").value.trim();
  const twitter = document.getElementById("Twitter").value.trim();
  const instagram = document.getElementById("Instagram").value.trim();
  const linkedin = document.getElementById("Linkedin").value.trim();

  const payload = new FormData();

  console.log("inside updateProfile.js");
  console.log(facebook);

  payload.append("about", about);
  payload.append("facebook", facebook);
  payload.append("twitter", twitter);
  payload.append("instagram", instagram);
  payload.append("linkedin", linkedin);

  fetch(USER_ENDPOINTS.USER_PROFILE_UPDATE, {
    method: "PUT",
    body: payload,
  })
    .then((res) => {
      if (!res.ok) {
        showNotification("Unexpected response from server", "warning");
        return;
      }

      showNotification("Profile Update successful", "success");
      setTimeout(() => {
        window.location.reload();
      }, 2000);
    })
    .catch((err) => {
      showNotification(err, "error");
    });
});
