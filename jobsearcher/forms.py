from django.contrib.auth.forms import UserCreationForm
from django import forms
from jobsearcher.models import Company, Scope, Applicant


class CompanyForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Company
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'telephone',
            'city',
            'zipCode',
            'url',
        )


class ApplicantForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Applicant
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'telephone',
            'city',
            'zipCode',
            'description',
        )

