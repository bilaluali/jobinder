# Generated by Django 3.0.3 on 2020-03-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearcher', '0011_auto_20200314_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='themes',
            field=models.ManyToManyField(blank=True, related_name='applicants', to='jobsearcher.Theme'),
        ),
    ]