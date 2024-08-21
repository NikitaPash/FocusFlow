document.addEventListener("DOMContentLoaded", function() {
    const editProfileButton = document.getElementById("editProfileButton");
    const editProfileForm = document.getElementById("editProfileForm");
    const cancelButton = document.getElementById("cancelButton");
    const form = editProfileForm.querySelector("form");

    // Show the form and hide the "Edit Profile" button
    editProfileButton.addEventListener("click", function() {
        editProfileButton.style.display = "none";
        editProfileForm.style.display = "block";
    });

    // Hide the form and reset it, show the "Edit Profile" button
    cancelButton.addEventListener("click", function() {
        editProfileForm.style.display = "none";
        editProfileButton.style.display = "block";
        form.reset(); // Reset the form fields
        const errorMessages = editProfileForm.querySelectorAll(".field-errors");
        errorMessages.forEach((error) => error.innerHTML = ""); // Clear error messages
    });

    // Keep the form open if there are errors immediately after form submission
    const hasErrors = editProfileForm.querySelectorAll(".text-danger").length > 0;
    if (hasErrors && performance.navigation.type === performance.navigation.TYPE_RELOAD) {
        form.reset(); // Reset the form if the page is reloaded
        const errorMessages = editProfileForm.querySelectorAll(".field-errors");
        errorMessages.forEach((error) => error.innerHTML = ""); // Clear error messages
    } else if (hasErrors) {
        editProfileButton.style.display = "none";
        editProfileForm.style.display = "block";
    }
});