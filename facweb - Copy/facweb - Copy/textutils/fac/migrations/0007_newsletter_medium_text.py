# Generated by Django 4.1.7 on 2023-04-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0006_newsletter_alter_introduction_big_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='MEDIUM_TEXT',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]