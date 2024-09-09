
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting

    /* Get input values
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    /* Basic validation
    if (email.trim() === '' || email.trim() === '') {
        alert("hahahah sammy i don run am");
        return;
    }
    */
    // Display alert with input values
    alert("incorrect username");

    // Optionally, you can reset the form after submission
    document.getElementById("loginForm").reset();
});