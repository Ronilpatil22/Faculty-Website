# Generated by Django 4.1.3 on 2023-04-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0015_navbar_navbar_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediabar',
            old_name='icon_link',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='socialmediabar',
            old_name='name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='socialmediabar',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='socialmediabar',
            name='image',
        ),
    ]