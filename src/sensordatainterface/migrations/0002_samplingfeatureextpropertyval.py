# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sensordatainterface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SamplingFeatureExtPropertyVal',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[SamplingFeatureExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
