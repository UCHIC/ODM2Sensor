# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('actionid', models.IntegerField(serialize=False, primary_key=True, db_column='ActionID')),
                ('actiontypecv', models.TextField(db_column='ActionTypeCV')),
                ('begindatetime', models.DateTimeField(db_column='BeginDateTime')),
                ('begindatetimeutcoffset', models.IntegerField(db_column='BeginDateTimeUTCOffset')),
                ('enddatetime', models.DateTimeField(null=True, db_column='EndDateTime', blank=True)),
                ('enddatetimeutcoffset', models.IntegerField(null=True, db_column='EndDateTimeUTCOffset', blank=True)),
                ('actiondescription', models.TextField(db_column='ActionDescription', blank=True)),
                ('actionfilelink', models.TextField(db_column='ActionFileLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[Actions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[ActionAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionBy',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('isactionlead', models.BooleanField(db_column='IsActionLead')),
                ('roledescription', models.TextField(db_column='RoleDescription', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[ActionBy',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionDirective',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2LabAnalyses].[ActionDirectives',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[ActionExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('affiliationid', models.IntegerField(serialize=False, primary_key=True, db_column='AffiliationID')),
                ('isprimaryorganizationcontact', models.NullBooleanField(db_column='IsPrimaryOrganizationContact')),
                ('affiliationstartdate', models.DateField(db_column='AffiliationStartDate')),
                ('affiliationenddate', models.DateField(null=True, db_column='AffiliationEndDate', blank=True)),
                ('primaryphone', models.TextField(db_column='PrimaryPhone', blank=True)),
                ('primaryemail', models.TextField(db_column='PrimaryEmail')),
                ('primaryaddress', models.TextField(db_column='PrimaryAddress', blank=True)),
                ('personlink', models.TextField(db_column='PersonLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[Affiliations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('annotationid', models.IntegerField(serialize=False, primary_key=True, db_column='AnnotationID')),
                ('annotationtypecv', models.TextField(db_column='AnnotationTypeCV')),
                ('annotationcode', models.TextField(db_column='AnnotationCode', blank=True)),
                ('annotationtext', models.TextField(db_column='AnnotationText')),
                ('annotationdatetime', models.DateTimeField(null=True, db_column='AnnotationDateTime', blank=True)),
                ('annotationutcoffset', models.IntegerField(null=True, db_column='AnnotationUTCOffset', blank=True)),
                ('annotationlink', models.TextField(db_column='AnnotationLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Annotations].[Annotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthorList',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('authororder', models.IntegerField(db_column='AuthorOrder')),
            ],
            options={
                'db_table': 'ODM2Provenance].[AuthorLists',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationAction',
            fields=[
                ('actionid', models.ForeignKey(primary_key=True, db_column='ActionID', serialize=False,
                                               to='sensordatainterface.Action')),
                ('calibrationcheckvalue', models.FloatField(null=True, db_column='CalibrationCheckValue', blank=True)),
                ('calibrationequation', models.TextField(db_column='CalibrationEquation', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[CalibrationActions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationReferenceEquipment',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Equipment].[CalibrationReferenceEquipment',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationStandard',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Equipment].[CalibrationStandards',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoricalResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.TextField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
            ],
            options={
                'db_table': 'ODM2Results].[CategoricalResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoricalResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[CategoricalResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('citationid', models.IntegerField(serialize=False, primary_key=True, db_column='CitationID')),
                ('title', models.TextField(db_column='Title')),
                ('publisher', models.TextField(db_column='Publisher')),
                ('publicationyear', models.IntegerField(db_column='PublicationYear')),
                ('citationlink', models.TextField(db_column='CitationLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Provenance].[Citations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CitationExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[CitationExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CitationExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('citationexternalidentifer', models.TextField(db_column='CitationExternalIdentifer')),
                (
                'citationexternalidentiferuri', models.TextField(db_column='CitationExternalIdentiferURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[CitationExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CvTerm',
            fields=[
                ('termid', models.IntegerField(serialize=False, primary_key=True, db_column='TermID')),
                ('term', models.TextField(db_column='Term')),
                ('definition', models.TextField(db_column='Definition', blank=True)),
                ('odmvocabulary', models.TextField(db_column='ODMVocabulary')),
                ('sourcevocabulary', models.TextField(db_column='SourceVocabulary', blank=True)),
            ],
            options={
                'db_table': 'ODM2CV].[CVTerms',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataloggerFile',
            fields=[
                ('dataloggerfileid', models.AutoField(serialize=False, primary_key=True, db_column='DataLoggerFileID')),
                ('dataloggerfilename', models.TextField(db_column='DataLoggerFileName')),
                ('dataloggerfiledescription', models.TextField(db_column='DataLoggerFileDescription', blank=True)),
                ('dataloggerfilelink', models.TextField(db_column='DataLoggerFileLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[DataLoggerFiles',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataloggerFileColumn',
            fields=[
                ('dataloggerfilecolumnid',
                 models.AutoField(serialize=False, primary_key=True, db_column='DataloggerFileColumnID')),
                ('columnlabel', models.TextField(db_column='ColumnLabel')),
                ('columndescription', models.TextField(db_column='ColumnDescription', blank=True)),
                ('measurementequation', models.TextField(db_column='MeasurementEquation', blank=True)),
                ('scaninterval', models.FloatField(null=True, db_column='ScanInterval', blank=True)),
                ('recordinginterval', models.FloatField(null=True, db_column='RecordingInterval', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[DataloggerFileColumns',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataloggerProgramFile',
            fields=[
                ('programid', models.AutoField(serialize=False, primary_key=True, db_column='ProgramID')),
                ('programname', models.TextField(db_column='ProgramName')),
                ('programdescription', models.TextField(db_column='ProgramDescription', blank=True)),
                ('programversion', models.TextField(db_column='ProgramVersion', blank=True)),
                ('programfilelink', models.TextField(db_column='ProgramFileLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[DataloggerProgramFiles',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataQuality',
            fields=[
                ('dataqualityid', models.IntegerField(serialize=False, primary_key=True, db_column='DataQualityID')),
                ('dataqualitytypecv', models.TextField(db_column='DataQualityTypeCV')),
                ('dataqualitycode', models.TextField(db_column='DataQualityCode')),
                ('dataqualityvalue', models.FloatField(null=True, db_column='DataQualityValue', blank=True)),
                ('dataqualitydescription', models.TextField(db_column='DataQualityDescription', blank=True)),
                ('dataqualitylink', models.TextField(db_column='DataQualityLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2DataQuality].[DataQuality',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('datasetid', models.IntegerField(serialize=False, primary_key=True, db_column='DataSetID')),
                ('datasetuuid', models.TextField(db_column='DataSetUUID')),
                ('datasettypecv', models.TextField(db_column='DataSetTypeCV')),
                ('datasetcode', models.TextField(db_column='DataSetCode')),
                ('datasettitle', models.TextField(db_column='DataSetTitle')),
                ('datasetabstract', models.TextField(db_column='DataSetAbstract')),
            ],
            options={
                'db_table': 'ODM2Core].[DataSets',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatasetCitation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2Provenance].[DataSetCitations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatasetsResult',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Core].[DataSetsResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DerivationEquation',
            fields=[
                ('derivationequationid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='DerivationEquationID')),
                ('derivationequation', models.TextField(db_column='DerivationEquation')),
            ],
            options={
                'db_table': 'ODM2Provenance].[DerivationEquations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Directive',
            fields=[
                ('directiveid', models.IntegerField(serialize=False, primary_key=True, db_column='DirectiveID')),
                ('directivetypecv', models.TextField(db_column='DirectiveTypeCV')),
                ('directivedescription', models.TextField(db_column='DirectiveDescription')),
            ],
            options={
                'db_table': 'ODM2LabAnalyses].[Directives',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipmentid', models.AutoField(serialize=False, primary_key=True, db_column='EquipmentID')),
                ('equipmentcode', models.TextField(db_column='EquipmentCode')),
                ('equipmentname', models.TextField(db_column='EquipmentName')),
                ('equipmenttypecv', models.TextField(db_column='EquipmentTypeCV')),
                ('equipmentserialnumber', models.TextField(db_column='EquipmentSerialNumber')),
                ('equipmentpurchasedate', models.DateTimeField(db_column='EquipmentPurchaseDate')),
                (
                'equipmentpurchaseordernumber', models.TextField(db_column='EquipmentPurchaseOrderNumber', blank=True)),
                ('equipmentdescription', models.TextField(db_column='EquipmentDescription', blank=True)),
                ('equipmentdocumentationlink', models.TextField(db_column='EquipmentDocumentationLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[Equipment',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[EquipmentAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('equipmentmodelid', models.AutoField(serialize=False, primary_key=True, db_column='EquipmentModelID')),
                ('modelpartnumber', models.TextField(db_column='ModelPartNumber', blank=True)),
                ('modelname', models.TextField(db_column='ModelName')),
                ('modeldescription', models.TextField(db_column='ModelDescription', blank=True)),
                ('isinstrument', models.BooleanField(db_column='IsInstrument')),
                ('modelspecificationsfilelink', models.TextField(db_column='ModelSpecificationsFileLink', blank=True)),
                ('modellink', models.TextField(db_column='ModelLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[EquipmentModels',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentUsed',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Equipment].[EquipmentUsed',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtensionProperties',
            fields=[
                ('propertyid', models.IntegerField(serialize=False, primary_key=True, db_column='PropertyID')),
                ('propertyname', models.TextField(db_column='PropertyName')),
                ('propertydescription', models.TextField(db_column='PropertyDescription', blank=True)),
                ('propertydatatypecv', models.TextField(db_column='PropertyDataTypeCV')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[ExtensionProperties',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExternalIdentifierSystem',
            fields=[
                ('externalidentifiersystemid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='ExternalIdentifierSystemID')),
                ('externalidentifiersystemname', models.TextField(db_column='ExternalIdentifierSystemName')),
                ('externalidentifiersystemdescription',
                 models.TextField(db_column='ExternalIdentifierSystemDescription', blank=True)),
                ('externalidentifiersystemurl', models.TextField(db_column='ExternalIdentifierSystemURL', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[ExternalIdentifierSystems',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureAction',
            fields=[
                (
                'featureactionid', models.IntegerField(serialize=False, primary_key=True, db_column='FeatureActionID')),
            ],
            options={
                'db_table': 'ODM2Core].[FeatureActions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstrumentOutputVariable',
            fields=[
                ('instrumentoutputvariableid',
                 models.AutoField(serialize=False, primary_key=True, db_column='InstrumentOutputVariableID')),
                ('instrumentresolution', models.TextField(db_column='InstrumentResolution', blank=True)),
                ('instrumentaccuracy', models.TextField(db_column='InstrumentAccuracy', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[InstrumentOutputVariables',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaintenanceAction',
            fields=[
                ('actionid', models.ForeignKey(primary_key=True, db_column='ActionID', serialize=False,
                                               to='sensordatainterface.Action')),
                ('isfactoryservice', models.BooleanField(db_column='IsFactoryService')),
                ('maintenancecode', models.TextField(db_column='MaintenanceCode', blank=True)),
                ('maintenancereason', models.TextField(db_column='MaintenanceReason', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[MaintenanceActions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
            ],
            options={
                'db_table': 'ODM2Results].[MeasurementResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[MeasurementResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('methodid', models.IntegerField(serialize=False, primary_key=True, db_column='MethodID')),
                ('methodtypecv', models.TextField(db_column='MethodTypeCV')),
                ('methodcode', models.TextField(db_column='MethodCode')),
                ('methodname', models.TextField(db_column='MethodName')),
                ('methoddescription', models.TextField(db_column='MethodDescription', blank=True)),
                ('methodlink', models.TextField(db_column='MethodLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[Methods',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[MethodAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodCitation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2Provenance].[MethodCitations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[MethodExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('methodexternalidentifier', models.TextField(db_column='MethodExternalIdentifier')),
                ('methodexternalidentifieruri', models.TextField(db_column='MethodExternalIdentifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[MethodExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelAffiliation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('isprimary', models.BooleanField(db_column='IsPrimary')),
                ('roledescription', models.TextField(db_column='RoleDescription', blank=True)),
            ],
            options={
                'db_table': 'ODM2Simulation].[ModelAffiliations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('modelid', models.IntegerField(serialize=False, primary_key=True, db_column='ModelID')),
                ('modelcode', models.CharField(max_length=255, db_column='ModelCode')),
                ('modelname', models.CharField(max_length=255, db_column='ModelName')),
                ('modeldescription', models.CharField(max_length=500, db_column='ModelDescription', blank=True)),
                ('version', models.TextField(db_column='Version', blank=True)),
                ('modellink', models.TextField(db_column='ModelLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Simulation].[Models',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organizationid', models.IntegerField(serialize=False, primary_key=True, db_column='OrganizationID')),
                ('organizationtypecv', models.TextField(db_column='OrganizationTypeCV')),
                ('organizationcode', models.TextField(db_column='OrganizationCode')),
                ('organizationname', models.TextField(db_column='OrganizationName')),
                ('organizationdescription', models.TextField(db_column='OrganizationDescription', blank=True)),
                ('organizationlink', models.TextField(db_column='OrganizationLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[Organizations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('personid', models.IntegerField(serialize=False, primary_key=True, db_column='PersonID')),
                ('personfirstname', models.TextField(db_column='PersonFirstName')),
                ('personmiddlename', models.TextField(db_column='PersonMiddleName', blank=True)),
                ('personlastname', models.TextField(db_column='PersonLastName')),
            ],
            options={
                'db_table': 'ODM2Core].[People',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('personexternalidentifier', models.TextField(db_column='PersonExternalIdentifier')),
                ('personexternalidenifieruri', models.TextField(db_column='PersonExternalIdenifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[PersonExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointCoverageResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.BigIntegerField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
                ('xlocation', models.FloatField(db_column='XLocation')),
                ('ylocation', models.FloatField(db_column='YLocation')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
            ],
            options={
                'db_table': 'ODM2Results].[PointCoverageResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointCoverageResultValueAnnotation',
            fields=[
                ('bridgeid', models.BigIntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[PointCoverageResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProcessingLevel',
            fields=[
                ('processinglevelid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='ProcessingLevelID')),
                ('processinglevelcode', models.TextField(db_column='ProcessingLevelCode')),
                ('definition', models.TextField(db_column='Definition', blank=True)),
                ('explanation', models.TextField(db_column='Explanation', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[ProcessingLevels',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
                ('zlocation', models.FloatField(db_column='ZLocation')),
                ('zaggregationinterval', models.FloatField(db_column='ZAggregationInterval')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[ProfileResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[ProfileResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterial',
            fields=[
                ('referencematerialid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='ReferenceMaterialID')),
                ('referencematerialmediumcv', models.TextField(db_column='ReferenceMaterialMediumCV')),
                ('referencematerialcode', models.TextField(db_column='ReferenceMaterialCode')),
                ('referencemateriallotcode', models.TextField(db_column='ReferenceMaterialLotCode', blank=True)),
                ('referencematerialpurchasedate',
                 models.DateTimeField(null=True, db_column='ReferenceMaterialPurchaseDate', blank=True)),
                ('referencematerialexpirationdate',
                 models.DateTimeField(null=True, db_column='ReferenceMaterialExpirationDate', blank=True)),
                ('referencematerialcertificatelink',
                 models.TextField(db_column='ReferenceMaterialCertificateLink', blank=True)),
            ],
            options={
                'db_table': 'ODM2DataQuality].[ReferenceMaterials',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterialExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('referencematerialexternalidentifier',
                 models.TextField(db_column='ReferenceMaterialExternalIdentifier')),
                ('referencematerialexternalidentifieruri',
                 models.TextField(db_column='ReferenceMaterialExternalIdentifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[ReferenceMaterialExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterialValue',
            fields=[
                ('referencematerialvalueid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='ReferenceMaterialValueID')),
                ('referencematerialvalue', models.FloatField(db_column='ReferenceMaterialValue')),
                ('referencematerialaccuracy',
                 models.FloatField(null=True, db_column='ReferenceMaterialAccuracy', blank=True)),
            ],
            options={
                'db_table': 'ODM2DataQuality].[ReferenceMaterialValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedAction',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2Core].[RelatedActions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedAnnotation',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2Provenance].[RelatedAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedCitation',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.IntegerField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2Provenance].[RelatedCitations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedDataset',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('versioncode', models.TextField(db_column='VersionCode', blank=True)),
            ],
            options={
                'db_table': 'ODM2Provenance].[RelatedDatasets',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedEquipment',
            fields=[
                ('relationid', models.AutoField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('relationshipstartdatetime', models.DateTimeField(db_column='RelationshipStartDateTime')),
                ('relationshipstartdatetimeutcoffset',
                 models.IntegerField(db_column='RelationshipStartDateTimeUTCOffset')),
                ('relationshipenddatetime',
                 models.DateTimeField(null=True, db_column='RelationshipEndDateTime', blank=True)),
                ('relationshipenddatetimeutcoffset',
                 models.IntegerField(null=True, db_column='RelationshipEndDateTimeUTCOffset', blank=True)),
            ],
            options={
                'db_table': 'ODM2Equipment].[RelatedEquipment',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedFeatures',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[RelatedFeatures',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('relatedid', models.IntegerField(serialize=False, primary_key=True, db_column='RelatedID')),
                ('relationshiptypecv', models.CharField(max_length=1, db_column='RelationshipTypeCV')),
                ('relatedmodelid', models.BigIntegerField(db_column='RelatedModelID')),
            ],
            options={
                'db_table': 'ODM2Simulation].[RelatedModels',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedResult',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('versioncode', models.TextField(db_column='VersionCode', blank=True)),
                ('relatedresultsequencenumber',
                 models.IntegerField(null=True, db_column='RelatedResultSequenceNumber', blank=True)),
            ],
            options={
                'db_table': 'ODM2Provenance].[RelatedResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('resultid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ResultID')),
                ('resultuuid', models.TextField(db_column='ResultUUID')),
                ('resultdatetime', models.DateTimeField(null=True, db_column='ResultDateTime', blank=True)),
                ('resultdatetimeutcoffset',
                 models.BigIntegerField(null=True, db_column='ResultDateTimeUTCOffset', blank=True)),
                ('validdatetime', models.DateTimeField(null=True, db_column='ValidDateTime', blank=True)),
                ('validdatetimeutcoffset',
                 models.BigIntegerField(null=True, db_column='ValidDateTimeUTCOffset', blank=True)),
                ('statuscv', models.TextField(db_column='StatusCV', blank=True)),
                ('sampledmediumcv', models.TextField(db_column='SampledMediumCV')),
                ('valuecount', models.IntegerField(db_column='ValueCount')),
            ],
            options={
                'db_table': 'ODM2Core].[Results',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('intendedzspacing', models.FloatField(null=True, db_column='IntendedZSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[ProfileResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointCoverageResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedxspacing', models.FloatField(null=True, db_column='IntendedXSpacing', blank=True)),
                ('intendedyspacing', models.FloatField(null=True, db_column='IntendedYSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
                ('timeaggregationintervalunitsid', models.IntegerField(db_column='TimeAggregationIntervalUnitsID')),
            ],
            options={
                'db_table': 'ODM2Results].[PointCoverageResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[MeasurementResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoricalResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('xlocationunitsid', models.IntegerField(null=True, db_column='XLocationUnitsID', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('ylocationunitsid', models.IntegerField(null=True, db_column='YLocationUnitsID', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('zlocationunitsid', models.IntegerField(null=True, db_column='ZLocationUnitsID', blank=True)),
                ('qualitycodecv', models.BigIntegerField(db_column='QualityCodeCV')),
            ],
            options={
                'db_table': 'ODM2Results].[CategoricalResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('begindatetime', models.DateTimeField(db_column='BeginDateTime')),
                ('enddatetime', models.DateTimeField(db_column='EndDateTime')),
            ],
            options={
                'db_table': 'ODM2Annotations].[ResultAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultDerivationEquation',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
            ],
            options={
                'db_table': 'ODM2Provenance].[ResultDerivationEquations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[ResultExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultNormalizationValue',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
            ],
            options={
                'db_table': 'ODM2DataQuality].[ResultNormalizationValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultsDataQuality',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2DataQuality].[ResultsDataQuality',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultTypeCV',
            fields=[
                ('resulttypecv', models.TextField(serialize=False, primary_key=True, db_column='ResultTypeCV')),
                ('resulttypecategory', models.TextField(db_column='ResultTypeCategory')),
                ('datatype', models.TextField(db_column='DataType')),
                ('resulttypedefinition', models.TextField(db_column='ResultTypeDefinition')),
                ('fixeddimensions', models.TextField(db_column='FixedDimensions')),
                ('varyingdimensions', models.TextField(db_column='VaryingDimensions')),
                ('spacemeasurementframework', models.TextField(db_column='SpaceMeasurementFramework')),
                ('timemeasurementframework', models.TextField(db_column='TimeMeasurementFramework')),
                ('variablemeasurementframework', models.TextField(db_column='VariableMeasurementFramework')),
            ],
            options={
                'db_table': 'ODM2Results].[ResultTypeCV',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeature',
            fields=[
                ('samplingfeatureid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='SamplingFeatureID')),
                ('samplingfeaturetypecv', models.TextField(db_column='SamplingFeatureTypeCV')),
                ('samplingfeaturecode', models.TextField(db_column='SamplingFeatureCode')),
                ('samplingfeaturename', models.TextField(db_column='SamplingFeatureName', blank=True)),
                ('samplingfeaturedescription', models.TextField(db_column='SamplingFeatureDescription', blank=True)),
                ('samplingfeaturegeotypecv', models.TextField(db_column='SamplingFeatureGeotypeCV', blank=True)),
                ('elevation_m', models.FloatField(null=True, db_column='Elevation_m', blank=True)),
                ('elevationdatumcv', models.TextField(db_column='ElevationDatumCV', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[SamplingFeatures',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeatureAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[SamplingFeatureAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeatureExtensionPropertyValue',
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
        migrations.CreateModel(
            name='SamplingFeatureExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('samplingfeatureexternalidentifier', models.TextField(db_column='SamplingFeatureExternalIdentifier')),
                ('samplingfeatureexternalidentiferuri',
                 models.TextField(db_column='SamplingFeatureExternalIdentiferURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[SamplingFeatureExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('intendedxspacing', models.FloatField(null=True, db_column='IntendedXSpacing', blank=True)),
                ('intendedzspacing', models.FloatField(null=True, db_column='IntendedZSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[SectionResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.BigIntegerField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.BigIntegerField(db_column='ValueDateTimeUTCOffset')),
                ('xlocation', models.FloatField(db_column='XLocation')),
                ('xaggregationinterval', models.FloatField(db_column='XAggregationInterval')),
                ('zlocation', models.BigIntegerField(db_column='ZLocation')),
                ('zaggregationinterval', models.FloatField(db_column='ZAggregationInterval')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[SectionResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[SectionResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('simulationid', models.IntegerField(serialize=False, primary_key=True, db_column='SimulationID')),
                ('actionid', models.BigIntegerField(db_column='ActionID')),
                ('simulationname', models.CharField(max_length=255, db_column='SimulationName')),
                ('simulationdescription',
                 models.CharField(max_length=500, db_column='SimulationDescription', blank=True)),
                ('simulationstartdatetime', models.DateTimeField(db_column='SimulationStartDateTime')),
                ('simulationstartdatetimeutcoffset', models.IntegerField(db_column='SimulationStartDateTimeUTCOffset')),
                ('simulationenddatetime', models.DateTimeField(db_column='SimulationEndDateTime')),
                ('simulationenddatetimeutcoffset', models.IntegerField(db_column='SimulationEndDateTimeUTCOffset')),
                ('timestepvalue', models.FloatField(db_column='TimeStepValue')),
                ('timestepunitsid', models.BigIntegerField(db_column='TimeStepUnitsID')),
                ('inputdatasetid', models.BigIntegerField(null=True, db_column='InputDataSetID', blank=True)),
            ],
            options={
                'db_table': 'ODM2Simulation].[Simulations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('samplingfeatureid',
                 models.ForeignKey(primary_key=True, db_column='SamplingFeatureID', serialize=False,
                                   to='sensordatainterface.SamplingFeature')),
                ('sitetypecv', models.TextField(db_column='SiteTypeCV')),
                ('latitude', models.FloatField(db_column='Latitude')),
                ('longitude', models.FloatField(db_column='Longitude')),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[Sites',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialOffsets',
            fields=[
                (
                'spatialoffsetid', models.IntegerField(serialize=False, primary_key=True, db_column='SpatialOffsetID')),
                ('spatialoffsettypecv', models.TextField(db_column='SpatialOffsetTypeCV')),
                ('offset1value', models.FloatField(db_column='Offset1Value')),
                ('offset1unitid', models.IntegerField(db_column='Offset1UnitID')),
                ('offset2value', models.FloatField(null=True, db_column='Offset2Value', blank=True)),
                ('offset2unitid', models.IntegerField(null=True, db_column='Offset2UnitID', blank=True)),
                ('offset3value', models.FloatField(null=True, db_column='Offset3Value', blank=True)),
                ('offset3unitid', models.IntegerField(null=True, db_column='Offset3UnitID', blank=True)),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[SpatialOffsets',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialReference',
            fields=[
                ('spatialreferenceid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='SpatialReferenceID')),
                ('srscode', models.TextField(db_column='SRSCode', blank=True)),
                ('srsname', models.TextField(db_column='SRSName')),
                ('srsdescription', models.TextField(db_column='SRSDescription', blank=True)),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[SpatialReferences',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialReferenceExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                (
                'spatialreferenceexternalidentifier', models.TextField(db_column='SpatialReferenceExternalIdentifier')),
                ('spatialreferenceexternalidentifieruri',
                 models.TextField(db_column='SpatialReferenceExternalIdentifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[SpatialReferenceExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecimenBatchPostion',
            fields=[
                ('featureactionid', models.ForeignKey(primary_key=True, db_column='FeatureActionID', serialize=False,
                                                      to='sensordatainterface.FeatureAction')),
                ('batchpositionnumber', models.IntegerField(db_column='BatchPositionNumber')),
                ('batchpositionlabel', models.TextField(db_column='BatchPositionLabel', blank=True)),
            ],
            options={
                'db_table': 'ODM2LabAnalyses].[SpecimenBatchPostions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specimens',
            fields=[
                ('samplingfeatureid',
                 models.ForeignKey(primary_key=True, db_column='SamplingFeatureID', serialize=False,
                                   to='sensordatainterface.SamplingFeature')),
                ('specimentypecv', models.TextField(db_column='SpecimenTypeCV')),
                ('specimenmediumcv', models.TextField(db_column='SpecimenMediumCV')),
                ('isfieldspecimen', models.BooleanField(db_column='IsFieldSpecimen')),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[Specimens',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecimenTaxonomicClassifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('citationid', models.IntegerField(null=True, db_column='CitationID', blank=True)),
            ],
            options={
                'db_table': 'ODM2SamplingFeatures].[SpecimenTaxonomicClassifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpectraResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedwavelengthspacing',
                 models.FloatField(null=True, db_column='IntendedWavelengthSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[SpectraResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpectraResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
                ('excitationwavelength', models.FloatField(db_column='ExcitationWavelength')),
                ('emissionwavelength', models.FloatField(db_column='EmissionWavelength')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[SpectraResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpectraResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[SpectraResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(serialize=False, primary_key=True)),
                ('version', models.IntegerField(null=True, blank=True)),
                ('definition', models.BinaryField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifier',
            fields=[
                ('taxonomicclassifierid',
                 models.IntegerField(serialize=False, primary_key=True, db_column='TaxonomicClassifierID')),
                ('taxonomicclassifiertypecv', models.TextField(db_column='TaxonomicClassifierTypeCV')),
                ('taxonomicclassifiername', models.TextField(db_column='TaxonomicClassifierName')),
                ('taxonomicclassifiercommonname',
                 models.TextField(db_column='TaxonomicClassifierCommonName', blank=True)),
                ('taxonomicclassifierdescription',
                 models.TextField(db_column='TaxonomicClassifierDescription', blank=True)),
            ],
            options={
                'db_table': 'ODM2Core].[TaxonomicClassifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifierExternalIdentifier',
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
        migrations.CreateModel(
            name='TimeSeriesResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[TimeSeriesResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSeriesResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[TimeSeriesResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSeriesResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[TimeSeriesResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrajectoryResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('intendedtrajectoryspacing',
                 models.FloatField(null=True, db_column='IntendedTrajectorySpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[TrajectoryResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrajectoryResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.IntegerField(db_column='ValueDateTimeUTCOffset')),
                ('xlocation', models.FloatField(db_column='XLocation')),
                ('ylocation', models.FloatField(db_column='YLocation')),
                ('zlocation', models.FloatField(db_column='ZLocation')),
                ('trajectorydistance', models.FloatField(db_column='TrajectoryDistance')),
                ('trajectorydistanceaggregationinterval',
                 models.FloatField(db_column='TrajectoryDistanceAggregationInterval')),
                ('trajectorydistanceunitsid', models.IntegerField(db_column='TrajectoryDistanceUnitsID')),
                ('censorcode', models.TextField(db_column='CensorCode')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'ODM2Results].[TrajectoryResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrajectoryResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[TrajectoryResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransectResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False,
                                               to='sensordatainterface.Result')),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedtransectspacing',
                 models.FloatField(null=True, db_column='IntendedTransectSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ODM2Results].[TransectResults',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransectResultValue',
            fields=[
                ('valueid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ValueID')),
                ('datavalue', models.FloatField(db_column='DataValue')),
                ('valuedatetime', models.DateTimeField(db_column='ValueDateTime')),
                ('valuedatetimeutcoffset', models.DateTimeField(db_column='ValueDateTimeUTCOffset')),
                ('xlocation', models.FloatField(db_column='XLocation')),
                ('xlocationunitsid', models.IntegerField(db_column='XLocationUnitsID')),
                ('ylocation', models.FloatField(db_column='YLocation')),
                ('ylocationunitsid', models.IntegerField(db_column='YLocationUnitsID')),
                ('transectdistance', models.FloatField(db_column='TransectDistance')),
                ('transectdistanceaggregationinterval',
                 models.FloatField(db_column='TransectDistanceAggregationInterval')),
                ('transectdistanceunitsid', models.IntegerField(db_column='TransectDistanceUnitsID')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
                ('timeaggregationintervalunitsid', models.IntegerField(db_column='TimeAggregationIntervalUnitsID')),
            ],
            options={
                'db_table': 'ODM2Results].[TransectResultValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransectResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ODM2Annotations].[TransectResultValueAnnotations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('unitsid', models.IntegerField(serialize=False, primary_key=True, db_column='UnitsID')),
                ('unitstypecv', models.TextField(db_column='UnitsTypeCV')),
                ('unitsabbreviation', models.TextField(db_column='UnitsAbbreviation')),
                ('unitsname', models.TextField(db_column='UnitsName')),
            ],
            options={
                'db_table': 'ODM2Core].[Units',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('variableid', models.IntegerField(serialize=False, primary_key=True, db_column='VariableID')),
                ('variabletypecv', models.TextField(db_column='VariableTypeCV')),
                ('variablecode', models.TextField(db_column='VariableCode')),
                ('variablenamecv', models.TextField(db_column='VariableNameCV')),
                ('variabledefinition', models.TextField(db_column='VariableDefinition', blank=True)),
                ('speciationcv', models.TextField(db_column='SpeciationCV', blank=True)),
                ('nodatavalue', models.FloatField(db_column='NoDataValue')),
            ],
            options={
                'db_table': 'ODM2Core].[Variables',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariableExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
            ],
            options={
                'db_table': 'ODM2ExtensionProperties].[VariableExtensionPropertyValues',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariableExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('variableexternalidentifer', models.TextField(db_column='VariableExternalIdentifer')),
                ('variableexternalidentifieruri',
                 models.TextField(db_column='VariableExternalIdentifierURI', blank=True)),
            ],
            options={
                'db_table': 'ODM2ExternalIdentifiers].[VariableExternalIdentifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
