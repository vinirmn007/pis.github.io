# Generated by Django 5.0.6 on 2024-06-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrazoRobotico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='codo',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hombro',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='muneca',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pinza',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servo',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
    ]
