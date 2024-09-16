function updateCharCount(inputId, counterId, maxChars) {
    const inputField = document.getElementById(inputId);
    const charCount = inputField.value.length;
    const counter = document.getElementById(counterId);
    counter.textContent = `${charCount}/${maxChars} characters`;
}

function resizeTextarea(textarea) {
    textarea.style.height = textarea.scrollHeight + 'px';
}

document.addEventListener('DOMContentLoaded', () => {
    updateCharCount('InputFullName', 'fullNameCharCount', 30);
    updateCharCount('InputBio', 'bioCharCount', 160);
    resizeTextarea(document.getElementById('InputBio'));
});