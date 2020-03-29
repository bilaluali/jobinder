from django.db import models


class Scope(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=128)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return self.name