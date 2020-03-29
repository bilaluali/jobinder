from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from jobsearcher.models import Theme, Scope


class Company(User):
    telephone = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    zipCode = models.CharField(blank=True, null=True, max_length=16)
    url = models.URLField(blank=True, null=True)
    scope = models.ForeignKey(Scope, blank=True, null=True, related_name="companies", on_delete=models.SET_NULL)
    logo = models.ImageField(upload_to="company_logos/", default='applicant_logos/default.png', blank=True, null=True)

    modified_by = models.ForeignKey(User, null=True, related_name="companies", on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False, null=False)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.username

    def get_absolute_url_edit(self):
        return reverse('jobsearcher:company_profile_info_edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('jobsearcher:company_delete', kwargs={'pk': self.pk})

    class Meta:
        default_related_name = "Company"


class JobOffer(models.Model):
    name = models.CharField(max_length=30)
    company = models.ForeignKey(Company, blank=True, related_name="joboffers", on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, null=True, blank=True, related_name="joboffers", on_delete=models.SET_NULL)
    description = models.TextField()

    modified_by = models.ForeignKey(User, null=True, related_name="joboffers_mod", on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False, null=False)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobsearcher:joboffer_detail', kwargs={'pk': self.pk})

    def get_absolute_url_edit(self):
        return reverse('jobsearcher:joboffer_edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('jobsearcher:joboffer_delete', kwargs={'pk': self.pk})

    class Meta:
        default_related_name = "JobOffer"