# Generated by Django 4.1.7 on 2023-04-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0003_alter_introduction_big_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='LINK_1_URL',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='introduction',
            name='LINK_2_URL',
            field=models.CharField(max_length=200),
        ),
    ]
