# Generated by Django 4.1.7 on 2023-04-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0011_contact_form_submit_message_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contacts',
        ),
    ]
