# Generated by Django 4.1.7 on 2023-04-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0007_newsletter_medium_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='socialmediabar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('icon', models.CharField(max_length=2000)),
                ('icon_link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='SMALL_TEXT',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
