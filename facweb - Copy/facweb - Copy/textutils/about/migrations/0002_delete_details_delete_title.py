# Generated by Django 4.1.7 on 2023-04-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DETAILS',
        ),
        migrations.DeleteModel(
            name='title',
        ),
    ]