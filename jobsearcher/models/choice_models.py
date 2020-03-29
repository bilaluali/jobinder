from django.db import models
from jobsearcher.models import Applicant, Company, JobOffer


class Choice(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    jobOffer = models.ForeignKey(JobOffer, null=True, blank=True, on_delete=models.CASCADE)

    choice = models.BooleanField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        msg = " liked " if self.choice else " noped "
        if self.company is None:
            return self.applicant.username + msg + self.jobOffer.name
        else:
            return self.company.username + msg + self.applicant.username