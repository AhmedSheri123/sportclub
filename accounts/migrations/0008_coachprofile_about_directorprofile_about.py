# Generated by Django 4.2.15 on 2024-08-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_coachprofile_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachprofile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='directorprofile',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
