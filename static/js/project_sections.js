function showSection(sectionId) {
    const sections = document.querySelectorAll('.project-info-section');
    sections.forEach(section => section.style.display = 'none');

    document.getElementById(sectionId).style.display = 'block';

    const buttons = document.querySelectorAll('.section-btn');
    buttons.forEach(button => button.classList.remove('active'));

    const activeButton = document.querySelector(`[onclick="showSection('${sectionId}')"]`);
    activeButton.classList.add('active');
}
