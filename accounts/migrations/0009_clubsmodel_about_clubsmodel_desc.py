# Generated by Django 4.2.15 on 2024-08-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_coachprofile_about_directorprofile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubsmodel',
            name='about',
            field=models.TextField(max_length=255, null=True, verbose_name='نبذة'),
        ),
        migrations.AddField(
            model_name='clubsmodel',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name='وصف قصير'),
        ),
    ]
