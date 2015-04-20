# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#NOTE: Schemas were removed to make tests possible. pyodbc doesn't currently support the creation of schemas
#in SQL Server.
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
                'db_table': 'Actions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ActionAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionBy',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('isactionlead', models.BooleanField(default=None, db_column='IsActionLead')),
                ('roledescription', models.TextField(db_column='RoleDescription', blank=True)),
            ],
            options={
                'db_table': 'ActionBy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionDirective',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'ActionDirectives',
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
                'db_table': 'ActionExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('affiliationid', models.IntegerField(serialize=False, primary_key=True, db_column='AffiliationID')),
                ('isprimaryorganizationcontact', models.NullBooleanField(default=None, db_column='IsPrimaryOrganizationContact')),
                ('affiliationstartdate', models.DateField(db_column='AffiliationStartDate')),
                ('affiliationenddate', models.DateField(null=True, db_column='AffiliationEndDate', blank=True)),
                ('primaryphone', models.TextField(db_column='PrimaryPhone', blank=True)),
                ('primaryemail', models.TextField(db_column='PrimaryEmail')),
                ('primaryaddress', models.TextField(db_column='PrimaryAddress', blank=True)),
                ('personlink', models.TextField(db_column='PersonLink', blank=True)),
            ],
            options={
                'db_table': 'Affiliations',
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
                'db_table': 'Annotations',
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
                'db_table': 'AuthorLists',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationAction',
            fields=[
                ('actionid', models.ForeignKey(related_name='calibrationaction', primary_key=True, db_column='ActionID', serialize=False, to='sensordatainterface.Action')),
                ('calibrationcheckvalue', models.FloatField(null=True, db_column='CalibrationCheckValue', blank=True)),
                ('calibrationequation', models.TextField(db_column='CalibrationEquation', blank=True)),
            ],
            options={
                'db_table': 'CalibrationActions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationReferenceEquipment',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('actionid', models.ForeignKey(related_name='calibrationreferenceequipment', db_column='ActionID', to='sensordatainterface.CalibrationAction')),
            ],
            options={
                'db_table': 'CalibrationReferenceEquipment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CalibrationStandard',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('actionid', models.ForeignKey(related_name='calibrationstandard', db_column='ActionID', to='sensordatainterface.CalibrationAction')),
            ],
            options={
                'db_table': 'CalibrationStandards',
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
                'db_table': 'CategoricalResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoricalResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.CategoricalResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'CategoricalResultValueAnnotations',
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
                'db_table': 'Citations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CitationExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
                ('citationid', models.ForeignKey(to='sensordatainterface.Citation', db_column='CitationID')),
            ],
            options={
                'db_table': 'CitationExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CitationExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('citationexternalidentifer', models.TextField(db_column='CitationExternalIdentifer')),
                ('citationexternalidentiferuri', models.TextField(db_column='CitationExternalIdentiferURI', blank=True)),
                ('citationid', models.ForeignKey(to='sensordatainterface.Citation', db_column='CitationID')),
            ],
            options={
                'db_table': 'CitationExternalIdentifiers',
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
                'db_table': 'CVTerms',
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
                'db_table': 'DataLoggerFiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataloggerFileColumn',
            fields=[
                ('dataloggerfilecolumnid', models.AutoField(serialize=False, primary_key=True, db_column='DataloggerFileColumnID')),
                ('columnlabel', models.TextField(db_column='ColumnLabel')),
                ('columndescription', models.TextField(db_column='ColumnDescription', blank=True)),
                ('measurementequation', models.TextField(db_column='MeasurementEquation', blank=True)),
                ('scaninterval', models.FloatField(null=True, db_column='ScanInterval', blank=True)),
                ('recordinginterval', models.FloatField(null=True, db_column='RecordingInterval', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV', blank=True)),
                ('dataloggerfileid', models.ForeignKey(related_name='dataloggerfilecolumn', db_column='DataLoggerFileID', to='sensordatainterface.DataloggerFile')),
            ],
            options={
                'db_table': 'DataloggerFileColumns',
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
                ('affiliationid', models.ForeignKey(to='sensordatainterface.Affiliation', db_column='AffiliationID')),
            ],
            options={
                'db_table': 'DataloggerProgramFiles',
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
                'db_table': 'DataQuality',
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
                'db_table': 'DataSets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatasetCitation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('citationid', models.ForeignKey(to='sensordatainterface.Citation', db_column='CitationID')),
                ('datasetid', models.ForeignKey(to='sensordatainterface.Dataset', db_column='DataSetID')),
            ],
            options={
                'db_table': 'DataSetCitations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DatasetsResult',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('datasetid', models.ForeignKey(to='sensordatainterface.Dataset', db_column='DataSetID')),
            ],
            options={
                'db_table': 'DataSetsResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DerivationEquation',
            fields=[
                ('derivationequationid', models.IntegerField(serialize=False, primary_key=True, db_column='DerivationEquationID')),
                ('derivationequation', models.TextField(db_column='DerivationEquation')),
            ],
            options={
                'db_table': 'DerivationEquations',
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
                'db_table': 'Directives',
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
                ('equipmentpurchaseordernumber', models.TextField(db_column='EquipmentPurchaseOrderNumber', blank=True)),
                ('equipmentdescription', models.TextField(db_column='EquipmentDescription', blank=True)),
                ('equipmentdocumentationlink', models.TextField(db_column='EquipmentDocumentationLink', blank=True)),
            ],
            options={
                'db_table': 'Equipment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('equipmentid', models.ForeignKey(to='sensordatainterface.Equipment', db_column='EquipmentID')),
            ],
            options={
                'db_table': 'EquipmentAnnotations',
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
                ('isinstrument', models.BooleanField(default=None, db_column='IsInstrument')),
                ('modelspecificationsfilelink', models.TextField(db_column='ModelSpecificationsFileLink', blank=True)),
                ('modellink', models.TextField(db_column='ModelLink', blank=True)),
            ],
            options={
                'db_table': 'EquipmentModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentUsed',
            fields=[
                ('bridgeid', models.AutoField(serialize=False, primary_key=True, db_column='BridgeID')),
            ],
            options={
                'db_table': 'EquipmentUsed',
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
                'db_table': 'ExtensionProperties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExternalIdentifierSystem',
            fields=[
                ('externalidentifiersystemid', models.IntegerField(serialize=False, primary_key=True, db_column='ExternalIdentifierSystemID')),
                ('externalidentifiersystemname', models.TextField(db_column='ExternalIdentifierSystemName')),
                ('externalidentifiersystemdescription', models.TextField(db_column='ExternalIdentifierSystemDescription', blank=True)),
                ('externalidentifiersystemurl', models.TextField(db_column='ExternalIdentifierSystemURL', blank=True)),
            ],
            options={
                'db_table': 'ExternalIdentifierSystems',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureAction',
            fields=[
                ('featureactionid', models.IntegerField(serialize=False, primary_key=True, db_column='FeatureActionID')),
            ],
            options={
                'db_table': 'FeatureActions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstrumentOutputVariable',
            fields=[
                ('instrumentoutputvariableid', models.AutoField(serialize=False, primary_key=True, db_column='InstrumentOutputVariableID')),
                ('instrumentresolution', models.TextField(db_column='InstrumentResolution', blank=True)),
                ('instrumentaccuracy', models.TextField(db_column='InstrumentAccuracy', blank=True)),
            ],
            options={
                'db_table': 'InstrumentOutputVariables',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MaintenanceAction',
            fields=[
                ('actionid', models.ForeignKey(primary_key=True, db_column='ActionID', serialize=False, to='sensordatainterface.Action')),
                ('isfactoryservice', models.BooleanField(default=None, db_column='IsFactoryService')),
                ('maintenancecode', models.TextField(db_column='MaintenanceCode', blank=True)),
                ('maintenancereason', models.TextField(db_column='MaintenanceReason', blank=True)),
            ],
            options={
                'db_table': 'MaintenanceActions',
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
                'db_table': 'MeasurementResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.MeasurementResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'MeasurementResultValueAnnotations',
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
                'db_table': 'Methods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('methodid', models.ForeignKey(to='sensordatainterface.Method', db_column='MethodID')),
            ],
            options={
                'db_table': 'MethodAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodCitation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('citationid', models.ForeignKey(to='sensordatainterface.Citation', db_column='CitationID')),
                ('methodid', models.ForeignKey(to='sensordatainterface.Method', db_column='MethodID')),
            ],
            options={
                'db_table': 'MethodCitations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
                ('methodid', models.ForeignKey(to='sensordatainterface.Method', db_column='MethodID')),
                ('propertyid', models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID')),
            ],
            options={
                'db_table': 'MethodExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MethodExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('methodexternalidentifier', models.TextField(db_column='MethodExternalIdentifier')),
                ('methodexternalidentifieruri', models.TextField(db_column='MethodExternalIdentifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('methodid', models.ForeignKey(to='sensordatainterface.Method', db_column='MethodID')),
            ],
            options={
                'db_table': 'MethodExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelAffiliation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('isprimary', models.BooleanField(default=None, db_column='IsPrimary')),
                ('roledescription', models.TextField(db_column='RoleDescription', blank=True)),
                ('affiliationid', models.ForeignKey(to='sensordatainterface.Affiliation', db_column='AffiliationID')),
            ],
            options={
                'db_table': 'ModelAffiliations',
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
                'db_table': 'Models',
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
                ('parentorganizationid', models.ForeignKey(db_column='ParentOrganizationID', blank=True, to='sensordatainterface.Organization', null=True)),
            ],
            options={
                'db_table': 'Organizations',
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
                'db_table': 'People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('personexternalidentifier', models.TextField(db_column='PersonExternalIdentifier')),
                ('personexternalidenifieruri', models.TextField(db_column='PersonExternalIdenifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('personid', models.ForeignKey(to='sensordatainterface.People', db_column='PersonID')),
            ],
            options={
                'db_table': 'PersonExternalIdentifiers',
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
                'db_table': 'PointCoverageResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointCoverageResultValueAnnotation',
            fields=[
                ('bridgeid', models.BigIntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.PointCoverageResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'PointCoverageResultValueAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProcessingLevel',
            fields=[
                ('processinglevelid', models.IntegerField(serialize=False, primary_key=True, db_column='ProcessingLevelID')),
                ('processinglevelcode', models.TextField(db_column='ProcessingLevelCode')),
                ('definition', models.TextField(db_column='Definition', blank=True)),
                ('explanation', models.TextField(db_column='Explanation', blank=True)),
            ],
            options={
                'db_table': 'ProcessingLevels',
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
                'db_table': 'ProfileResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.ProfileResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'ProfileResultValueAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterial',
            fields=[
                ('referencematerialid', models.IntegerField(serialize=False, primary_key=True, db_column='ReferenceMaterialID')),
                ('referencematerialmediumcv', models.TextField(db_column='ReferenceMaterialMediumCV')),
                ('referencematerialcode', models.TextField(db_column='ReferenceMaterialCode')),
                ('referencemateriallotcode', models.TextField(db_column='ReferenceMaterialLotCode', blank=True)),
                ('referencematerialpurchasedate', models.DateTimeField(null=True, db_column='ReferenceMaterialPurchaseDate', blank=True)),
                ('referencematerialexpirationdate', models.DateTimeField(null=True, db_column='ReferenceMaterialExpirationDate', blank=True)),
                ('referencematerialcertificatelink', models.TextField(db_column='ReferenceMaterialCertificateLink', blank=True)),
                ('referencematerialorganizationid', models.ForeignKey(to='sensordatainterface.Organization', db_column='ReferenceMaterialOrganizationID')),
            ],
            options={
                'db_table': 'ReferenceMaterials',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterialExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('referencematerialexternalidentifier', models.TextField(db_column='ReferenceMaterialExternalIdentifier')),
                ('referencematerialexternalidentifieruri', models.TextField(db_column='ReferenceMaterialExternalIdentifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('referencematerialid', models.ForeignKey(to='sensordatainterface.ReferenceMaterial', db_column='ReferenceMaterialID')),
            ],
            options={
                'db_table': 'ReferenceMaterialExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceMaterialValue',
            fields=[
                ('referencematerialvalueid', models.IntegerField(serialize=False, primary_key=True, db_column='ReferenceMaterialValueID')),
                ('referencematerialvalue', models.FloatField(db_column='ReferenceMaterialValue')),
                ('referencematerialaccuracy', models.FloatField(null=True, db_column='ReferenceMaterialAccuracy', blank=True)),
                ('citationid', models.ForeignKey(db_column='CitationID', blank=True, to='sensordatainterface.Citation', null=True)),
                ('referencematerialid', models.ForeignKey(related_name='referencematerialvalue', db_column='ReferenceMaterialID', to='sensordatainterface.ReferenceMaterial')),
            ],
            options={
                'db_table': 'ReferenceMaterialValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedAction',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('actionid', models.ForeignKey(related_name='relatedaction', db_column='ActionID', to='sensordatainterface.Action')),
                ('relatedactionid', models.ForeignKey(related_name='parent_relatedaction', db_column='RelatedActionID', to='sensordatainterface.Action')),
            ],
            options={
                'db_table': 'RelatedActions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedAnnotation',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('annotationid', models.ForeignKey(related_name='relatedannonations_annotationid', db_column='AnnotationID', to='sensordatainterface.Annotation')),
                ('relatedannotationid', models.ForeignKey(related_name='relatedannotation_relatedannontationid', db_column='RelatedAnnotationID', to='sensordatainterface.Annotation')),
            ],
            options={
                'db_table': 'RelatedAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedCitation',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.IntegerField(db_column='RelationshipTypeCV')),
                ('citationid', models.ForeignKey(related_name='relatedcitations_citationid', db_column='CitationID', to='sensordatainterface.Citation')),
                ('relatedcitationid', models.ForeignKey(related_name='relatedcitations_relatedcitationid', db_column='RelatedCitationID', to='sensordatainterface.Citation')),
            ],
            options={
                'db_table': 'RelatedCitations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedDataset',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('versioncode', models.TextField(db_column='VersionCode', blank=True)),
                ('datasetid', models.ForeignKey(related_name='relateddatasets_datasetid', db_column='DataSetID', to='sensordatainterface.Dataset')),
                ('relateddatasetid', models.ForeignKey(related_name='relateddatasets_relateddatasetid', db_column='RelatedDatasetID', to='sensordatainterface.Dataset')),
            ],
            options={
                'db_table': 'RelatedDatasets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedEquipment',
            fields=[
                ('relationid', models.AutoField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('relationshipstartdatetime', models.DateTimeField(db_column='RelationshipStartDateTime')),
                ('relationshipstartdatetimeutcoffset', models.IntegerField(db_column='RelationshipStartDateTimeUTCOffset')),
                ('relationshipenddatetime', models.DateTimeField(null=True, db_column='RelationshipEndDateTime', blank=True)),
                ('relationshipenddatetimeutcoffset', models.IntegerField(null=True, db_column='RelationshipEndDateTimeUTCOffset', blank=True)),
                ('equipmentid', models.ForeignKey(related_name='relatedequipment_equipmentid', db_column='EquipmentID', to='sensordatainterface.Equipment')),
                ('relatedequipmentid', models.ForeignKey(related_name='relatedequipment_relatedequipmentid', db_column='RelatedEquipmentID', to='sensordatainterface.Equipment')),
            ],
            options={
                'db_table': 'RelatedEquipment',
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
                'db_table': 'RelatedFeatures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('relatedid', models.IntegerField(serialize=False, primary_key=True, db_column='RelatedID')),
                ('relationshiptypecv', models.CharField(max_length=1, db_column='RelationshipTypeCV')),
                ('relatedmodelid', models.BigIntegerField(db_column='RelatedModelID')),
                ('modelid', models.ForeignKey(to='sensordatainterface.Models', db_column='ModelID')),
            ],
            options={
                'db_table': 'RelatedModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedResult',
            fields=[
                ('relationid', models.IntegerField(serialize=False, primary_key=True, db_column='RelationID')),
                ('relationshiptypecv', models.TextField(db_column='RelationshipTypeCV')),
                ('versioncode', models.TextField(db_column='VersionCode', blank=True)),
                ('relatedresultsequencenumber', models.IntegerField(null=True, db_column='RelatedResultSequenceNumber', blank=True)),
            ],
            options={
                'db_table': 'RelatedResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('resultid', models.BigIntegerField(serialize=False, primary_key=True, db_column='ResultID')),
                ('resultuuid', models.TextField(db_column='ResultUUID')),
                ('resultdatetime', models.DateTimeField(null=True, db_column='ResultDateTime', blank=True)),
                ('resultdatetimeutcoffset', models.BigIntegerField(null=True, db_column='ResultDateTimeUTCOffset', blank=True)),
                ('validdatetime', models.DateTimeField(null=True, db_column='ValidDateTime', blank=True)),
                ('validdatetimeutcoffset', models.BigIntegerField(null=True, db_column='ValidDateTimeUTCOffset', blank=True)),
                ('statuscv', models.TextField(db_column='StatusCV', blank=True)),
                ('sampledmediumcv', models.TextField(db_column='SampledMediumCV')),
                ('valuecount', models.IntegerField(db_column='ValueCount')),
            ],
            options={
                'db_table': 'Results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('intendedzspacing', models.FloatField(null=True, db_column='IntendedZSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'ProfileResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PointCoverageResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedxspacing', models.FloatField(null=True, db_column='IntendedXSpacing', blank=True)),
                ('intendedyspacing', models.FloatField(null=True, db_column='IntendedYSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
                ('timeaggregationintervalunitsid', models.IntegerField(db_column='TimeAggregationIntervalUnitsID')),
            ],
            options={
                'db_table': 'PointCoverageResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasurementResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
            ],
            options={
                'db_table': 'MeasurementResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoricalResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('xlocationunitsid', models.IntegerField(null=True, db_column='XLocationUnitsID', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('ylocationunitsid', models.IntegerField(null=True, db_column='YLocationUnitsID', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('zlocationunitsid', models.IntegerField(null=True, db_column='ZLocationUnitsID', blank=True)),
                ('qualitycodecv', models.BigIntegerField(db_column='QualityCodeCV')),
            ],
            options={
                'db_table': 'CategoricalResults',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('begindatetime', models.DateTimeField(db_column='BeginDateTime')),
                ('enddatetime', models.DateTimeField(db_column='EndDateTime')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
            ],
            options={
                'db_table': 'ResultAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultDerivationEquation',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('derivationequationid', models.ForeignKey(to='sensordatainterface.DerivationEquation', db_column='DerivationEquationID')),
            ],
            options={
                'db_table': 'ResultDerivationEquations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
                ('propertyid', models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID')),
            ],
            options={
                'db_table': 'ResultExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultNormalizationValue',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('normalizedbyreferencematerialvalueid', models.ForeignKey(to='sensordatainterface.ReferenceMaterialValue', db_column='NormalizedByReferenceMaterialValueID')),
            ],
            options={
                'db_table': 'ResultNormalizationValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultsDataQuality',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('dataqualityid', models.ForeignKey(to='sensordatainterface.DataQuality', db_column='DataQualityID')),
            ],
            options={
                'db_table': 'ResultsDataQuality',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultTypeCV',
            fields=[
                ('resulttypecv', models.TextField(serialize=False, null=False, db_column='ResultTypeCV')),
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
                'db_table': 'ResultTypeCV',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeature',
            fields=[
                ('samplingfeatureid', models.IntegerField(serialize=False, primary_key=True, db_column='SamplingFeatureID')),
                ('samplingfeaturetypecv', models.TextField(db_column='SamplingFeatureTypeCV')),
                ('samplingfeaturecode', models.TextField(db_column='SamplingFeatureCode')),
                ('samplingfeaturename', models.TextField(db_column='SamplingFeatureName', blank=True)),
                ('samplingfeaturedescription', models.TextField(db_column='SamplingFeatureDescription', blank=True)),
                ('samplingfeaturegeotypecv', models.TextField(db_column='SamplingFeatureGeotypeCV', blank=True)),
                ('elevation_m', models.FloatField(null=True, db_column='Elevation_m', blank=True)),
                ('elevationdatumcv', models.TextField(db_column='ElevationDatumCV', blank=True)),
            ],
            options={
                'db_table': 'SamplingFeatures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeatureAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
            ],
            options={
                'db_table': 'SamplingFeatureAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeatureExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('samplingfeatureexternalidentifier', models.TextField(db_column='SamplingFeatureExternalIdentifier')),
                ('samplingfeatureexternalidentiferuri', models.TextField(db_column='SamplingFeatureExternalIdentiferURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
            ],
            options={
                'db_table': 'SamplingFeatureExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamplingFeatureExtPropertyVal',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
                ('propertyid', models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID')),
            ],
            options={
                'db_table': 'SamplingFeatureExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('intendedxspacing', models.FloatField(null=True, db_column='IntendedXSpacing', blank=True)),
                ('intendedzspacing', models.FloatField(null=True, db_column='IntendedZSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'SectionResults',
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
                ('resultid', models.ForeignKey(to='sensordatainterface.SectionResult', db_column='ResultID')),
            ],
            options={
                'db_table': 'SectionResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.SectionResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'SectionResultValueAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('simulationid', models.IntegerField(serialize=False, primary_key=True, db_column='SimulationID')),
                ('actionid', models.BigIntegerField(db_column='ActionID')),
                ('simulationname', models.CharField(max_length=255, db_column='SimulationName')),
                ('simulationdescription', models.CharField(max_length=500, db_column='SimulationDescription', blank=True)),
                ('simulationstartdatetime', models.DateTimeField(db_column='SimulationStartDateTime')),
                ('simulationstartdatetimeutcoffset', models.IntegerField(db_column='SimulationStartDateTimeUTCOffset')),
                ('simulationenddatetime', models.DateTimeField(db_column='SimulationEndDateTime')),
                ('simulationenddatetimeutcoffset', models.IntegerField(db_column='SimulationEndDateTimeUTCOffset')),
                ('timestepvalue', models.FloatField(db_column='TimeStepValue')),
                ('timestepunitsid', models.BigIntegerField(db_column='TimeStepUnitsID')),
                ('inputdatasetid', models.BigIntegerField(null=True, db_column='InputDataSetID', blank=True)),
                ('modelid', models.ForeignKey(to='sensordatainterface.Models', db_column='ModelID')),
            ],
            options={
                'db_table': 'Simulations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('samplingfeatureid', models.ForeignKey(related_name='sites', primary_key=True, db_column='SamplingFeatureID', serialize=False, to='sensordatainterface.SamplingFeature')),
                ('sitetypecv', models.TextField(db_column='SiteTypeCV')),
                ('latitude', models.FloatField(db_column='Latitude')),
                ('longitude', models.FloatField(db_column='Longitude')),
            ],
            options={
                'db_table': 'Sites',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialOffsets',
            fields=[
                ('spatialoffsetid', models.IntegerField(serialize=False, primary_key=True, db_column='SpatialOffsetID')),
                ('spatialoffsettypecv', models.TextField(db_column='SpatialOffsetTypeCV')),
                ('offset1value', models.FloatField(db_column='Offset1Value')),
                ('offset1unitid', models.IntegerField(db_column='Offset1UnitID')),
                ('offset2value', models.FloatField(null=True, db_column='Offset2Value', blank=True)),
                ('offset2unitid', models.IntegerField(null=True, db_column='Offset2UnitID', blank=True)),
                ('offset3value', models.FloatField(null=True, db_column='Offset3Value', blank=True)),
                ('offset3unitid', models.IntegerField(null=True, db_column='Offset3UnitID', blank=True)),
            ],
            options={
                'db_table': 'SpatialOffsets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialReference',
            fields=[
                ('spatialreferenceid', models.IntegerField(serialize=False, primary_key=True, db_column='SpatialReferenceID')),
                ('srscode', models.TextField(db_column='SRSCode', blank=True)),
                ('srsname', models.TextField(db_column='SRSName')),
                ('srsdescription', models.TextField(db_column='SRSDescription', blank=True)),
            ],
            options={
                'db_table': 'SpatialReferences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialReferenceExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('spatialreferenceexternalidentifier', models.TextField(db_column='SpatialReferenceExternalIdentifier')),
                ('spatialreferenceexternalidentifieruri', models.TextField(db_column='SpatialReferenceExternalIdentifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('spatialreferenceid', models.ForeignKey(to='sensordatainterface.SpatialReference', db_column='SpatialReferenceID')),
            ],
            options={
                'db_table': 'SpatialReferenceExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecimenBatchPostion',
            fields=[
                ('featureactionid', models.ForeignKey(primary_key=True, db_column='FeatureActionID', serialize=False, to='sensordatainterface.FeatureAction')),
                ('batchpositionnumber', models.IntegerField(db_column='BatchPositionNumber')),
                ('batchpositionlabel', models.TextField(db_column='BatchPositionLabel', blank=True)),
            ],
            options={
                'db_table': 'SpecimenBatchPostions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specimens',
            fields=[
                ('samplingfeatureid', models.ForeignKey(primary_key=True, db_column='SamplingFeatureID', serialize=False, to='sensordatainterface.SamplingFeature')),
                ('specimentypecv', models.TextField(db_column='SpecimenTypeCV')),
                ('specimenmediumcv', models.TextField(db_column='SpecimenMediumCV')),
                ('isfieldspecimen', models.BooleanField(default=None, db_column='IsFieldSpecimen')),
            ],
            options={
                'db_table': 'Specimens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecimenTaxonomicClassifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('citationid', models.IntegerField(null=True, db_column='CitationID', blank=True)),
                ('samplingfeatureid', models.ForeignKey(to='sensordatainterface.Specimens', db_column='SamplingFeatureID')),
            ],
            options={
                'db_table': 'SpecimenTaxonomicClassifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpectraResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedwavelengthspacing', models.FloatField(null=True, db_column='IntendedWavelengthSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'SpectraResults',
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
                ('resultid', models.ForeignKey(to='sensordatainterface.SpectraResult', db_column='ResultID')),
            ],
            options={
                'db_table': 'SpectraResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpectraResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.SpectraResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'SpectraResultValueAnnotations',
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
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifier',
            fields=[
                ('taxonomicclassifierid', models.IntegerField(serialize=False, primary_key=True, db_column='TaxonomicClassifierID')),
                ('taxonomicclassifiertypecv', models.TextField(db_column='TaxonomicClassifierTypeCV')),
                ('taxonomicclassifiername', models.TextField(db_column='TaxonomicClassifierName')),
                ('taxonomicclassifiercommonname', models.TextField(db_column='TaxonomicClassifierCommonName', blank=True)),
                ('taxonomicclassifierdescription', models.TextField(db_column='TaxonomicClassifierDescription', blank=True)),
                ('parenttaxonomicclassifierid', models.ForeignKey(db_column='ParentTaxonomicClassifierID', blank=True, to='sensordatainterface.TaxonomicClassifier', null=True)),
            ],
            options={
                'db_table': 'TaxonomicClassifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonomicClassifierExtId',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('taxonomicclassifierexternalidentifier', models.TextField(db_column='TaxonomicClassifierExternalIdentifier')),
                ('taxonomicclassifierexternalidentifieruri', models.TextField(db_column='TaxonomicClassifierExternalIdentifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('taxonomicclassifierid', models.ForeignKey(to='sensordatainterface.TaxonomicClassifier', db_column='TaxonomicClassifierID')),
            ],
            options={
                'db_table': 'TaxonomicClassifierExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSeriesResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('xlocation', models.FloatField(null=True, db_column='XLocation', blank=True)),
                ('ylocation', models.FloatField(null=True, db_column='YLocation', blank=True)),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'TimeSeriesResults',
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
                ('resultid', models.ForeignKey(to='sensordatainterface.TimeSeriesResult', db_column='ResultID')),
            ],
            options={
                'db_table': 'TimeSeriesResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeSeriesResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.TimeSeriesResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'TimeSeriesResultValueAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrajectoryResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('intendedtrajectoryspacing', models.FloatField(null=True, db_column='IntendedTrajectorySpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'TrajectoryResults',
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
                ('trajectorydistanceaggregationinterval', models.FloatField(db_column='TrajectoryDistanceAggregationInterval')),
                ('trajectorydistanceunitsid', models.IntegerField(db_column='TrajectoryDistanceUnitsID')),
                ('censorcode', models.TextField(db_column='CensorCode')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
                ('resultid', models.ForeignKey(to='sensordatainterface.TrajectoryResult', db_column='ResultID')),
            ],
            options={
                'db_table': 'TrajectoryResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrajectoryResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.TrajectoryResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'TrajectoryResultValueAnnotations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransectResult',
            fields=[
                ('resultid', models.ForeignKey(primary_key=True, db_column='ResultID', serialize=False, to='sensordatainterface.Result')),
                ('zlocation', models.FloatField(null=True, db_column='ZLocation', blank=True)),
                ('intendedtransectspacing', models.FloatField(null=True, db_column='IntendedTransectSpacing', blank=True)),
                ('intendedtimespacing', models.FloatField(null=True, db_column='IntendedTimeSpacing', blank=True)),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
            ],
            options={
                'db_table': 'TransectResults',
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
                ('transectdistanceaggregationinterval', models.FloatField(db_column='TransectDistanceAggregationInterval')),
                ('transectdistanceunitsid', models.IntegerField(db_column='TransectDistanceUnitsID')),
                ('censorcodecv', models.TextField(db_column='CensorCodeCV')),
                ('qualitycodecv', models.TextField(db_column='QualityCodeCV')),
                ('aggregationstatisticcv', models.TextField(db_column='AggregationStatisticCV')),
                ('timeaggregationinterval', models.FloatField(db_column='TimeAggregationInterval')),
                ('timeaggregationintervalunitsid', models.IntegerField(db_column='TimeAggregationIntervalUnitsID')),
                ('resultid', models.ForeignKey(to='sensordatainterface.TransectResult', db_column='ResultID')),
            ],
            options={
                'db_table': 'TransectResultValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransectResultValueAnnotation',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('annotationid', models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID')),
                ('valueid', models.ForeignKey(to='sensordatainterface.TransectResultValue', db_column='ValueID')),
            ],
            options={
                'db_table': 'TransectResultValueAnnotations',
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
                'db_table': 'Units',
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
                'db_table': 'Variables',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariableExtensionPropertyValue',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('propertyvalue', models.TextField(db_column='PropertyValue')),
                ('propertyid', models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID')),
                ('variableid', models.ForeignKey(to='sensordatainterface.Variable', db_column='VariableID')),
            ],
            options={
                'db_table': 'VariableExtensionPropertyValues',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariableExternalIdentifier',
            fields=[
                ('bridgeid', models.IntegerField(serialize=False, primary_key=True, db_column='BridgeID')),
                ('variableexternalidentifer', models.TextField(db_column='VariableExternalIdentifer')),
                ('variableexternalidentifieruri', models.TextField(db_column='VariableExternalIdentifierURI', blank=True)),
                ('externalidentifiersystemid', models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID')),
                ('variableid', models.ForeignKey(to='sensordatainterface.Variable', db_column='VariableID')),
            ],
            options={
                'db_table': 'VariableExternalIdentifiers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transectresult',
            name='intendedtimespacingunitsid',
            field=models.ForeignKey(related_name='transectresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transectresult',
            name='intendedtransectspacingunitsid',
            field=models.ForeignKey(db_column='IntendedTransectSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transectresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transectresult',
            name='zlocationunitsid',
            field=models.ForeignKey(related_name='transectresults_zlocationunitsid', db_column='ZLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresultvalue',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(related_name='trajectoryresultvalues_timeaggregationintervalunitsid', db_column='TimeAggregationIntervalUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresultvalue',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='trajectoryresultvalues_xlocationunitsid', db_column='XLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresultvalue',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='trajectoryresultvalues_ylocationunitsid', db_column='YLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresultvalue',
            name='zlocationunitsid',
            field=models.ForeignKey(related_name='trajectoryresultvalues_zlocationunitsid', db_column='ZLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresult',
            name='intendedtimespacingunitsid',
            field=models.ForeignKey(related_name='trajectoryresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresult',
            name='intendedtrajectoryspacingunitsid',
            field=models.ForeignKey(related_name='trajectoryresults_intendedtrajectoryspacingunitsid', db_column='IntendedTrajectorySpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trajectoryresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresultvalue',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='TimeAggregationIntervalUnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresult',
            name='intendedtimespacingunitsid',
            field=models.ForeignKey(related_name='timeseriesresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresult',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='timeseriesresults_xlocationunits', db_column='XLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresult',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='timeseriesresults_ylocationunits', db_column='YLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='timeseriesresult',
            name='zlocationunitsid',
            field=models.ForeignKey(related_name='timeseriesresults_zlocationunits', db_column='ZLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresultvalue',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='TimeAggregationIntervalUnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresultvalue',
            name='wavelengthunitsid',
            field=models.ForeignKey(related_name='spectralresultsvalues_wavelengthunitsid', db_column='WavelengthUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresult',
            name='intendedwavelengthspacingunitsid',
            field=models.ForeignKey(related_name='spectralresult_intendedwavelengthspacingunitsid', db_column='IntendedWavelengthSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresult',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='spectralresults_xlocationunitsid', db_column='XLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresult',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='spectralresults_zlocationunitsid', db_column='YLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spectraresult',
            name='zlocationunitsid',
            field=models.ForeignKey(db_column='ZLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='specimentaxonomicclassifier',
            name='taxonomicclassifierid',
            field=models.ForeignKey(to='sensordatainterface.TaxonomicClassifier', db_column='TaxonomicClassifierID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sites',
            name='latlondatumid',
            field=models.ForeignKey(to='sensordatainterface.SpatialReference', db_column='LatLonDatumID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresultvalue',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(related_name='sectionresults_timeaggregationintervalunitsid', db_column='TimeAggregationIntervalUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresultvalue',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='sectionresults_xlocationunitsid', db_column='XLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresultvalue',
            name='zlocationunitsid',
            field=models.ForeignKey(related_name='sectionresults_zlocationunitsid', db_column='ZLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresult',
            name='intendedtimespacingunitsid',
            field=models.ForeignKey(related_name='sectionresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresult',
            name='intendedxspacingunitsid',
            field=models.ForeignKey(related_name='sectionresults_intendedxspacingunitsid', db_column='IntendedXSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresult',
            name='intendedzspacingunitsid',
            field=models.ForeignKey(related_name='sectionresults_intendedzspacingunitsid', db_column='IntendedZSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sectionresult',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='sectionresults_ylocationunitsid', db_column='YLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='samplingfeatureextpropertyval',
            name='samplingfeatureid',
            field=models.ForeignKey(to='sensordatainterface.SamplingFeature', db_column='SamplingFeatureID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='samplingfeatureexternalidentifier',
            name='samplingfeatureid',
            field=models.ForeignKey(to='sensordatainterface.SamplingFeature', db_column='SamplingFeatureID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='samplingfeatureannotation',
            name='samplingfeatureid',
            field=models.ForeignKey(to='sensordatainterface.SamplingFeature', db_column='SamplingFeatureID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultsdataquality',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.Result', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultextensionpropertyvalue',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.Result', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resultannotation',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.Result', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='featureactionid',
            field=models.ForeignKey(to='sensordatainterface.FeatureAction', db_column='FeatureActionID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='processinglevelid',
            field=models.ForeignKey(to='sensordatainterface.ProcessingLevel', db_column='ProcessingLevelID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='resulttypecv',
            field=models.ForeignKey(to='sensordatainterface.ResultTypeCV', db_column='ResultTypeCV'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='taxonomicclassifierid',
            field=models.ForeignKey(db_column='TaxonomicClassifierID', blank=True, to='sensordatainterface.TaxonomicClassifier', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='unitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='UnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='variableid',
            field=models.ForeignKey(to='sensordatainterface.Variable', db_column='VariableID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedresult',
            name='relatedresultid',
            field=models.ForeignKey(related_name='relatedresults_relatedresultid', db_column='RelatedResultID', to='sensordatainterface.Result'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedresult',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.Result', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedfeatures',
            name='relatedfeatureid',
            field=models.ForeignKey(related_name='relatedfeature_relatedfeatureid', db_column='RelatedFeatureID', to='sensordatainterface.SamplingFeature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedfeatures',
            name='samplingfeatureid',
            field=models.ForeignKey(related_name='relatedfeatures_samplingfeatureid', db_column='SamplingFeatureID', to='sensordatainterface.SamplingFeature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relatedfeatures',
            name='spatialoffsetid',
            field=models.ForeignKey(db_column='SpatialOffsetID', blank=True, to='sensordatainterface.SpatialOffsets', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referencematerialvalue',
            name='unitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='UnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referencematerialvalue',
            name='variableid',
            field=models.ForeignKey(to='sensordatainterface.Variable', db_column='VariableID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referencematerial',
            name='samplingfeatureid',
            field=models.ForeignKey(db_column='SamplingFeatureID', blank=True, to='sensordatainterface.SamplingFeature', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresultvalue',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.ProfileResult', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresultvalue',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(related_name='profile_timeaggregationintervalunitsid', db_column='TimeAggregationIntervalUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresultvalue',
            name='zlocationunitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='ZLocationUnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresult',
            name='intendedtimespacingunitsid',
            field=models.ForeignKey(related_name='profile_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresult',
            name='intendedzspacingunitsid',
            field=models.ForeignKey(db_column='IntendedZSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresult',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='profile_xlocationunitsid', db_column='XLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profileresult',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='profile_ylocationunitsid', db_column='YLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresultvalue',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.PointCoverageResult', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresultvalue',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='point_xlocationunitsid', db_column='XLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresultvalue',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='point_ylocationunitsid', db_column='YLocationUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresult',
            name='intendedxspacingunitsid',
            field=models.ForeignKey(related_name='point_intendedxspacingunitsid', db_column='IntendedXSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresult',
            name='intendedyspacingunitsid',
            field=models.ForeignKey(related_name='point_intendedyspacingunitsid', db_column='IntendedYSpacingUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pointcoverageresult',
            name='zlocationunitsid',
            field=models.ForeignKey(db_column='ZLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='modelaffiliation',
            name='modelid',
            field=models.ForeignKey(to='sensordatainterface.Models', db_column='ModelID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='method',
            name='organizationid',
            field=models.ForeignKey(db_column='OrganizationID', blank=True, to='sensordatainterface.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresultvalue',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.MeasurementResult', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='timeaggregationintervalunitsid',
            field=models.ForeignKey(related_name='measurement_timeaggregationintervalunitsid', db_column='TimeAggregationIntervalUnitsID', to='sensordatainterface.Units'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='xlocationunitsid',
            field=models.ForeignKey(related_name='measurement_xlocationunitsid', db_column='XLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='ylocationunitsid',
            field=models.ForeignKey(related_name='measurement_ylocationunitsid', db_column='YLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measurementresult',
            name='zlocationunitsid',
            field=models.ForeignKey(db_column='ZLocationUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrumentoutputvariable',
            name='instrumentmethodid',
            field=models.ForeignKey(to='sensordatainterface.Method', db_column='InstrumentMethodID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrumentoutputvariable',
            name='instrumentrawoutputunitsid',
            field=models.ForeignKey(to='sensordatainterface.Units', db_column='InstrumentRawOutputUnitsID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrumentoutputvariable',
            name='modelid',
            field=models.ForeignKey(related_name='instrumentoutputvariable', db_column='ModelID', to='sensordatainterface.EquipmentModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instrumentoutputvariable',
            name='variableid',
            field=models.ForeignKey(related_name='instrumentoutputvariable', db_column='VariableID', to='sensordatainterface.Variable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureaction',
            name='actionid',
            field=models.ForeignKey(related_name='featureaction', db_column='ActionID', to='sensordatainterface.Action'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureaction',
            name='samplingfeatureid',
            field=models.ForeignKey(related_name='featureaction', db_column='SamplingFeatureID', to='sensordatainterface.SamplingFeature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='externalidentifiersystem',
            name='identifiersystemorganizationid',
            field=models.ForeignKey(to='sensordatainterface.Organization', db_column='IdentifierSystemOrganizationID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extensionproperties',
            name='propertyunitsid',
            field=models.ForeignKey(db_column='PropertyUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipmentused',
            name='actionid',
            field=models.ForeignKey(related_name='equipmentused', db_column='ActionID', to='sensordatainterface.Action'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipmentused',
            name='equipmentid',
            field=models.ForeignKey(related_name='equipmentused', db_column='EquipmentID', to='sensordatainterface.Equipment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipmentmodel',
            name='modelmanufacturerid',
            field=models.ForeignKey(to='sensordatainterface.Organization', db_column='ModelManufacturerID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipmentmodelid',
            field=models.ForeignKey(related_name='equipment', db_column='EquipmentModelID', to='sensordatainterface.EquipmentModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipmentownerid',
            field=models.ForeignKey(to='sensordatainterface.People', db_column='EquipmentOwnerID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipmentvendorid',
            field=models.ForeignKey(related_name='equipment', db_column='EquipmentVendorID', to='sensordatainterface.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datasetsresult',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.Result', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataquality',
            name='dataqualityvalueunitsid',
            field=models.ForeignKey(db_column='DataQualityValueUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataloggerfilecolumn',
            name='instrumentoutputvariableid',
            field=models.ForeignKey(related_name='dataloggerfilecolumn', db_column='InstrumentOutputVariableID', to='sensordatainterface.InstrumentOutputVariable'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataloggerfilecolumn',
            name='recordingintervalunitsid',
            field=models.ForeignKey(related_name='column_recordingintervalunitsid', db_column='RecordingIntervalUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataloggerfilecolumn',
            name='resultid',
            field=models.ForeignKey(db_column='ResultID', blank=True, to='sensordatainterface.Result', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataloggerfilecolumn',
            name='scanintervalunitsid',
            field=models.ForeignKey(db_column='ScanIntervalUnitsID', blank=True, to='sensordatainterface.Units', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataloggerfile',
            name='programid',
            field=models.ForeignKey(to='sensordatainterface.DataloggerProgramFile', db_column='ProgramID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citationexternalidentifier',
            name='externalidentifiersystemid',
            field=models.ForeignKey(to='sensordatainterface.ExternalIdentifierSystem', db_column='ExternalIdentifierSystemID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='citationextensionpropertyvalue',
            name='propertyid',
            field=models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoricalresultvalue',
            name='resultid',
            field=models.ForeignKey(to='sensordatainterface.CategoricalResult', db_column='ResultID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoricalresult',
            name='spatialreferenceid',
            field=models.ForeignKey(db_column='SpatialReferenceID', blank=True, to='sensordatainterface.SpatialReference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calibrationstandard',
            name='referencematerialid',
            field=models.ForeignKey(to='sensordatainterface.ReferenceMaterial', db_column='ReferenceMaterialID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calibrationreferenceequipment',
            name='equipmentid',
            field=models.ForeignKey(to='sensordatainterface.Equipment', db_column='EquipmentID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calibrationaction',
            name='instrumentoutputvariableid',
            field=models.ForeignKey(to='sensordatainterface.InstrumentOutputVariable', db_column='InstrumentOutputVariableID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorlist',
            name='citationid',
            field=models.ForeignKey(to='sensordatainterface.Citation', db_column='CitationID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorlist',
            name='personid',
            field=models.ForeignKey(to='sensordatainterface.People', db_column='PersonID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotation',
            name='annotatorid',
            field=models.ForeignKey(db_column='AnnotatorID', blank=True, to='sensordatainterface.People', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotation',
            name='citationid',
            field=models.ForeignKey(db_column='CitationID', blank=True, to='sensordatainterface.Citation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='affiliation',
            name='organizationid',
            field=models.ForeignKey(related_name='affiliation', db_column='OrganizationID', blank=True, to='sensordatainterface.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='affiliation',
            name='personid',
            field=models.ForeignKey(related_name='affiliation', db_column='PersonID', to='sensordatainterface.People'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionextensionpropertyvalue',
            name='actionid',
            field=models.ForeignKey(to='sensordatainterface.Action', db_column='ActionID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionextensionpropertyvalue',
            name='propertyid',
            field=models.ForeignKey(to='sensordatainterface.ExtensionProperties', db_column='PropertyID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actiondirective',
            name='actionid',
            field=models.ForeignKey(to='sensordatainterface.Action', db_column='ActionID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actiondirective',
            name='directiveid',
            field=models.ForeignKey(to='sensordatainterface.Directive', db_column='DirectiveID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionby',
            name='actionid',
            field=models.ForeignKey(related_name='actionby', db_column='ActionID', to='sensordatainterface.Action'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionby',
            name='affiliationid',
            field=models.ForeignKey(to='sensordatainterface.Affiliation', db_column='AffiliationID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionannotation',
            name='actionid',
            field=models.ForeignKey(to='sensordatainterface.Action', db_column='ActionID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionannotation',
            name='annotationid',
            field=models.ForeignKey(to='sensordatainterface.Annotation', db_column='AnnotationID'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='methodid',
            field=models.ForeignKey(to='sensordatainterface.Method', db_column='MethodID'),
            preserve_default=True,
        ),
    ]
