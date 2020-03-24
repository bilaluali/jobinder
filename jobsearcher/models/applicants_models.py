from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from jobsearcher.models import Theme, Scope


class Applicant(User):
    telephone = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    zipCode = models.CharField(blank=True, null=True, max_length=16)
    description = models.TextField(blank=True, null=True)
    scope = models.ForeignKey(Scope, null=True, blank=True, related_name="applicants", on_delete=models.SET_NULL)
    themes = models.ManyToManyField(Theme, blank=True, related_name="applicants")
    photo = models.ImageField(upload_to="applicant_logos/", blank=True, null=True)

    modified_by = models.ForeignKey(User, null=True, related_name="applicants", on_delete=models.SET_NULL)
    last_modified = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('jobsearcher:applicant_detail', kwargs={'pk': self.pk})

    def get_absolute_url_edit(self):
        return reverse('jobsearcher:applicant_profile_info_edit', kwargs={'pk': self.pk})

    def get_absolute_url_delete(self):
        return reverse('jobsearcher:applicant_delete', kwargs={'pk': self.pk})

    class Meta:
        default_related_name = "Applicant"