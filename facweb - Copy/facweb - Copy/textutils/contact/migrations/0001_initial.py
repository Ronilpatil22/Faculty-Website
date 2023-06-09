# Generated by Django 4.1.7 on 2023-04-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BIG_TEXT_LEFT', models.CharField(blank=True, max_length=2000)),
                ('SMALL_TEXT', models.CharField(blank=True, max_length=2000)),
                ('ADDRESS', models.CharField(blank=True, max_length=2000)),
                ('PHONE', models.CharField(blank=True, max_length=2000)),
                ('EMAIL', models.EmailField(blank=True, max_length=254)),
                ('WEBSITE', models.URLField(blank=True)),
                ('FORM_BIG_TEXT', models.CharField(blank=True, max_length=2000)),
                ('FORM_SUBMIT_MESSAGE_TEXT', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]
