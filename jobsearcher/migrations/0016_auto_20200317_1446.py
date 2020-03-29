# Generated by Django 3.0.3 on 2020-03-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearcher', '0015_auto_20200317_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='applicant_logos/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logos/'),
        ),
    ]
