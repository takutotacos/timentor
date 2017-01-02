# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 22:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('task_name', models.CharField(max_length=256)),
                ('time', models.CharField(max_length=3)),
                ('time_start_hour', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_start_min', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_end_hour', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_end_min', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('classification', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ParentTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_date', models.CharField(max_length=10)),
                ('task_no', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('task_name', models.CharField(max_length=256)),
                ('time', models.CharField(max_length=3)),
                ('time_start_hour', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_start_min', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_end_hour', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
                ('time_end_min', models.IntegerField(validators=[django.core.validators.MaxValueValidator(24)])),
            ],
        ),
        migrations.AddField(
            model_name='childtask',
            name='parent_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timentor.ParentTask'),
        ),
    ]
