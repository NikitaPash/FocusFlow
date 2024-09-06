from django import forms
from django.forms import inlineformset_factory, TextInput

from .models import Project, Feature, SubFeature


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "name": "title",
                "id": "InputTitle",
                "placeholder": "Add title",
            }
        )
    )
    description = forms.CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "name": "description",
                "id": "InputDescription",
                "placeholder": "Add description",
            }
        )
    )

    class Meta:
        model = Project
        fields = ("title", "description")


class FeatureForm(forms.ModelForm):
    feature_name = forms.CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "name": "feature_name",
                "id": "InputFeatureName",
                "placeholder": "Add Feature",
            }
        )
    )

    class Meta:
        model = Feature
        fields = ("feature_name",)


class SubFeatureForm(forms.ModelForm):
    subfeature_name = forms.CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "name": "subfeature_name",
                "id": "InputSubFeature",
                "placeholder": "Add SubFeature",
            }
        )
    )

    class Meta:
        model = SubFeature
        fields = ("subfeature_name",)


FeatureFormSet = inlineformset_factory(
    Project, Feature, form=FeatureForm, extra=1, can_delete=True
)
SubFeatureFormSet = inlineformset_factory(
    Feature, SubFeature, form=SubFeatureForm, extra=1, can_delete=True
)
