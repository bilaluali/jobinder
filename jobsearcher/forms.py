from django.contrib.auth.forms import UserCreationForm
from django import forms
from jobsearcher.models import Company


class CompanyForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = Company
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Company',
            'password1': 'Create Password',
            'password2': 'Confirm Password',
        }

    '''def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user'''
