from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ActionAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='ActionID')  # Field name made lowercase.
    annotationid = models.ForeignKey('Annotation', db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Annotations].[ActionAnnotations'


class ActionBy(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', related_name="actionby", db_column='ActionID')  # Field name made lowercase.
    affiliationid = models.ForeignKey('Affiliation', db_column='AffiliationID')  # Field name made lowercase.
    isactionlead = models.BooleanField(
        db_column='IsActionLead', default=None)  # , default=False)  # Field name made lowercase. <- How to fix Warnings
    roledescription = models.TextField(db_column='RoleDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Core].[ActionBy'


class ActionDirective(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='ActionID')  # Field name made lowercase.
    directiveid = models.ForeignKey('Directive', db_column='DirectiveID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2LabAnalyses].[ActionDirectives'


class ActionExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='ActionID')  # Field name made lowercase.
    propertyid = models.ForeignKey('ExtensionProperties', db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2ExtensionProperties].[ActionExtensionPropertyValues'


class Action(models.Model):
    actionid = models.IntegerField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.TextField(db_column='ActionTypeCV')  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='MethodID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='BeginDateTimeUTCOffset')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='EndDateTimeUTCOffset', blank=True,
                                               null=True)  # Field name made lowercase.
    actiondescription = models.TextField(db_column='ActionDescription', blank=True)  # Field name made lowercase.
    actionfilelink = models.TextField(db_column='ActionFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Core].[Actions'


class Affiliation(models.Model):
    affiliationid = models.IntegerField(db_column='AffiliationID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('People', related_name='affiliation', db_column='PersonID')  # Field name made lowercase.
    organizationid = models.ForeignKey('Organization', related_name='affiliation', db_column='OrganizationID', blank=True,
                                       null=True)  # Field name made lowercase.
    isprimaryorganizationcontact = models.NullBooleanField(
        db_column='IsPrimaryOrganizationContact', default=None)  # Field name made lowercase.
    affiliationstartdate = models.DateField(db_column='AffiliationStartDate')  # Field name made lowercase.
    affiliationenddate = models.DateField(db_column='AffiliationEndDate', blank=True,
                                          null=True)  # Field name made lowercase.
    primaryphone = models.TextField(db_column='PrimaryPhone', blank=True)  # Field name made lowercase.
    primaryemail = models.TextField(db_column='PrimaryEmail')  # Field name made lowercase.
    primaryaddress = models.TextField(db_column='PrimaryAddress', blank=True)  # Field name made lowercase.
    personlink = models.TextField(db_column='PersonLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Core].[Affiliations'


class Annotation(models.Model):
    annotationid = models.IntegerField(db_column='AnnotationID', primary_key=True)  # Field name made lowercase.
    annotationtypecv = models.TextField(db_column='AnnotationTypeCV')  # Field name made lowercase.
    annotationcode = models.TextField(db_column='AnnotationCode', blank=True)  # Field name made lowercase.
    annotationtext = models.TextField(db_column='AnnotationText')  # Field name made lowercase.
    annotationdatetime = models.DateTimeField(db_column='AnnotationDateTime', blank=True,
                                              null=True)  # Field name made lowercase.
    annotationutcoffset = models.IntegerField(db_column='AnnotationUTCOffset', blank=True,
                                              null=True)  # Field name made lowercase.
    annotationlink = models.TextField(db_column='AnnotationLink', blank=True)  # Field name made lowercase.
    annotatorid = models.ForeignKey('People', db_column='AnnotatorID', blank=True,
                                    null=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='CitationID', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Annotations].[Annotations'


class AuthorList(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='CitationID')  # Field name made lowercase.
    personid = models.ForeignKey('People', db_column='PersonID')  # Field name made lowercase.
    authororder = models.IntegerField(db_column='AuthorOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Provenance].[AuthorLists'


class CvTerm(models.Model):
    termid = models.IntegerField(db_column='TermID', primary_key=True)  # Field name made lowercase.
    term = models.TextField(db_column='Term')  # Field name made lowercase.
    definition = models.TextField(db_column='Definition', blank=True)  # Field name made lowercase.
    odmvocabulary = models.TextField(db_column='ODMVocabulary')  # Field name made lowercase.
    sourcevocabulary = models.TextField(db_column='SourceVocabulary', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2CV].[CVTerms'


class CalibrationAction(models.Model):
    actionid = models.ForeignKey(Action, related_name='calibrationaction', db_column='ActionID', primary_key=True)  # Field name made lowercase.
    calibrationcheckvalue = models.FloatField(db_column='CalibrationCheckValue', blank=True,
                                              null=True)  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariable',
                                                   db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    calibrationequation = models.TextField(db_column='CalibrationEquation', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Equipment].[CalibrationActions'


class CalibrationReferenceEquipment(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(CalibrationAction, related_name='calibrationreferenceequipment', db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipment', db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Equipment].[CalibrationReferenceEquipment'


class CalibrationStandard(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(CalibrationAction, related_name='calibrationstandard', db_column='ActionID')  # Field name made lowercase.
    referencematerialid = models.ForeignKey('ReferenceMaterial',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Equipment].[CalibrationStandards'


class CategoricalResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('CategoricalResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODM2Annotations].[CategoricalResultValueAnnotations'


class CategoricalResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('CategoricalResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[CategoricalResultValues'


class CategoricalResult(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    qualitycodecv = models.BigIntegerField(db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[CategoricalResults'


class CitationExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='CitationID')  # Field name made lowercase.
    propertyid = models.ForeignKey('ExtensionProperties', db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[CitationExtensionPropertyValues'


class CitationExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='CitationID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey('ExternalIdentifierSystem',
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    citationexternalidentifer = models.TextField(db_column='CitationExternalIdentifer')  # Field name made lowercase.
    citationexternalidentiferuri = models.TextField(db_column='CitationExternalIdentiferURI',
                                                    blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[CitationExternalIdentifiers'


class Citation(models.Model):
    citationid = models.IntegerField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher')  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='PublicationYear')  # Field name made lowercase.
    citationlink = models.TextField(db_column='CitationLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[Citations'


class DataloggerFile(models.Model):
    dataloggerfileid = models.AutoField(db_column='DataLoggerFileID', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('DataloggerProgramFile', db_column='ProgramID')  # Field name made lowercase.
    dataloggerfilename = models.TextField(db_column='DataLoggerFileName')  # Field name made lowercase.
    dataloggerfiledescription = models.TextField(db_column='DataLoggerFileDescription',
                                                 blank=True)  # Field name made lowercase.
    dataloggerfilelink = models.TextField(db_column='DataLoggerFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[DataLoggerFiles'


class DataQuality(models.Model):
    dataqualityid = models.IntegerField(db_column='DataQualityID', primary_key=True)  # Field name made lowercase.
    dataqualitytypecv = models.TextField(db_column='DataQualityTypeCV')  # Field name made lowercase.
    dataqualitycode = models.TextField(db_column='DataQualityCode')  # Field name made lowercase.
    dataqualityvalue = models.FloatField(db_column='DataQualityValue', blank=True,
                                         null=True)  # Field name made lowercase.
    dataqualityvalueunitsid = models.ForeignKey('Units', db_column='DataQualityValueUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    dataqualitydescription = models.TextField(db_column='DataQualityDescription',
                                              blank=True)  # Field name made lowercase.
    dataqualitylink = models.TextField(db_column='DataQualityLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2DataQuality].[DataQuality'


class DatasetCitation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey('Dataset', db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[DataSetCitations'


class Dataset(models.Model):
    datasetid = models.IntegerField(db_column='DataSetID', primary_key=True)  # Field name made lowercase.
    datasetuuid = models.TextField(db_column='DataSetUUID')  # Field name made lowercase.
    datasettypecv = models.TextField(db_column='DataSetTypeCV')  # Field name made lowercase.
    datasetcode = models.TextField(db_column='DataSetCode')  # Field name made lowercase.
    datasettitle = models.TextField(db_column='DataSetTitle')  # Field name made lowercase.
    datasetabstract = models.TextField(db_column='DataSetAbstract')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[DataSets'


class DatasetsResult(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Dataset, db_column='DataSetID')  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='ResultID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[DataSetsResults'


class DataloggerFileColumn(models.Model):
    dataloggerfilecolumnid = models.AutoField(db_column='DataloggerFileColumnID',
                                              primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='ResultID', blank=True, null=True)  # Field name made lowercase.
    dataloggerfileid = models.ForeignKey(DataloggerFile, related_name='dataloggerfilecolumn',
                                         db_column='DataLoggerFileID')  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariable', related_name='dataloggerfilecolumn',
                                                   db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    columnlabel = models.TextField(db_column='ColumnLabel')  # Field name made lowercase.
    columndescription = models.TextField(db_column='ColumnDescription', blank=True)  # Field name made lowercase.
    measurementequation = models.TextField(db_column='MeasurementEquation',  blank=True)  # Field name made lowercase.
    scaninterval = models.FloatField(db_column='ScanInterval', blank=True, null=True)  # Field name made lowercase.
    scanintervalunitsid = models.ForeignKey('Units', db_column='ScanIntervalUnitsID', blank=True,
                                            null=True)  # Field name made lowercase.
    recordinginterval = models.FloatField(db_column='RecordingInterval', blank=True,
                                          null=True)  # Field name made lowercase.
    recordingintervalunitsid = models.ForeignKey('Units', related_name='column_recordingintervalunitsid',
                                                 db_column='RecordingIntervalUnitsID', blank=True,
                                                 null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV',
                                              blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[DataloggerFileColumns'


class DataloggerProgramFile(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliation, db_column='AffiliationID')  # Field name made lowercase.
    programname = models.TextField(db_column='ProgramName')  # Field name made lowercase.
    programdescription = models.TextField(db_column='ProgramDescription', blank=True)  # Field name made lowercase.
    programversion = models.TextField(db_column='ProgramVersion', blank=True)  # Field name made lowercase.
    programfilelink = models.TextField(db_column='ProgramFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[DataloggerProgramFiles'


class DerivationEquation(models.Model):
    derivationequationid = models.IntegerField(db_column='DerivationEquationID',
                                               primary_key=True)  # Field name made lowercase.
    derivationequation = models.TextField(db_column='DerivationEquation')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[DerivationEquations'


class Directive(models.Model):
    directiveid = models.IntegerField(db_column='DirectiveID', primary_key=True)  # Field name made lowercase.
    directivetypecv = models.TextField(db_column='DirectiveTypeCV')  # Field name made lowercase.
    directivedescription = models.TextField(db_column='DirectiveDescription')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2LabAnalyses].[Directives'


class Equipment(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  # Field name made lowercase.
    equipmentcode = models.TextField(db_column='EquipmentCode')  # Field name made lowercase.
    equipmentname = models.TextField(db_column='EquipmentName')  # Field name made lowercase.
    equipmenttypecv = models.TextField(db_column='EquipmentTypeCV')  # Field name made lowercase.
    equipmentmodelid = models.ForeignKey('EquipmentModel', related_name='equipment', db_column='EquipmentModelID')  # Field name made lowercase.
    equipmentserialnumber = models.TextField(db_column='EquipmentSerialNumber')  # Field name made lowercase.
    equipmentownerid = models.ForeignKey('People', db_column='EquipmentOwnerID')  # Field name made lowercase.
    equipmentvendorid = models.ForeignKey('Organization', related_name='equipment', db_column='EquipmentVendorID')  # Field name made lowercase.
    equipmentpurchasedate = models.DateTimeField(db_column='EquipmentPurchaseDate')  # Field name made lowercase.
    equipmentpurchaseordernumber = models.TextField(db_column='EquipmentPurchaseOrderNumber',
                                                    blank=True)  # Field name made lowercase.
    equipmentdescription = models.TextField(db_column='EquipmentDescription', blank=True)  # Field name made lowercase.
    equipmentdocumentationlink = models.TextField(db_column='EquipmentDocumentationLink',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[Equipment'


class EquipmentAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, db_column='EquipmentID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[EquipmentAnnotations'


class EquipmentModel(models.Model):
    equipmentmodelid = models.AutoField(db_column='EquipmentModelID', primary_key=True)  # Field name made lowercase.
    modelmanufacturerid = models.ForeignKey('Organization',
                                            db_column='ModelManufacturerID')  # Field name made lowercase.
    modelpartnumber = models.TextField(db_column='ModelPartNumber', blank=True)  # Field name made lowercase.
    modelname = models.TextField(db_column='ModelName')  # Field name made lowercase.
    modeldescription = models.TextField(db_column='ModelDescription', blank=True)  # Field name made lowercase.
    isinstrument = models.BooleanField(db_column='IsInstrument', default=None)  # Field name made lowercase.
    modelspecificationsfilelink = models.TextField(db_column='ModelSpecificationsFileLink',
                                                   blank=True)  # Field name made lowercase.
    modellink = models.TextField(db_column='ModelLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[EquipmentModels'


class EquipmentUsed(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name='equipmentused', db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, related_name='equipmentused', db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[EquipmentUsed'


class ExtensionProperties(models.Model):
    propertyid = models.IntegerField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    propertyname = models.TextField(db_column='PropertyName')  # Field name made lowercase.
    propertydescription = models.TextField(db_column='PropertyDescription', blank=True)  # Field name made lowercase.
    propertydatatypecv = models.TextField(db_column='PropertyDataTypeCV')  # Field name made lowercase.
    propertyunitsid = models.ForeignKey('Units', db_column='PropertyUnitsID', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[ExtensionProperties'


class ExternalIdentifierSystem(models.Model):
    externalidentifiersystemid = models.IntegerField(db_column='ExternalIdentifierSystemID',
                                                     primary_key=True)  # Field name made lowercase.
    externalidentifiersystemname = models.TextField(
        db_column='ExternalIdentifierSystemName')  # Field name made lowercase.
    identifiersystemorganizationid = models.ForeignKey('Organization',
                                                       db_column='IdentifierSystemOrganizationID')  # Field name made lowercase.
    externalidentifiersystemdescription = models.TextField(db_column='ExternalIdentifierSystemDescription',
                                                           blank=True)  # Field name made lowercase.
    externalidentifiersystemurl = models.TextField(db_column='ExternalIdentifierSystemURL',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[ExternalIdentifierSystems'


class FeatureAction(models.Model):
    featureactionid = models.IntegerField(db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature', related_name="featureaction",
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name="featureaction", db_column='ActionID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[FeatureActions'


class InstrumentOutputVariable(models.Model):
    instrumentoutputvariableid = models.AutoField(db_column='InstrumentOutputVariableID',
                                                  primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(EquipmentModel, related_name='instrumentoutputvariable', db_column='ModelID')  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', related_name='instrumentoutputvariable', db_column='VariableID')  # Field name made lowercase.
    instrumentmethodid = models.ForeignKey('Method', db_column='InstrumentMethodID')  # Field name made lowercase.
    instrumentresolution = models.TextField(db_column='InstrumentResolution', blank=True)  # Field name made lowercase.
    instrumentaccuracy = models.TextField(db_column='InstrumentAccuracy', blank=True)  # Field name made lowercase.
    instrumentrawoutputunitsid = models.ForeignKey('Units',
                                                   db_column='InstrumentRawOutputUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[InstrumentOutputVariables'


class MaintenanceAction(models.Model):
    actionid = models.ForeignKey(Action, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    isfactoryservice = models.BooleanField(db_column='IsFactoryService', default=None)  # Field name made lowercase.
    maintenancecode = models.TextField(db_column='MaintenanceCode', blank=True)  # Field name made lowercase.
    maintenancereason = models.TextField(db_column='MaintenanceReason', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[MaintenanceActions'


class MeasurementResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('MeasurementResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[MeasurementResultValueAnnotations'


class MeasurementResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('MeasurementResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[MeasurementResultValues'


class MeasurementResult(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='measurement_xlocationunitsid',
                                         db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='measurement_ylocationunitsid',
                                         db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='measurement_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[MeasurementResults'


class MethodAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='MethodID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[MethodAnnotations'


class MethodCitation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='MethodID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[MethodCitations'


class MethodExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='MethodID')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[MethodExtensionPropertyValues'


class MethodExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='MethodID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    methodexternalidentifier = models.TextField(db_column='MethodExternalIdentifier')  # Field name made lowercase.
    methodexternalidentifieruri = models.TextField(db_column='MethodExternalIdentifierURI',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[MethodExternalIdentifiers'


class Method(models.Model):
    methodid = models.IntegerField(db_column='MethodID', primary_key=True)  # Field name made lowercase.
    methodtypecv = models.TextField(db_column='MethodTypeCV')  # Field name made lowercase.
    methodcode = models.TextField(db_column='MethodCode')  # Field name made lowercase.
    methodname = models.TextField(db_column='MethodName')  # Field name made lowercase.
    methoddescription = models.TextField(db_column='MethodDescription', blank=True)  # Field name made lowercase.
    methodlink = models.TextField(db_column='MethodLink', blank=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Organization', db_column='OrganizationID', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[Methods'


class ModelAffiliation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey('Models', db_column='ModelID')  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliation, db_column='AffiliationID')  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary', default=None)  # Field name made lowercase.
    roledescription = models.TextField(db_column='RoleDescription', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Simulation].[ModelAffiliations'


class Models(models.Model):
    modelid = models.IntegerField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='ModelCode', max_length=255)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=255)  # Field name made lowercase.
    modeldescription = models.CharField(db_column='ModelDescription', max_length=500,
                                        blank=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True)  # Field name made lowercase.
    modellink = models.TextField(db_column='ModelLink', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Simulation].[Models'


class Organization(models.Model):
    organizationid = models.IntegerField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    organizationtypecv = models.TextField(db_column='OrganizationTypeCV')  # Field name made lowercase.
    organizationcode = models.TextField(db_column='OrganizationCode')  # Field name made lowercase.
    organizationname = models.TextField(db_column='OrganizationName')  # Field name made lowercase.
    organizationdescription = models.TextField(db_column='OrganizationDescription',
                                               blank=True)  # Field name made lowercase.
    organizationlink = models.TextField(db_column='OrganizationLink', blank=True)  # Field name made lowercase.
    parentorganizationid = models.ForeignKey('self', db_column='ParentOrganizationID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[Organizations'


class People(models.Model):
    personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    personfirstname = models.TextField(db_column='PersonFirstName')  # Field name made lowercase.
    personmiddlename = models.TextField(db_column='PersonMiddleName', blank=True)  # Field name made lowercase.
    personlastname = models.TextField(db_column='PersonLastName')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[People'


class PersonExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(People, db_column='PersonID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    personexternalidentifier = models.TextField(db_column='PersonExternalIdentifier')  # Field name made lowercase.
    personexternalidenifieruri = models.TextField(db_column='PersonExternalIdenifierURI',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[PersonExternalIdentifiers'


class PointCoverageResultValueAnnotation(models.Model):
    bridgeid = models.BigIntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('PointCoverageResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[PointCoverageResultValueAnnotations'


class PointCoverageResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('PointCoverageResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.BigIntegerField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='point_xlocationunitsid',
                                         db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='point_ylocationunitsid',
                                         db_column='YLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[PointCoverageResultValues'


class PointCoverageResult(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='point_intendedxspacingunitsid',
                                                db_column='IntendedXSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedyspacing = models.FloatField(db_column='IntendedYSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedyspacingunitsid = models.ForeignKey('Units', related_name='point_intendedyspacingunitsid',
                                                db_column='IntendedYSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(
        db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[PointCoverageResults'


class ProcessingLevel(models.Model):
    processinglevelid = models.IntegerField(db_column='ProcessingLevelID',
                                            primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.TextField(db_column='ProcessingLevelCode')  # Field name made lowercase.
    definition = models.TextField(db_column='Definition', blank=True)  # Field name made lowercase.
    explanation = models.TextField(db_column='Explanation', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[ProcessingLevels'


class ProfileResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('ProfileResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[ProfileResultValueAnnotations'


class ProfileResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('ProfileResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='ZAggregationInterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='profile_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[ProfileResultValues'


class ProfileResult(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='profile_xlocationunitsid', db_column='XLocationUnitsID',
                                         blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='profile_ylocationunitsid', db_column='YLocationUnitsID',
                                         blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', db_column='IntendedZSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='profile_intendedtimespacingunitsid',
                                                   db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[ProfileResults'


class ReferenceMaterialExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('ReferenceMaterial',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    referencematerialexternalidentifier = models.TextField(
        db_column='ReferenceMaterialExternalIdentifier')  # Field name made lowercase.
    referencematerialexternalidentifieruri = models.TextField(db_column='ReferenceMaterialExternalIdentifierURI',
                                                              blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[ReferenceMaterialExternalIdentifiers'


class ReferenceMaterialValue(models.Model):
    referencematerialvalueid = models.IntegerField(db_column='ReferenceMaterialValueID',
                                                   primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('ReferenceMaterial', related_name='referencematerialvalue',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.
    referencematerialvalue = models.FloatField(db_column='ReferenceMaterialValue')  # Field name made lowercase.
    referencematerialaccuracy = models.FloatField(db_column='ReferenceMaterialAccuracy', blank=True,
                                                  null=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='UnitsID')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='CitationID', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2DataQuality].[ReferenceMaterialValues'


class ReferenceMaterial(models.Model):
    referencematerialid = models.IntegerField(db_column='ReferenceMaterialID',
                                              primary_key=True)  # Field name made lowercase.
    referencematerialmediumcv = models.TextField(db_column='ReferenceMaterialMediumCV')  # Field name made lowercase.
    referencematerialorganizationid = models.ForeignKey(Organization,
                                                        db_column='ReferenceMaterialOrganizationID')  # Field name made lowercase.
    referencematerialcode = models.TextField(db_column='ReferenceMaterialCode')  # Field name made lowercase.
    referencemateriallotcode = models.TextField(db_column='ReferenceMaterialLotCode',
                                                blank=True)  # Field name made lowercase.
    referencematerialpurchasedate = models.DateTimeField(db_column='ReferenceMaterialPurchaseDate', blank=True,
                                                         null=True)  # Field name made lowercase.
    referencematerialexpirationdate = models.DateTimeField(db_column='ReferenceMaterialExpirationDate', blank=True,
                                                           null=True)  # Field name made lowercase.
    referencematerialcertificatelink = models.TextField(db_column='ReferenceMaterialCertificateLink',
                                                        blank=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature', db_column='SamplingFeatureID', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2DataQuality].[ReferenceMaterials'


class RelatedAction(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name='relatedaction',
                                 db_column='ActionID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedactionid = models.ForeignKey(Action, related_name='parent_relatedaction',
                                        db_column='RelatedActionID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[RelatedActions'


class RelatedAnnotation(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, related_name='relatedannonations_annotationid',
                                     db_column='AnnotationID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedannotationid = models.ForeignKey(Annotation, related_name='relatedannotation_relatedannontationid',
                                            db_column='RelatedAnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[RelatedAnnotations'


class RelatedCitation(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, related_name='relatedcitations_citationid',
                                   db_column='CitationID')  # Field name made lowercase.
    relationshiptypecv = models.IntegerField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedcitationid = models.ForeignKey(Citation, related_name='relatedcitations_relatedcitationid',
                                          db_column='RelatedCitationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[RelatedCitations'


class RelatedDataset(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Dataset, related_name='relateddatasets_datasetid',
                                  db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relateddatasetid = models.ForeignKey(Dataset, related_name='relateddatasets_relateddatasetid',
                                         db_column='RelatedDatasetID')  # Field name made lowercase.
    versioncode = models.TextField(db_column='VersionCode', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[RelatedDatasets'


class RelatedEquipment(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_equipmentid',
                                    db_column='EquipmentID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedequipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_relatedequipmentid',
                                           db_column='RelatedEquipmentID')  # Field name made lowercase.
    relationshipstartdatetime = models.DateTimeField(
        db_column='RelationshipStartDateTime')  # Field name made lowercase.
    relationshipstartdatetimeutcoffset = models.IntegerField(
        db_column='RelationshipStartDateTimeUTCOffset')  # Field name made lowercase.
    relationshipenddatetime = models.DateTimeField(db_column='RelationshipEndDateTime', blank=True,
                                                   null=True)  # Field name made lowercase.
    relationshipenddatetimeutcoffset = models.IntegerField(db_column='RelationshipEndDateTimeUTCOffset', blank=True,
                                                           null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Equipment].[RelatedEquipment'


class RelatedFeatures(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          related_name='relatedfeatures_samplingfeatureid',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedfeatureid = models.ForeignKey('SamplingFeature', related_name='relatedfeature_relatedfeatureid',
                                         db_column='RelatedFeatureID')  # Field name made lowercase.
    spatialoffsetid = models.ForeignKey('SpatialOffsets', db_column='SpatialOffsetID', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[RelatedFeatures'


class RelatedModel(models.Model):
    relatedid = models.IntegerField(db_column='RelatedID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, db_column='ModelID')  # Field name made lowercase.
    relationshiptypecv = models.CharField(db_column='RelationshipTypeCV', max_length=1)  # Field name made lowercase.
    relatedmodelid = models.BigIntegerField(db_column='RelatedModelID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Simulation].[RelatedModels'


class RelatedResult(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='ResultID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Result', related_name='relatedresults_relatedresultid',
                                        db_column='RelatedResultID')  # Field name made lowercase.
    versioncode = models.TextField(db_column='VersionCode', blank=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='RelatedResultSequenceNumber', blank=True,
                                                      null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[RelatedResults'


class ResultAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='ResultID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[ResultAnnotations'


class ResultDerivationEquation(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(DerivationEquation,
                                             db_column='DerivationEquationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Provenance].[ResultDerivationEquations'


class ResultExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='ResultID')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[ResultExtensionPropertyValues'


class ResultNormalizationValue(models.Model):
    resultid = models.ForeignKey('Result', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    normalizedbyreferencematerialvalueid = models.ForeignKey(ReferenceMaterialValue,
                                                             db_column='NormalizedByReferenceMaterialValueID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2DataQuality].[ResultNormalizationValues'


class ResultTypeCV(models.Model):
    resulttypecv = models.TextField(db_column='ResultTypeCV', primary_key=True)  # Field name made lowercase.
    resulttypecategory = models.TextField(db_column='ResultTypeCategory')  # Field name made lowercase.
    datatype = models.TextField(db_column='DataType')  # Field name made lowercase.
    resulttypedefinition = models.TextField(db_column='ResultTypeDefinition')  # Field name made lowercase.
    fixeddimensions = models.TextField(db_column='FixedDimensions')  # Field name made lowercase.
    varyingdimensions = models.TextField(db_column='VaryingDimensions')  # Field name made lowercase.
    spacemeasurementframework = models.TextField(db_column='SpaceMeasurementFramework')  # Field name made lowercase.
    timemeasurementframework = models.TextField(db_column='TimeMeasurementFramework')  # Field name made lowercase.
    variablemeasurementframework = models.TextField(
        db_column='VariableMeasurementFramework')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[ResultTypeCV'


class Result(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    resultuuid = models.TextField(db_column='ResultUUID')  # Field name made lowercase.
    featureactionid = models.ForeignKey(FeatureAction, db_column='FeatureActionID')  # Field name made lowercase.
    resulttypecv = models.ForeignKey(ResultTypeCV, db_column='ResultTypeCV')  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='UnitsID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier', db_column='TaxonomicClassifierID', blank=True,
                                              null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey(ProcessingLevel, db_column='ProcessingLevelID')  # Field name made lowercase.
    resultdatetime = models.DateTimeField(db_column='ResultDateTime', blank=True,
                                          null=True)  # Field name made lowercase.
    resultdatetimeutcoffset = models.BigIntegerField(db_column='ResultDateTimeUTCOffset', blank=True,
                                                     null=True)  # Field name made lowercase.
    validdatetime = models.DateTimeField(db_column='ValidDateTime', blank=True, null=True)  # Field name made lowercase.
    validdatetimeutcoffset = models.BigIntegerField(db_column='ValidDateTimeUTCOffset', blank=True,
                                                    null=True)  # Field name made lowercase.
    statuscv = models.TextField(db_column='StatusCV', blank=True)  # Field name made lowercase.
    sampledmediumcv = models.TextField(db_column='SampledMediumCV')  # Field name made lowercase.
    valuecount = models.IntegerField(db_column='ValueCount')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[Results'


class ResultsDataQuality(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Result, db_column='ResultID')  # Field name made lowercase.
    dataqualityid = models.ForeignKey(DataQuality, db_column='DataQualityID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2DataQuality].[ResultsDataQuality'


class SamplingFeatureAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[SamplingFeatureAnnotations'


class SamplingFeatureExtPropertyVal(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[SamplingFeatureExtensionPropertyValues'


class SamplingFeatureExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    samplingfeatureexternalidentifier = models.TextField(
        db_column='SamplingFeatureExternalIdentifier')  # Field name made lowercase.
    samplingfeatureexternalidentiferuri = models.TextField(db_column='SamplingFeatureExternalIdentiferURI',
                                                           blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[SamplingFeatureExternalIdentifiers'


class SamplingFeature(models.Model):
    samplingfeatureid = models.AutoField(db_column='SamplingFeatureID',
                                            primary_key=True)  # Field name made lowercase.
    samplingfeaturetypecv = models.TextField(db_column='SamplingFeatureTypeCV')  # Field name made lowercase.
    samplingfeaturecode = models.TextField(db_column='SamplingFeatureCode')  # Field name made lowercase.
    samplingfeaturename = models.TextField(db_column='SamplingFeatureName', blank=True)  # Field name made lowercase.
    samplingfeaturedescription = models.TextField(db_column='SamplingFeatureDescription',
                                                  blank=True)  # Field name made lowercase.
    samplingfeaturegeotypecv = models.TextField(db_column='SamplingFeatureGeotypeCV',
                                                blank=True)  # Field name made lowercase.
    # featuregeometry = models.TextField(db_column='FeatureGeometry',
    #                                   blank=True)  # Field name made lowercase. This field type is a guess.
    elevation_m = models.FloatField(db_column='Elevation_m', blank=True, null=True)  # Field name made lowercase.
    elevationdatumcv = models.TextField(db_column='ElevationDatumCV', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[SamplingFeatures'


class SectionResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('SectionResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[SectionResultValueAnnotations'


class SectionResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('SectionResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.BigIntegerField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.BigIntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xaggregationinterval = models.FloatField(db_column='XAggregationInterval')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_xlocationunitsid',
                                         db_column='XLocationUnitsID')  # Field name made lowercase.
    zlocation = models.BigIntegerField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='ZAggregationInterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_zlocationunitsid',
                                         db_column='ZLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='sectionresults_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[SectionResultValues'


class SectionResult(models.Model):
    resultid = models.ForeignKey(Result, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='sectionresults_ylocationunitsid',
                                         db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedxspacingunitsid',
                                                db_column='IntendedXSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedzspacingunitsid',
                                                db_column='IntendedZSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedtimespacingunitsid',
                                                   db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[SectionResults'


class Simulation(models.Model):
    simulationid = models.IntegerField(db_column='SimulationID', primary_key=True)  # Field name made lowercase.
    actionid = models.BigIntegerField(db_column='ActionID')  # Field name made lowercase.
    simulationname = models.CharField(db_column='SimulationName', max_length=255)  # Field name made lowercase.
    simulationdescription = models.CharField(db_column='SimulationDescription', max_length=500,
                                             blank=True)  # Field name made lowercase.
    simulationstartdatetime = models.DateTimeField(db_column='SimulationStartDateTime')  # Field name made lowercase.
    simulationstartdatetimeutcoffset = models.IntegerField(
        db_column='SimulationStartDateTimeUTCOffset')  # Field name made lowercase.
    simulationenddatetime = models.DateTimeField(db_column='SimulationEndDateTime')  # Field name made lowercase.
    simulationenddatetimeutcoffset = models.IntegerField(
        db_column='SimulationEndDateTimeUTCOffset')  # Field name made lowercase.
    timestepvalue = models.FloatField(db_column='TimeStepValue')  # Field name made lowercase.
    timestepunitsid = models.BigIntegerField(db_column='TimeStepUnitsID')  # Field name made lowercase.
    inputdatasetid = models.BigIntegerField(db_column='InputDataSetID', blank=True,
                                            null=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, db_column='ModelID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Simulation].[Simulations'


class Sites(models.Model):
    samplingfeatureid = models.ForeignKey(SamplingFeature, related_name='sites',
                                          db_column='SamplingFeatureID',
                                          primary_key=True)  # Field name made lowercase.
    sitetypecv = models.TextField(db_column='SiteTypeCV')  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    latlondatumid = models.ForeignKey('SpatialReference', db_column='LatLonDatumID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[Sites'


class SpatialOffsets(models.Model):
    spatialoffsetid = models.IntegerField(db_column='SpatialOffsetID', primary_key=True)  # Field name made lowercase.
    spatialoffsettypecv = models.TextField(db_column='SpatialOffsetTypeCV')  # Field name made lowercase.
    offset1value = models.FloatField(db_column='Offset1Value')  # Field name made lowercase.
    offset1unitid = models.IntegerField(db_column='Offset1UnitID')  # Field name made lowercase.
    offset2value = models.FloatField(db_column='Offset2Value', blank=True, null=True)  # Field name made lowercase.
    offset2unitid = models.IntegerField(db_column='Offset2UnitID', blank=True, null=True)  # Field name made lowercase.
    offset3value = models.FloatField(db_column='Offset3Value', blank=True, null=True)  # Field name made lowercase.
    offset3unitid = models.IntegerField(db_column='Offset3UnitID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[SpatialOffsets'


class SpatialReferenceExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference',
                                           db_column='SpatialReferenceID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    spatialreferenceexternalidentifier = models.TextField(
        db_column='SpatialReferenceExternalIdentifier')  # Field name made lowercase.
    spatialreferenceexternalidentifieruri = models.TextField(db_column='SpatialReferenceExternalIdentifierURI',
                                                             blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[SpatialReferenceExternalIdentifiers'


class SpatialReference(models.Model):
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID',
                                             primary_key=True)  # Field name made lowercase.
    srscode = models.TextField(db_column='SRSCode', blank=True)  # Field name made lowercase.
    srsname = models.TextField(db_column='SRSName')  # Field name made lowercase.
    srsdescription = models.TextField(db_column='SRSDescription', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[SpatialReferences'


class SpecimenBatchPostion(models.Model):
    featureactionid = models.ForeignKey(FeatureAction, db_column='FeatureActionID',
                                        primary_key=True)  # Field name made lowercase.
    batchpositionnumber = models.IntegerField(db_column='BatchPositionNumber')  # Field name made lowercase.
    batchpositionlabel = models.TextField(db_column='BatchPositionLabel', blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2LabAnalyses].[SpecimenBatchPostions'


class SpecimenTaxonomicClassifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Specimens', db_column='SamplingFeatureID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier',
                                              db_column='TaxonomicClassifierID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[SpecimenTaxonomicClassifiers'


class Specimens(models.Model):
    samplingfeatureid = models.ForeignKey(SamplingFeature, db_column='SamplingFeatureID',
                                          primary_key=True)  # Field name made lowercase.
    specimentypecv = models.TextField(db_column='SpecimenTypeCV')  # Field name made lowercase.
    specimenmediumcv = models.TextField(db_column='SpecimenMediumCV')  # Field name made lowercase.
    isfieldspecimen = models.BooleanField(db_column='IsFieldSpecimen', default=None)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2SamplingFeatures].[Specimens'


class SpectraResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('SpectraResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[SpectraResultValueAnnotations'


class SpectraResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('SpectraResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    excitationwavelength = models.FloatField(db_column='ExcitationWavelength')  # Field name made lowercase.
    emissionwavelength = models.FloatField(db_column='EmissionWavelength')  # Field name made lowercase.
    wavelengthunitsid = models.ForeignKey('Units', related_name='spectralresultsvalues_wavelengthunitsid',
                                          db_column='WavelengthUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[SpectraResultValues'


class SpectraResult(models.Model):
    resultid = models.ForeignKey(Result, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='spectralresults_xlocationunitsid',
                                         db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='spectralresults_zlocationunitsid',
                                         db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedwavelengthspacing = models.FloatField(db_column='IntendedWavelengthSpacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedwavelengthspacingunitsid = models.ForeignKey('Units',
                                                         related_name='spectralresult_intendedwavelengthspacingunitsid',
                                                         db_column='IntendedWavelengthSpacingUnitsID',
                                                         blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[SpectraResults'


class TaxonomicClassifierExtId(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier',
                                              db_column='TaxonomicClassifierID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    taxonomicclassifierexternalidentifier = models.TextField(
        db_column='TaxonomicClassifierExternalIdentifier')  # Field name made lowercase.
    taxonomicclassifierexternalidentifieruri = models.TextField(db_column='TaxonomicClassifierExternalIdentifierURI',
                                                                blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[TaxonomicClassifierExternalIdentifiers'


class TaxonomicClassifier(models.Model):
    taxonomicclassifierid = models.IntegerField(db_column='TaxonomicClassifierID',
                                                primary_key=True)  # Field name made lowercase.
    taxonomicclassifiertypecv = models.TextField(db_column='TaxonomicClassifierTypeCV')  # Field name made lowercase.
    taxonomicclassifiername = models.TextField(db_column='TaxonomicClassifierName')  # Field name made lowercase.
    taxonomicclassifiercommonname = models.TextField(db_column='TaxonomicClassifierCommonName',
                                                     blank=True)  # Field name made lowercase.
    taxonomicclassifierdescription = models.TextField(db_column='TaxonomicClassifierDescription',
                                                      blank=True)  # Field name made lowercase.
    parenttaxonomicclassifierid = models.ForeignKey('self', db_column='ParentTaxonomicClassifierID', blank=True,
                                                    null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[TaxonomicClassifiers'


class TimeSeriesResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TimeSeriesResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[TimeSeriesResultValueAnnotations'


class TimeSeriesResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TimeSeriesResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TimeSeriesResultValues'


class TimeSeriesResult(models.Model):
    resultid = models.ForeignKey(Result, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_xlocationunits',
                                         db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_ylocationunits',
                                         db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_zlocationunits',
                                         db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='timeseriesresults_intendedtimespacingunitsid',
                                                   db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TimeSeriesResults'


class TrajectoryResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TrajectoryResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[TrajectoryResultValueAnnotations'


class TrajectoryResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TrajectoryResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_xlocationunitsid',
                                         db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_ylocationunitsid',
                                         db_column='YLocationUnitsID')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_zlocationunitsid',
                                         db_column='ZLocationUnitsID')  # Field name made lowercase.
    trajectorydistance = models.FloatField(db_column='TrajectoryDistance')  # Field name made lowercase.
    trajectorydistanceaggregationinterval = models.FloatField(
        db_column='TrajectoryDistanceAggregationInterval')  # Field name made lowercase.
    trajectorydistanceunitsid = models.IntegerField(db_column='TrajectoryDistanceUnitsID')  # Field name made lowercase.
    censorcode = models.TextField(db_column='CensorCode')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='trajectoryresultvalues_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TrajectoryResultValues'


class TrajectoryResult(models.Model):
    resultid = models.ForeignKey(Result, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtrajectoryspacing = models.FloatField(db_column='IntendedTrajectorySpacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedtrajectoryspacingunitsid = models.ForeignKey('Units',
                                                         related_name='trajectoryresults_intendedtrajectoryspacingunitsid',
                                                         db_column='IntendedTrajectorySpacingUnitsID',
                                                         blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='trajectoryresults_intendedtimespacingunitsid',
                                                   db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TrajectoryResults'


class TransectResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TransectResultValue', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Annotations].[TransectResultValueAnnotations'


class TransectResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TransectResult', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.DateTimeField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID')  # Field name made lowercase.
    transectdistance = models.FloatField(db_column='TransectDistance')  # Field name made lowercase.
    transectdistanceaggregationinterval = models.FloatField(
        db_column='TransectDistanceAggregationInterval')  # Field name made lowercase.
    transectdistanceunitsid = models.IntegerField(db_column='TransectDistanceUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(
        db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TransectResultValues'


class TransectResult(models.Model):
    resultid = models.ForeignKey(Result, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='transectresults_zlocationunitsid',
                                         db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtransectspacing = models.FloatField(db_column='IntendedTransectSpacing', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtransectspacingunitsid = models.ForeignKey('Units', db_column='IntendedTransectSpacingUnitsID', blank=True,
                                                       null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='transectresults_intendedtimespacingunitsid',
                                                   db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Results].[TransectResults'


class Units(models.Model):
    unitsid = models.IntegerField(db_column='UnitsID', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.TextField(db_column='UnitsTypeCV')  # Field name made lowercase.
    unitsabbreviation = models.TextField(db_column='UnitsAbbreviation')  # Field name made lowercase.
    unitsname = models.TextField(db_column='UnitsName')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[Units'


class VariableExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='VariableID')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExtensionProperties].[VariableExtensionPropertyValues'


class VariableExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='VariableID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    variableexternalidentifer = models.TextField(db_column='VariableExternalIdentifer')  # Field name made lowercase.
    variableexternalidentifieruri = models.TextField(db_column='VariableExternalIdentifierURI',
                                                     blank=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2ExternalIdentifiers].[VariableExternalIdentifiers'


class Variable(models.Model):
    variableid = models.IntegerField(db_column='VariableID', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.TextField(db_column='VariableTypeCV')  # Field name made lowercase.
    variablecode = models.TextField(db_column='VariableCode')  # Field name made lowercase.
    variablenamecv = models.TextField(db_column='VariableNameCV')  # Field name made lowercase.
    variabledefinition = models.TextField(db_column='VariableDefinition', blank=True)  # Field name made lowercase.
    speciationcv = models.TextField(db_column='SpeciationCV', blank=True)  # Field name made lowercase.
    nodatavalue = models.FloatField(db_column='NoDataValue')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ODM2Core].[Variables'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'sysdiagrams'