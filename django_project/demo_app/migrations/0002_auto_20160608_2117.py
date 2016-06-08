# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interestzone',
            options={'ordering': ('acquisition_date', 'name'), 'verbose_name': 'Interest Zone', 'verbose_name_plural': 'Interest Zones'},
        ),
    ]
