# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 00:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childtask',
            name='time_ended_hour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='childtask',
            name='time_ended_min',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='childtask',
            name='time_started_hour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='childtask',
            name='time_started_min',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='parenttask',
            name='time_ended_hour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='parenttask',
            name='time_ended_min',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='parenttask',
            name='time_started_hour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='parenttask',
            name='time_started_min',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='childtask',
            name='time_end_min',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='childtask',
            name='time_start_min',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='parenttask',
            name='time_end_min',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='parenttask',
            name='time_start_min',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60)]),
        ),
    ]
