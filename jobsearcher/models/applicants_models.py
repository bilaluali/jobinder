from django.contrib.auth.models import User
from django.db import models
from jobsearcher.models import Theme, Scope


class Applicant(User):
    telephone = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField()
    scope = models.ForeignKey(Scope, null=True, related_name="applicants",on_delete=models.SET_NULL)
    themes = models.ManyToManyField(Theme,related_name="applicants")

    modified_by = models.ForeignKey(User, null=True, related_name="applicants", on_delete=models.SET_NULL)
    last_modified = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False, null=False)

    '''def save(self):
        la =
        mod = user
        self.save()'''

    def __str__(self):
        return self.first_name, self.last_name
