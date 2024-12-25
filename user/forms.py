from django import forms

from user.models import Profile


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = [
            'id', 'dating_sex', 'location', 'min_distance',
            'max_distance', 'min_dating_age', 'max_dating_age',
            'vibration', 'only_matche', 'outo_play',
        ]

    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age > max_dating_age')



