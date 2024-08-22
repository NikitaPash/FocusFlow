from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    full_name = forms.CharField(required=False)
    website = forms.URLField(required=False)
    github = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    email = forms.EmailField(required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ("bio", "full_name", "website", "github", "linkedin", "email", "profile_image")

    def save(self, commit=True):
        instance = super().save(commit=False)
        fields_to_update = []

        for field in self.changed_data:
            if field in self.fields:
                fields_to_update.append(field)

        if commit:
            if fields_to_update:
                instance.save(update_fields=fields_to_update)
            else:
                instance.save()

        return instance
