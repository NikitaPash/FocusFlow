function updateCharCount(inputId, counterId, maxChars) {
    const inputField = document.getElementById(inputId);
    const charCount = inputField.value.length;
    const counter = document.getElementById(counterId);
    counter.textContent = `${charCount}/${maxChars} characters`;
}


document.addEventListener('DOMContentLoaded', function () {
    const toggleEditBtn = document.getElementById('toggleEditBtn');
    const descriptionText = document.getElementById('descriptionText');
    const editDescriptionForm = document.getElementById('editDescriptionForm');
    const descriptionInput = document.getElementById('descriptionInput');
    const saveDescriptionBtn = document.getElementById('saveDescriptionBtn');
    const charCounter = document.getElementById('charCounter');
    const maxChars = 2000;

    updateCharCount('descriptionInput', 'charCounter', maxChars);

    descriptionInput.addEventListener('input', function () {
        updateCharCount('descriptionInput', 'charCounter', maxChars);
    });

    let formVisible = false;
    let originalDescription = descriptionText.querySelector('p').innerText;

    toggleEditBtn.addEventListener('click', function () {
        formVisible = !formVisible;

        if (formVisible) {
            editDescriptionForm.style.display = 'block';
            descriptionText.classList.add('p-hidden');

            if (originalDescription !== 'No details yet :(') {
                descriptionInput.value = originalDescription;
            } else {
                descriptionInput.value = '';
            }

            autoResize(descriptionInput);
        } else {
            editDescriptionForm.style.display = 'none';
            descriptionText.classList.remove('p-hidden');
            descriptionInput.value = originalDescription;
        }
    });

    descriptionInput.addEventListener('input', function () {
        autoResize(descriptionInput);
    });

    saveDescriptionBtn.addEventListener('click', function () {
        originalDescription = descriptionInput.value;
        editDescriptionForm.style.display = 'none';
        descriptionText.classList.remove('p-hidden');
        descriptionText.querySelector('p').innerText = originalDescription || 'No details yet :(';
        formVisible = false;
    });

    function autoResize(textarea) {
        const startScrollPos = window.pageYOffset;
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
        window.scrollTo(0, startScrollPos);
    }
});
