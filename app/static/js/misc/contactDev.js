import { DEV_SUPPORT_ENDPOINTS } from "../endpoints.js";

document
  .getElementById("contactDevTeam")
  .addEventListener("submit", (event) => {
    event.preventDefault();

    const userEmail = document.getElementById("formEmail").value;
    const subject = document.getElementById("formSubject").value.trim();
    const formMsg = document.getElementById("formMsg").value.trim();

    if (subject === "" || formMsg === "") {
      showNotification(
        "Please fill in all fields with valid characters",
        "info"
      );

      document.getElementById("contactDevTeam").reset();

      return;
    }

    const formData = new FormData();
    /*
    fetch(DEV_SUPPORT_ENDPOINTS.CONTACT_DEV_TEAM, {
        method: "POST",
        body: formData,
    })
*/
    formData.append("email", userEmail);
    formData.append("subject", subject);
    formData.append("message", formMsg);

    showNotification("your message has been sent", "success");
  });
