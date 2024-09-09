import { DOCUMENTS_ENDPOINTS } from "../endpoints.js";

document.getElementById("uploadDocument").addEventListener("submit", event => {
    event.preventDefault();

    const firstName = document.getElementById("firstName").value.trim();
    const lastName = document.getElementById("lastName").value.trim();
    const clientAddress = document.getElementById("clientAddress").value.trim();
    const phoneNumber = document.getElementById("clientPhoneNumber").value.trim();

    const clientEmail = document.getElementById("clientEmail").value.trim();
    const clientBranch = document.getElementById("clientBranch").value;
    const docCategory = document.getElementById("documentCategory").value;
    const formFile = document.getElementById("formFile").files[0];

    if (formFile.size > (5 * 1024 *1024)) {
        showNotification("file should be less then 5mb", "warning");
        return;
    }

    let payload = new FormData();
    
    payload.append("firstName", firstName);
    payload.append("lastName", lastName);
    payload.append("clientAddress", clientAddress);
    payload.append("phoneNumber", phoneNumber);
    payload.append("clientEmail", clientEmail);
    payload.append("clientBranch", clientBranch);
    payload.append("docCategory", docCategory);
    payload.append("formFile", formFile);
    
    fetch(
        DOCUMENTS_ENDPOINTS.UPLOAD_DOCUMENTS, {
        method: "POST",
        body: payload,
    })
    .then(res => {
        if (!res.ok) {
          showNotification("Unable to upload file", "warning");
          return;
        }
        showNotification("File Upload Successful", "info");
        setTimeout(() => {
          window.location.reload();
        }, 700);
    })
    .catch(err => {
        showNotification(err, "error");
        document.getElementById("uploadDocument").reset();
    })
});