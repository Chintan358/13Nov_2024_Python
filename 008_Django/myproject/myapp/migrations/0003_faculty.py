# Generated by Django 5.1.4 on 2025-01-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_email_student_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=30)),
                ('faculty_subject', models.CharField(max_length=20)),
            ],
        ),
    ]