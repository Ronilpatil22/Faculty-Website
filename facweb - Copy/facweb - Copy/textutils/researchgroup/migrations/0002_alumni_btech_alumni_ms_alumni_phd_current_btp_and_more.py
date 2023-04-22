# Generated by Django 4.1.7 on 2023-04-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchgroup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumni_btech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
                ('Position', models.CharField(blank=True, max_length=2000)),
                ('Company', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='alumni_ms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
                ('Area_of_research', models.CharField(blank=True, max_length=2000)),
                ('google_scholar_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='alumni_phd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
                ('Area_of_research', models.CharField(blank=True, max_length=2000)),
                ('google_scholar_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='current_btp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='current_research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
                ('Area_of_research', models.CharField(blank=True, max_length=2000)),
                ('google_scholar_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='interns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, upload_to='current_research/images')),
                ('Name', models.CharField(max_length=2000)),
                ('Period', models.CharField(blank=True, max_length=2000)),
                ('Education', models.CharField(blank=True, max_length=2000)),
                ('Area_of_research', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='research_group_details',
            name='Class',
        ),
        migrations.DeleteModel(
            name='research_group_class',
        ),
        migrations.DeleteModel(
            name='research_group_details',
        ),
    ]