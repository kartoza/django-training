# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterestZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('acquisition_date', models.DateTimeField(auto_now=True, verbose_name=b'DateAdded')),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(help_text=b'Area', srid=4326, null=True, blank=True)),
            ],
            options={
                'ordering': ('acquisition_date',),
                'verbose_name': 'Interest Zone',
                'verbose_name_plural': 'Interest Zones',
            },
        ),
        migrations.CreateModel(
            name='ZoneType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='interestzone',
            name='zone_type',
            field=models.ForeignKey(to='demo_app.ZoneType'),
        ),
    ]
