# Generated by Django 3.2.18 on 2023-06-21 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('from_location', models.IntegerField()),
                ('to_location', models.IntegerField()),
                ('transport', models.IntegerField()),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FixedRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('from_location', models.IntegerField()),
                ('to_location', models.IntegerField()),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('direct_routes', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='FlyingRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('from_location', models.IntegerField()),
                ('to_location', models.IntegerField()),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('direct_routes', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('from_location', models.IntegerField()),
                ('to_location', models.IntegerField()),
                ('price', models.FloatField()),
                ('duration', models.IntegerField()),
                ('direct_routes', models.JSONField()),
            ],
        ),
    ]
