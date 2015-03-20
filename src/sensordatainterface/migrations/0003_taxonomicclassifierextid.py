# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sensordatainterface', '0002_samplingfeatureextpropertyval'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxonomicClassifierExtId',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('taxonomicclassifierexternalidentifier',
                 models.TextField(db_column='TaxonomicClassifierExternalIdentifier')),
                ('taxonomicclassifierexternalidentifieruri',
                 models.TextField(db_column='TaxonomicClassifierExternalIdentifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[TaxonomicClassifierExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
