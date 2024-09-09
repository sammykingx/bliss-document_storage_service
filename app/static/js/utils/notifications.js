function showNotification(message, category) {
    const notification = document.getElementById("notification");
    notification.textContent = message;
    notification.className = category;
    notification.style.display = "block";
    setTimeout(function() {
        notification.style.opacity = 1;
    }, 10);

    // Hide the notification after 3 seconds
    setTimeout(function() {
        notification.style.opacity = 0;
        setTimeout(function() {
            notification.style.display = "none";
        }, 500);
    }, 3000);
}