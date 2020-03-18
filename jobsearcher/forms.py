from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from jobsearcher.models import Company, Scope, Applicant, JobOffer, Theme


class CompanyForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Company
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'scope',
            'telephone',
            'city',
            'zipCode',
            'url',
            'logo',
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
            'scope',
            'themes',
            'telephone',
            'city',
            'zipCode',
            'description',
            'photo',
        )


class JobOfferForm(ModelForm):
    class Meta:
        model = JobOffer
        fields = (
            'name',
            'description',
            'company',
            'theme',
        )
