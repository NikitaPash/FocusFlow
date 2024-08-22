document.addEventListener("DOMContentLoaded", function() {
    const editProfileButton = document.getElementById("editProfileButton");
    const editProfileForm = document.getElementById("editProfileForm");
    const cancelButton = document.getElementById("cancelButton");
    const form = editProfileForm.querySelector("form");

    editProfileButton.addEventListener("click", function() {
        editProfileButton.style.display = "none";
        editProfileForm.style.display = "block";
    });

    cancelButton.addEventListener("click", function() {
        editProfileForm.style.display = "none";
        editProfileButton.style.display = "block";
        form.reset();
        const errorMessages = editProfileForm.querySelectorAll(".field-errors");
        errorMessages.forEach((error) => error.innerHTML = "");
    });

    const hasErrors = editProfileForm.querySelectorAll(".text-danger").length > 0;
    if (hasErrors && performance.navigation.type === performance.navigation.TYPE_RELOAD) {
        form.reset();
        const errorMessages = editProfileForm.querySelectorAll(".field-errors");
        errorMessages.forEach((error) => error.innerHTML = "");
    } else if (hasErrors) {
        editProfileButton.style.display = "none";
        editProfileForm.style.display = "block";
    }
});