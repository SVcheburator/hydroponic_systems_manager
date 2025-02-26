# Generated by Django 5.1.5 on 2025-02-01 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HydroponicSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='systems', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.FloatField()),
                ('temperature', models.FloatField()),
                ('tds', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='hydroponic_api.hydroponicsystem')),
            ],
        ),
    ]
