from django import forms
from django.forms import TextInput, Textarea

from .models import Project, Feature, SubFeature


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        widget=Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter title",
            "maxlength": "100",
            "id": "InputTitle",
            "style": "height: 10px",
            "oninput": "updateCharCount('InputTitle', 'TitleCharCount', 100); resizeTextarea(this);"
        })
    )
    description = forms.CharField(
        widget=Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter description",
            "maxlength": "350",
            "id": "InputDescription",
            "style": "height: 10px",
            "oninput": "updateCharCount('InputDescription', 'DescriptionCharCount', 350); resizeTextarea(this);"
        })
    )

    class Meta:
        model = Project
        fields = ("title", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            features = Feature.objects.filter(project=self.instance)
            for i, feature in enumerate(features):
                field_name = f"feature_name_{i}"
                self.fields[field_name] = forms.CharField(
                    initial=feature.feature_name,
                    widget=TextInput(
                        attrs={"class": "form-control", "placeholder": "Enter feature"}
                    ),
                )
            field_name = f"feature_name_{len(features)}"
            self.fields[field_name] = forms.CharField(
                required=False,
                widget=TextInput(
                    attrs={"class": "form-control", "placeholder": "Enter feature"}
                ),
            )

    def clean(self):
        cleaned_data = super().clean()
        feature_fields = [
            field for field in self.data if field.startswith("feature_name_")
        ]
        features = set()

        for field_name in feature_fields:
            feature_name = self.data.get(field_name)
            if feature_name and feature_name not in features:
                features.add(feature_name)

        cleaned_data["features"] = features
        return cleaned_data

    def save(self, commit=True):
        project = super().save(commit=False)
        project.title = self.cleaned_data["title"]
        project.description = self.cleaned_data["description"]

        if commit:
            project.save()
            for feature_name in self.cleaned_data["features"]:
                if feature_name:
                    Feature.objects.create(project=project, feature_name=feature_name)
        return project


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ("feature_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            subfeatures = SubFeature.objects.filter(feature=self.instance)
            for i, subfeature in enumerate(subfeatures):
                field_name = f"subfeature_name_{i}"
                self.fields[field_name] = forms.CharField(
                    initial=subfeature.subfeature_name,
                    widget=TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": "Enter Subfeature",
                        }
                    ),
                )
            field_name = f"subfeature_name_{len(subfeatures)}"
            self.fields[field_name] = forms.CharField(
                required=False,
                widget=TextInput(
                    attrs={"class": "form-control", "placeholder": "Enter Subfeature"}
                ),
            )

    def clean(self):
        cleaned_data = super().clean()
        subfeature_fields = [
            field for field in self.data if field.startswith("subfeature_name_")
        ]
        subfeatures = set()

        for field_name in subfeature_fields:
            subfeature_name = self.data.get(field_name)
            if subfeature_name and subfeature_name not in subfeatures:
                subfeatures.add(subfeature_name)

        cleaned_data["subfeatures"] = subfeatures
        return cleaned_data

    def save(self, commit=True):
        feature = super().save(commit=False)

        if commit:
            feature.save()
            for subfeature_name in self.cleaned_data["subfeatures"]:
                if subfeature_name:
                    SubFeature.objects.create(
                        feature=feature, subfeature_name=subfeature_name
                    )
        return feature
