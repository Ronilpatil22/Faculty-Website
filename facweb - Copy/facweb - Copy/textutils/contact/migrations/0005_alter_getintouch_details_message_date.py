# Generated by Django 4.1.7 on 2023-04-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_getintouch_details_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getintouch_details',
            name='Message_date',
            field=models.DateField(default='11/09/2001'),
        ),
    ]