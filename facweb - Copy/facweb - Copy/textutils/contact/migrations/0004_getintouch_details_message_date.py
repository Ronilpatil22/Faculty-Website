# Generated by Django 4.1.7 on 2023-04-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_getintouch_details_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='getintouch_details',
            name='Message_date',
            field=models.DateField(default=None),
        ),
    ]
