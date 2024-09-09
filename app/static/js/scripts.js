document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const searchQuery = document.getElementById('searchInput').value.toLowerCase();
    const categoryFilter = document.getElementById('categoryFilter').value;
    const tableBody = document.getElementById('documentTableBody');
    const rows = tableBody.getElementsByTagName('tr');
    
    for (let row of rows) {
        const cells = row.getElementsByTagName('td');
        const category = cells[2].innerText;
        let matchFound = false;
        
        if (categoryFilter === '' || categoryFilter === category) {
            for (let cell of cells) {
                if (cell.innerText.toLowerCase().includes(searchQuery)) {
                    matchFound = true;
                    break;
                }
            }
        }
        
        if (matchFound) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    }
});

// Sample data - replace this with actual data fetching logic
const documents = [
    { name: 'Document 1', description: 'Description of Document 1', category: 'Personal' },
    { name: 'Document 2', description: 'Description of Document 2', category: 'Work' },
    // Add more document data here
];

document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.getElementById('documentTableBody');
    
    documents.forEach(doc => {
        const row = document.createElement('tr');
        
        const nameCell = document.createElement('td');
        nameCell.textContent = doc.name;
        row.appendChild(nameCell);
        
        const descriptionCell = document.createElement('td');
        descriptionCell.textContent = doc.description;
        row.appendChild(descriptionCell);
        
        const categoryCell = document.createElement('td');
        categoryCell.textContent = doc.category;
        row.appendChild(categoryCell);
        
        const actionsCell = document.createElement('td');
        const viewButton = document.createElement('a');
        viewButton.href = '#';
        viewButton.className = 'btn';
        viewButton.textContent = 'View';
        actionsCell.appendChild(viewButton);
        
        const editButton = document.createElement('a');
        editButton.href = '#';
        editButton.className = 'btn';
        editButton.textContent = 'Edit';
        actionsCell.appendChild(editButton);
        
        const deleteButton = document.createElement('a');
        deleteButton.href = '#';
        deleteButton.className = 'btn btn-danger';
        deleteButton.textContent = 'Delete';
        actionsCell.appendChild(deleteButton);
        
        row.appendChild(actionsCell);
        tableBody.appendChild(row);
    });

    // Check URL for category parameter
    const urlParams = new URLSearchParams(window.location.search);
    const category = urlParams.get('category');
    if (category) {
        document.getElementById('categoryFilter').value = category;
        document.getElementById('searchForm').dispatchEvent(new Event('submit'));
    }
});