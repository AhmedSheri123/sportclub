# Generated by Django 4.2.15 on 2024-08-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_blog_club_blog_creator_blogclassificationmodel_club_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesmodel',
            name='classification',
            field=models.ManyToManyField(blank=True, to='students.productsclassificationmodel'),
        ),
    ]
