let featureCount = 0;
let subfeatureCounts = {};

function updateCharCount(inputId, counterId, maxChars) {
    const inputField = document.getElementById(inputId);
    const charCount = inputField.value.length;
    const counter = document.getElementById(counterId);
    counter.textContent = `${charCount}/${maxChars} characters`;
}

function resizeTextarea(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
}

function addFeature() {
    const featureFormsContainer = document.getElementById('feature-forms');

    const newFeatureDiv = document.createElement('div');
    newFeatureDiv.classList.add('mb-1');

    const featureLabel = document.createElement('label');
    featureLabel.textContent = 'Feature';
    featureLabel.classList.add('d-block', 'opacity-75');
    newFeatureDiv.appendChild(featureLabel);

    const newFeatureInput = document.createElement('textarea');
    newFeatureInput.name = `feature_name_${featureCount}`;
    newFeatureInput.id = `id_feature_name_${featureCount}`;
    newFeatureInput.classList.add('form-control', 'mb-2');
    newFeatureInput.placeholder = 'Enter feature';
    newFeatureInput.maxLength = 100;
    newFeatureInput.rows = 1;

    newFeatureInput.addEventListener('input', function () {
        updateCharCount(newFeatureInput.id, featureCharCount.id, 100);
        resizeTextarea(newFeatureInput);
    });

    newFeatureDiv.appendChild(newFeatureInput);

    const featureCharCount = document.createElement('small');
    featureCharCount.id = `FeatureCharCount_${featureCount}`;
    featureCharCount.classList.add('form-text', 'text-muted');
    featureCharCount.textContent = '0/100 characters';
    newFeatureDiv.appendChild(featureCharCount);

    const subFeatureLabel = document.createElement('label');
    subFeatureLabel.textContent = 'Subfeatures:';
    subFeatureLabel.classList.add('d-block', 'ms-4', 'opacity-75');
    newFeatureDiv.appendChild(subFeatureLabel);

    const addSubFeatureButton = document.createElement('button');
    addSubFeatureButton.type = 'button';
    addSubFeatureButton.textContent = '+ Add SubFeature';
    addSubFeatureButton.classList.add('link-primary', 'link-offset-2', 'text-decoration-none', 'opacity-75');
    addSubFeatureButton.style.cssText = "background: none; border: none; padding: 0; font: inherit; cursor: pointer;";

    addSubFeatureButton.onclick = (function (featureIndex) {
        return function () {
            addSubFeature(featureIndex);
        };
    })(featureCount);

    const subFeatureContainer = document.createElement('div');
    subFeatureContainer.id = `subfeature-container-${featureCount}`;
    subFeatureContainer.style.marginLeft = '20px';

    newFeatureDiv.appendChild(subFeatureContainer);
    newFeatureDiv.appendChild(addSubFeatureButton);

    featureFormsContainer.appendChild(newFeatureDiv);

    subfeatureCounts[featureCount] = 0;

    featureCount++;
}

function addSubFeature(featureIndex) {
    const subFeatureContainer = document.getElementById(`subfeature-container-${featureIndex}`);

    const newSubFeatureDiv = document.createElement('div');
    newSubFeatureDiv.classList.add('mb-2');
    newSubFeatureDiv.style.marginLeft = '20px';

    const newSubFeatureInput = document.createElement('textarea');
    newSubFeatureInput.name = `subfeature_name_${featureIndex}_${subfeatureCounts[featureIndex]}`;
    newSubFeatureInput.id = `id_subfeature_name_${featureIndex}_${subfeatureCounts[featureIndex]}`;
    newSubFeatureInput.classList.add('form-control');
    newSubFeatureInput.placeholder = 'Enter Subfeature';
    newSubFeatureInput.maxLength = 100;
    newSubFeatureInput.rows = 1;

    newSubFeatureInput.addEventListener('input', function () {
        updateCharCount(newSubFeatureInput.id, subFeatureCharCount.id, 100);
        resizeTextarea(newSubFeatureInput);
    });

    newSubFeatureDiv.appendChild(newSubFeatureInput);

    const subFeatureCharCount = document.createElement('small');
    subFeatureCharCount.id = `SubFeatureCharCount_${featureIndex}_${subfeatureCounts[featureIndex]}`;
    subFeatureCharCount.classList.add('form-text', 'text-muted');
    subFeatureCharCount.textContent = '0/100 characters';
    newSubFeatureDiv.appendChild(subFeatureCharCount);

    subFeatureContainer.appendChild(newSubFeatureDiv);

    subfeatureCounts[featureIndex]++;
}
