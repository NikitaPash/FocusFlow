let featureCount = 0;
let subfeatureCounts = {};

function addFeature() {
    const featureFormsContainer = document.getElementById('feature-forms');

    const newFeatureDiv = document.createElement('div');
    newFeatureDiv.classList.add('mb-1');

    const featureLabel = document.createElement('label');
    featureLabel.textContent = 'Feature';
    featureLabel.classList.add('d-block', 'opacity-75');
    newFeatureDiv.appendChild(featureLabel);

    const newFeatureInput = document.createElement('input');
    newFeatureInput.type = 'text';
    newFeatureInput.name = `feature_name_${featureCount}`;
    newFeatureInput.id = `id_feature_name_${featureCount}`;
    newFeatureInput.classList.add('form-control', 'mb-2');
    newFeatureInput.placeholder = 'Enter feature';

    newFeatureDiv.appendChild(newFeatureInput);

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

    const newSubFeatureInput = document.createElement('input');
    newSubFeatureInput.type = 'text';
    newSubFeatureInput.name = `subfeature_name_${featureIndex}_${subfeatureCounts[featureIndex]}`;
    newSubFeatureInput.id = `id_subfeature_name_${featureIndex}_${subfeatureCounts[featureIndex]}`;
    newSubFeatureInput.classList.add('form-control');
    newSubFeatureInput.placeholder = 'Enter Subfeature';

    newSubFeatureDiv.appendChild(newSubFeatureInput);
    subFeatureContainer.appendChild(newSubFeatureDiv);

    subfeatureCounts[featureIndex]++;
}
