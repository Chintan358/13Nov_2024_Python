# Generated by Django 5.1.4 on 2025-01-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_myuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='education',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='lang',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
