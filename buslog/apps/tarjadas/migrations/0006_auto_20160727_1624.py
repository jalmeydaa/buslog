# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarjadas', '0005_auto_20160727_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_choferes', to=settings.AUTH_USER_MODEL),
        ),
    ]
