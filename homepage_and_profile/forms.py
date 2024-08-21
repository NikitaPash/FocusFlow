from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    full_name = forms.CharField(required=False)
    website = forms.URLField(required=False)
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ("bio", "full_name", "website", "github", "linkedin", "email")


    def save(self, commit=True):
        instance = super().save(commit=False)

        fields_to_update = []
        for field in instance._meta.fields:
            field_name = field.name
            if field_name == "id":
                continue

            field_value = getattr(instance, field_name)
            if field_value not in [None, ""]:
                fields_to_update.append(field_name)

        if commit:
            instance.save(update_fields=fields_to_update)

        return instance
