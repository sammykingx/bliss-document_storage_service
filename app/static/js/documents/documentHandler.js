import { DOCUMENTS_ENDPOINTS } from "../endpoints.js";

/*
 * make a request to get all documents
 * iterate the response to get individual file
 * fix the download link there
*/

// get documents
/*
async function fetchDocuments() {
    try {
        const response = await fetch(DOCUMENTS_ENDPOINTS.All_DOCUMENTS);
        if (!response.ok) {
            if (response.status === 404) {
                showNotification("No Documents Found, loading demo data", "warning");
                let demoData = [
                    {
                        docId: "BLL-1234567890",
                        clientName: "Name of doc",
                        clientEmail: "johnDoe@example.com",
                        docType: "Deed of Transfer",
                        originBranch: "BLL Ihm",
                    }
                ];
                return demoData;
            }
            // any other status code not 404
            throw new Error("Ooopsy, Network Error try again");
        }

        const data = await response.json();
        showNotification("Loading documents", "infoo");
        return data;

    } catch (err) {
        showNotification(err, "error")
    }
}

let allDocuments = await fetchDocuments();
*/

/* dynamically place nodes on DOMTree
document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("tableBody");

    allDocuments.forEach(doc => {
        const row = doc.createElement("tr");

        const docIdCell = doc.createElement("td");
        docIdCell.textContent = doc.docId;
        row.appendChild(docIdCell);

        const clientName = doc.createElement("td");
        clientName.textContent = doc.clientName;
        row.appendChild(clientName);
        
        const clientEmail = doc.createElement("td");
        clientEmail.textContent = doc.clientEmail;
        row.appendChild(clientEmail);

        const docType = doc.createElement("td");
        docType.textContent = doc.docType;
        row.appendChild(docType);

        const originBranch = doc.createElement("td");
        originBranch.textContent = doc.originBranch;
        row.appendChild(originBranch);

        tableBody.appendChild(row);
    });

});

*/
// come back to this part
/*
document.getElementById("searchForm").addEventListener("submit", event => {
    event.preventDefault();

    const searchInput = document.getElementById("searchInput").value.trim();
    const docCategory = document.getElementById("categoryFilter").value;
    const branchName = document.getElementById("clientBranch").value;

    if (!searchInput && !docCategory && !branchName) {
        showNotification("Enter at least 1 Property to search", "warning");
        return;
    }

    let payload = new FormData();
    
    payload.append("search_input", searchInput);
    payload.append("doc_category", docCategory);
    payload.append("client_branch", branchName);

    fetch(
        DOCUMENTS_ENDPOINTS.All_DOCUMENTS, {
        method: "POST",
        body: payload,
    })
    .then(response => {
        if (!response.ok) {
            console.log("response not ok");
            showNotification("request status not ok", "warning");
        }

        document.getElementById("searchForm").reset();
        showNotification("Still Working on it", "info");
        // return response.json();
    })
    .catch(err => {
        console.log("inside the catch block");
        showNotification(err, "error");
    })
});
*/

document.addEventListener("DOMContentLoaded", () => {
  showNotification("All files loaded Succesffully", "info");
});

document.getElementById("deleteDoc").addEventListener("click", () => {
  showNotification("Delete Functionality not enabled by dev", "info");
});