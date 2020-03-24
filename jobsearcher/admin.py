from django.contrib import admin

# Register your models here.
from jobsearcher import models


admin.site.register(models.Company)
admin.site.register(models.Applicant)
admin.site.register(models.Scope)
admin.site.register(models.Theme)
admin.site.register(models.JobOffer)
admin.site.register(models.Choice)
