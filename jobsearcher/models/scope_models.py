from django.db import models


class Scope(models.Model):
    class Area(models.TextChoices):
        IT = ('IT', 'Information Technology')
        EG = ('EG', 'Engineering and Manufacturing')
        BS = ('BS', 'Business')
        HC = ('HC', 'HealthCare')
        LW = ('LW', 'Law')

    name = models.CharField(max_length=30, choices=Area.choices, default=Area.IT)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return self.name