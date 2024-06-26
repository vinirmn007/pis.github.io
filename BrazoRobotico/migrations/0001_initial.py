# Generated by Django 5.0.6 on 2024-06-06 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VOLTAJE', models.DecimalField(decimal_places=2, max_digits=5)),
                ('CORRIENTE', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nombre', models.CharField(max_length=50)),
                ('torque', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pinza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('angulo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('servo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrazoRobotico.servo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Muneca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('angulo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('servo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrazoRobotico.servo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hombro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('angulo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('servo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrazoRobotico.servo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Codo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('angulo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('servo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrazoRobotico.servo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('angulo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('servo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BrazoRobotico.servo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
