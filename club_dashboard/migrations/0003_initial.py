# Generated by Django 4.2.15 on 2024-08-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club_dashboard', '0002_remove_studentappointmentpresence_appointment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsStockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('creation_date', models.DateTimeField(null=True, verbose_name='تاريخ الانشاء')),
            ],
        ),
    ]
