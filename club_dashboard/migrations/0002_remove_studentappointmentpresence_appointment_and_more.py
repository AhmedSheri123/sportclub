# Generated by Django 4.2.15 on 2024-08-15 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentappointmentpresence',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='studentappointmentpresence',
            name='student',
        ),
        migrations.DeleteModel(
            name='CoachAppointmentsModel',
        ),
        migrations.DeleteModel(
            name='StudentAppointmentPresence',
        ),
    ]
