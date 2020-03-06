from django.contrib.auth.models import User
from django.db import models

from jobsearcher.models import *


class Company(User):
    telephone = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True,max_length=50)
    url = models.URLField(blank=True, null=True)
    scope = models.ForeignKey(Scope, null=True, related_name="companies", on_delete=models.SET_NULL)

    modified_by = models.ForeignKey(User, null=True, related_name="companies", on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False, null=False)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        default_related_name = "Company"


class JobOffer(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)
    company = models.ForeignKey(Company, related_name="joboffers", on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, null=True, related_name="joboffers", on_delete=models.SET_NULL)
    description = models.TextField()

    modified_by = models.ForeignKey(User, null=True, related_name="joboffers_mod", on_delete=models.SET_NULL)
    deleted = models.BooleanField(default=False, null=False)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = "JobOffer"
