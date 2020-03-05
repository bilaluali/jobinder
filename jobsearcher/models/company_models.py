from django.contrib.auth.models import User
from django.db import models

from jobsearcher.models import Scope


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
