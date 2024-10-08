# Generated by Django 4.2.15 on 2024-09-04 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True, default='')),
                ('evaluation', models.DecimalField(decimal_places=1, max_digits=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assessments', to='api_test_django.course')),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
                'unique_together': {('email', 'course')},
            },
        ),
    ]
