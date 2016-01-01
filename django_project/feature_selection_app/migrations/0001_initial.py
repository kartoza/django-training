# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doodle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('doodle_date', models.DateTimeField(auto_now=True, verbose_name=b'DateAdded')),
            ],
            options={
                'ordering': ('doodle_date',),
                'verbose_name': 'Doodle',
                'verbose_name_plural': 'Doodles',
            },
        ),
        migrations.CreateModel(
            name='DoodleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
                'db_table': 'doodletype',
                'verbose_name': 'Doodle Type',
                'verbose_name_plural': 'Doodle Types',
            },
        ),
        migrations.AddField(
            model_name='doodle',
            name='doodle_type',
            field=models.ForeignKey(to='feature_selection_app.DoodleType'),
        ),
    ]
