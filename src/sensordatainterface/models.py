from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Actionannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', db_column='ActionID')  # Field name made lowercase.
    annotationid = models.ForeignKey('Annotations', db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionAnnotations'


class Actionby(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', db_column='ActionID')  # Field name made lowercase.
    affiliationid = models.ForeignKey('Affiliations', db_column='AffiliationID')  # Field name made lowercase.
    isactionlead = models.BooleanField(db_column='IsActionLead')  # Field name made lowercase.
    roledescription = models.TextField(db_column='RoleDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionBy'


class Actiondirectives(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', db_column='ActionID')  # Field name made lowercase.
    directiveid = models.ForeignKey('Directives', db_column='DirectiveID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionDirectives'


class Actionextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', db_column='ActionID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionExtensionPropertyValues'


class Actions(models.Model):
    actionid = models.IntegerField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.TextField(db_column='ActionTypeCV')  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', db_column='MethodID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='BeginDateTimeUTCOffset')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='EndDateTimeUTCOffset', blank=True,
                                               null=True)  # Field name made lowercase.
    actiondescription = models.TextField(db_column='ActionDescription', blank=True)  # Field name made lowercase.
    actionfilelink = models.TextField(db_column='ActionFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actions'


class Affiliations(models.Model):
    affiliationid = models.IntegerField(db_column='AffiliationID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('People', db_column='PersonID')  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', db_column='OrganizationID', blank=True,
                                       null=True)  # Field name made lowercase.
    isprimaryorganizationcontact = models.NullBooleanField(
        db_column='IsPrimaryOrganizationContact')  # Field name made lowercase.
    affiliationstartdate = models.DateField(db_column='AffiliationStartDate')  # Field name made lowercase.
    affiliationenddate = models.DateField(db_column='AffiliationEndDate', blank=True,
                                          null=True)  # Field name made lowercase.
    primaryphone = models.TextField(db_column='PrimaryPhone', blank=True)  # Field name made lowercase.
    primaryemail = models.TextField(db_column='PrimaryEmail')  # Field name made lowercase.
    primaryaddress = models.TextField(db_column='PrimaryAddress', blank=True)  # Field name made lowercase.
    personlink = models.TextField(db_column='PersonLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Affiliations'


class Annotations(models.Model):
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
    citationid = models.ForeignKey('Citations', db_column='CitationID', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Annotations'


class Authorlists(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', db_column='CitationID')  # Field name made lowercase.
    personid = models.ForeignKey('People', db_column='PersonID')  # Field name made lowercase.
    authororder = models.IntegerField(db_column='AuthorOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuthorLists'


class Cvterms(models.Model):
    termid = models.IntegerField(db_column='TermID', primary_key=True)  # Field name made lowercase.
    term = models.TextField(db_column='Term')  # Field name made lowercase.
    definition = models.TextField(db_column='Definition', blank=True)  # Field name made lowercase.
    odmvocabulary = models.TextField(db_column='ODMVocabulary')  # Field name made lowercase.
    sourcevocabulary = models.TextField(db_column='SourceVocabulary', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CVTerms'


class Calibrationactions(models.Model):
    actionid = models.ForeignKey(Actions, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    calibrationcheckvalue = models.FloatField(db_column='CalibrationCheckValue', blank=True,
                                              null=True)  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables',
                                                   db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    calibrationequation = models.TextField(db_column='CalibrationEquation', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationActions'


class Calibrationreferenceequipment(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipment', db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationReferenceEquipment'


class Calibrationstandards(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, db_column='ActionID')  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationStandards'


class Categoricalresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Categoricalresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResultValueAnnotations'


class Categoricalresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Categoricalresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResultValues'


class Categoricalresults(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True,
                                           null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    qualitycodecv = models.BigIntegerField(db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResults'


class Citationextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', db_column='CitationID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CitationExtensionPropertyValues'


class Citationexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', db_column='CitationID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey('Externalidentifiersystems',
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    citationexternalidentifer = models.TextField(db_column='CitationExternalIdentifer')  # Field name made lowercase.
    citationexternalidentiferuri = models.TextField(db_column='CitationExternalIdentiferURI',
                                                    blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CitationExternalIdentifiers'


class Citations(models.Model):
    citationid = models.IntegerField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher')  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='PublicationYear')  # Field name made lowercase.
    citationlink = models.TextField(db_column='CitationLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citations'


class Dataloggerfiles(models.Model):
    dataloggerfileid = models.AutoField(db_column='DataLoggerFileID', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('Dataloggerprogramfiles', db_column='ProgramID')  # Field name made lowercase.
    dataloggerfilename = models.TextField(db_column='DataLoggerFileName')  # Field name made lowercase.
    dataloggerfiledescription = models.TextField(db_column='DataLoggerFileDescription',
                                                 blank=True)  # Field name made lowercase.
    dataloggerfilelink = models.TextField(db_column='DataLoggerFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataLoggerFiles'


class Dataquality(models.Model):
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
        managed = False
        db_table = 'DataQuality'


class Datasetcitations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey('Datasets', db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSetCitations'


class Datasets(models.Model):
    datasetid = models.IntegerField(db_column='DataSetID', primary_key=True)  # Field name made lowercase.
    datasetuuid = models.TextField(db_column='DataSetUUID')  # Field name made lowercase.
    datasettypecv = models.TextField(db_column='DataSetTypeCV')  # Field name made lowercase.
    datasetcode = models.TextField(db_column='DataSetCode')  # Field name made lowercase.
    datasettitle = models.TextField(db_column='DataSetTitle')  # Field name made lowercase.
    datasetabstract = models.TextField(db_column='DataSetAbstract')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSets'


class Datasetsresults(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, db_column='DataSetID')  # Field name made lowercase.
    resultid = models.ForeignKey('Results', db_column='ResultID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSetsResults'


class Dataloggerfilecolumns(models.Model):
    dataloggerfilecolumnid = models.AutoField(db_column='DataloggerFileColumnID',
                                              primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', db_column='ResultID', blank=True, null=True)  # Field name made lowercase.
    dataloggerfileid = models.ForeignKey(Dataloggerfiles, db_column='DataLoggerFileID')  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables',
                                                   db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    columnlabel = models.TextField(db_column='ColumnLabel')  # Field name made lowercase.
    columndescription = models.TextField(db_column='ColumnDescription', blank=True)  # Field name made lowercase.
    measurementequation = models.TextField(db_column='MeasurementEquation', blank=True)  # Field name made lowercase.
    scaninterval = models.FloatField(db_column='ScanInterval', blank=True, null=True)  # Field name made lowercase.
    scanintervalunitsid = models.ForeignKey('Units', db_column='ScanIntervalUnitsID', blank=True,
                                            null=True)  # Field name made lowercase.
    recordinginterval = models.FloatField(db_column='RecordingInterval', blank=True,
                                          null=True)  # Field name made lowercase.
    recordingintervalunitsid = models.ForeignKey('Units', related_name='column_recordingintervalunitsid', db_column='RecordingIntervalUnitsID', blank=True,
                                                 null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV',
                                              blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataloggerFileColumns'


class Dataloggerprogramfiles(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliations, db_column='AffiliationID')  # Field name made lowercase.
    programname = models.TextField(db_column='ProgramName')  # Field name made lowercase.
    programdescription = models.TextField(db_column='ProgramDescription', blank=True)  # Field name made lowercase.
    programversion = models.TextField(db_column='ProgramVersion', blank=True)  # Field name made lowercase.
    programfilelink = models.TextField(db_column='ProgramFileLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataloggerProgramFiles'


class Derivationequations(models.Model):
    derivationequationid = models.IntegerField(db_column='DerivationEquationID',
                                               primary_key=True)  # Field name made lowercase.
    derivationequation = models.TextField(db_column='DerivationEquation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DerivationEquations'


class Directives(models.Model):
    directiveid = models.IntegerField(db_column='DirectiveID', primary_key=True)  # Field name made lowercase.
    directivetypecv = models.TextField(db_column='DirectiveTypeCV')  # Field name made lowercase.
    directivedescription = models.TextField(db_column='DirectiveDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Directives'


class Equipment(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  # Field name made lowercase.
    equipmentcode = models.TextField(db_column='EquipmentCode')  # Field name made lowercase.
    equipmentname = models.TextField(db_column='EquipmentName')  # Field name made lowercase.
    equipmenttypecv = models.TextField(db_column='EquipmentTypeCV')  # Field name made lowercase.
    equipmentmodelid = models.ForeignKey('Equipmentmodels', db_column='EquipmentModelID')  # Field name made lowercase.
    equipmentserialnumber = models.TextField(db_column='EquipmentSerialNumber')  # Field name made lowercase.
    equipmentownerid = models.ForeignKey('People', db_column='EquipmentOwnerID')  # Field name made lowercase.
    equipmentvendorid = models.ForeignKey('Organizations', db_column='EquipmentVendorID')  # Field name made lowercase.
    equipmentpurchasedate = models.DateTimeField(db_column='EquipmentPurchaseDate')  # Field name made lowercase.
    equipmentpurchaseordernumber = models.TextField(db_column='EquipmentPurchaseOrderNumber',
                                                    blank=True)  # Field name made lowercase.
    equipmentdescription = models.TextField(db_column='EquipmentDescription', blank=True)  # Field name made lowercase.
    equipmentdocumentationlink = models.TextField(db_column='EquipmentDocumentationLink',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Equipment'


class Equipmentannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, db_column='EquipmentID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentAnnotations'


class Equipmentmodels(models.Model):
    equipmentmodelid = models.AutoField(db_column='EquipmentModelID', primary_key=True)  # Field name made lowercase.
    modelmanufacturerid = models.ForeignKey('Organizations',
                                            db_column='ModelManufacturerID')  # Field name made lowercase.
    modelpartnumber = models.TextField(db_column='ModelPartNumber', blank=True)  # Field name made lowercase.
    modelname = models.TextField(db_column='ModelName')  # Field name made lowercase.
    modeldescription = models.TextField(db_column='ModelDescription', blank=True)  # Field name made lowercase.
    isinstrument = models.BooleanField(db_column='IsInstrument')  # Field name made lowercase.
    modelspecificationsfilelink = models.TextField(db_column='ModelSpecificationsFileLink',
                                                   blank=True)  # Field name made lowercase.
    modellink = models.TextField(db_column='ModelLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentModels'


class Equipmentused(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentUsed'


class Extensionproperties(models.Model):
    propertyid = models.IntegerField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    propertyname = models.TextField(db_column='PropertyName')  # Field name made lowercase.
    propertydescription = models.TextField(db_column='PropertyDescription', blank=True)  # Field name made lowercase.
    propertydatatypecv = models.TextField(db_column='PropertyDataTypeCV')  # Field name made lowercase.
    propertyunitsid = models.ForeignKey('Units', db_column='PropertyUnitsID', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtensionProperties'


class Externalidentifiersystems(models.Model):
    externalidentifiersystemid = models.IntegerField(db_column='ExternalIdentifierSystemID',
                                                     primary_key=True)  # Field name made lowercase.
    externalidentifiersystemname = models.TextField(
        db_column='ExternalIdentifierSystemName')  # Field name made lowercase.
    identifiersystemorganizationid = models.ForeignKey('Organizations',
                                                       db_column='IdentifierSystemOrganizationID')  # Field name made lowercase.
    externalidentifiersystemdescription = models.TextField(db_column='ExternalIdentifierSystemDescription',
                                                           blank=True)  # Field name made lowercase.
    externalidentifiersystemurl = models.TextField(db_column='ExternalIdentifierSystemURL',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternalIdentifierSystems'


class Featureactions(models.Model):
    featureactionid = models.IntegerField(db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, db_column='ActionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeatureActions'


class Instrumentoutputvariables(models.Model):
    instrumentoutputvariableid = models.AutoField(db_column='InstrumentOutputVariableID',
                                                  primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Equipmentmodels, db_column='ModelID')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', db_column='VariableID')  # Field name made lowercase.
    instrumentmethodid = models.ForeignKey('Methods', db_column='InstrumentMethodID')  # Field name made lowercase.
    instrumentresolution = models.TextField(db_column='InstrumentResolution', blank=True)  # Field name made lowercase.
    instrumentaccuracy = models.TextField(db_column='InstrumentAccuracy', blank=True)  # Field name made lowercase.
    instrumentrawoutputunitsid = models.ForeignKey('Units',
                                                   db_column='InstrumentRawOutputUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstrumentOutputVariables'


class Maintenanceactions(models.Model):
    actionid = models.ForeignKey(Actions, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    isfactoryservice = models.BooleanField(db_column='IsFactoryService')  # Field name made lowercase.
    maintenancecode = models.TextField(db_column='MaintenanceCode', blank=True)  # Field name made lowercase.
    maintenancereason = models.TextField(db_column='MaintenanceReason', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaintenanceActions'


class Measurementresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Measurementresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResultValueAnnotations'


class Measurementresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Measurementresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResultValues'


class Measurementresults(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='measurement_xlocationunitsid', db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='measurement_ylocationunitsid', db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='measurement_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResults'


class Methodannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', db_column='MethodID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodAnnotations'


class Methodcitations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', db_column='MethodID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodCitations'


class Methodextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', db_column='MethodID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodExtensionPropertyValues'


class Methodexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', db_column='MethodID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    methodexternalidentifier = models.TextField(db_column='MethodExternalIdentifier')  # Field name made lowercase.
    methodexternalidentifieruri = models.TextField(db_column='MethodExternalIdentifierURI',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodExternalIdentifiers'


class Methods(models.Model):
    methodid = models.IntegerField(db_column='MethodID', primary_key=True)  # Field name made lowercase.
    methodtypecv = models.TextField(db_column='MethodTypeCV')  # Field name made lowercase.
    methodcode = models.TextField(db_column='MethodCode')  # Field name made lowercase.
    methodname = models.TextField(db_column='MethodName')  # Field name made lowercase.
    methoddescription = models.TextField(db_column='MethodDescription', blank=True)  # Field name made lowercase.
    methodlink = models.TextField(db_column='MethodLink', blank=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', db_column='OrganizationID', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Methods'


class Modelaffiliations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey('Models', db_column='ModelID')  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliations, db_column='AffiliationID')  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    roledescription = models.TextField(db_column='RoleDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModelAffiliations'


class Models(models.Model):
    modelid = models.IntegerField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='ModelCode', max_length=255)  # Field name made lowercase.
    modelname = models.CharField(db_column='ModelName', max_length=255)  # Field name made lowercase.
    modeldescription = models.CharField(db_column='ModelDescription', max_length=500,
                                        blank=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True)  # Field name made lowercase.
    modellink = models.TextField(db_column='ModelLink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Models'


class Organizations(models.Model):
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
        managed = False
        db_table = 'Organizations'


class People(models.Model):
    personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    personfirstname = models.TextField(db_column='PersonFirstName')  # Field name made lowercase.
    personmiddlename = models.TextField(db_column='PersonMiddleName', blank=True)  # Field name made lowercase.
    personlastname = models.TextField(db_column='PersonLastName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'People'


class Personexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(People, db_column='PersonID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    personexternalidentifier = models.TextField(db_column='PersonExternalIdentifier')  # Field name made lowercase.
    personexternalidenifieruri = models.TextField(db_column='PersonExternalIdenifierURI',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonExternalIdentifiers'


class Pointcoverageresultvalueannotations(models.Model):
    bridgeid = models.BigIntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Pointcoverageresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResultValueAnnotations'


class Pointcoverageresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Pointcoverageresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.BigIntegerField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='point_xlocationunitsid', db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='point_ylocationunitsid', db_column='YLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResultValues'


class Pointcoverageresults(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='point_intendedxspacingunitsid', db_column='IntendedXSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedyspacing = models.FloatField(db_column='IntendedYSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedyspacingunitsid = models.ForeignKey('Units', related_name='point_intendedyspacingunitsid', db_column='IntendedYSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(
        db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResults'


class Processinglevels(models.Model):
    processinglevelid = models.IntegerField(db_column='ProcessingLevelID',
                                            primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.TextField(db_column='ProcessingLevelCode')  # Field name made lowercase.
    definition = models.TextField(db_column='Definition', blank=True)  # Field name made lowercase.
    explanation = models.TextField(db_column='Explanation', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProcessingLevels'


class Profileresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Profileresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResultValueAnnotations'


class Profileresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Profileresults', db_column='ResultID')  # Field name made lowercase.
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
                                    related_name='profile_timeaggregationintervalunitsid', db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResultValues'


class Profileresults(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='profile_xlocationunitsid', db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='profile_ylocationunitsid', db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', db_column='IntendedZSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='profile_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResults'


class Referencematerialexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    referencematerialexternalidentifier = models.TextField(
        db_column='ReferenceMaterialExternalIdentifier')  # Field name made lowercase.
    referencematerialexternalidentifieruri = models.TextField(db_column='ReferenceMaterialExternalIdentifierURI',
                                                              blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterialExternalIdentifiers'


class Referencematerialvalues(models.Model):
    referencematerialvalueid = models.IntegerField(db_column='ReferenceMaterialValueID',
                                                   primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials',
                                            db_column='ReferenceMaterialID')  # Field name made lowercase.
    referencematerialvalue = models.FloatField(db_column='ReferenceMaterialValue')  # Field name made lowercase.
    referencematerialaccuracy = models.FloatField(db_column='ReferenceMaterialAccuracy', blank=True,
                                                  null=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='UnitsID')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, db_column='CitationID', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterialValues'


class Referencematerials(models.Model):
    referencematerialid = models.IntegerField(db_column='ReferenceMaterialID',
                                              primary_key=True)  # Field name made lowercase.
    referencematerialmediumcv = models.TextField(db_column='ReferenceMaterialMediumCV')  # Field name made lowercase.
    referencematerialorganizationid = models.ForeignKey(Organizations,
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
    samplingfeatureid = models.ForeignKey('Samplingfeatures', db_column='SamplingFeatureID', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterials'


class Relatedactions(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, related_name='relatedactions_actionid', db_column='ActionID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedactionid = models.ForeignKey(Actions, related_name='relatedactions_relatedactionid', db_column='RelatedActionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedActions'


class Relatedannotations(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, related_name='relatedannonations_annotationid', db_column='AnnotationID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedannotationid = models.ForeignKey(Annotations, related_name='relatedannotation_relatedannontationid', db_column='RelatedAnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedAnnotations'


class Relatedcitations(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, related_name='relatedcitations_citationid', db_column='CitationID')  # Field name made lowercase.
    relationshiptypecv = models.IntegerField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedcitationid = models.ForeignKey(Citations,  related_name='relatedcitations_relatedcitationid', db_column='RelatedCitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedCitations'


class Relateddatasets(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, related_name='relateddatasets_datasetid', db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relateddatasetid = models.ForeignKey(Datasets,  related_name='relateddatasets_relateddatasetid', db_column='RelatedDatasetID')  # Field name made lowercase.
    versioncode = models.TextField(db_column='VersionCode', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedDatasets'


class Relatedequipment(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_equipmentid', db_column='EquipmentID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedequipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_relatedequipmentid', db_column='RelatedEquipmentID')  # Field name made lowercase.
    relationshipstartdatetime = models.DateTimeField(
        db_column='RelationshipStartDateTime')  # Field name made lowercase.
    relationshipstartdatetimeutcoffset = models.IntegerField(
        db_column='RelationshipStartDateTimeUTCOffset')  # Field name made lowercase.
    relationshipenddatetime = models.DateTimeField(db_column='RelationshipEndDateTime', blank=True,
                                                   null=True)  # Field name made lowercase.
    relationshipenddatetimeutcoffset = models.IntegerField(db_column='RelationshipEndDateTimeUTCOffset', blank=True,
                                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedEquipment'


class Relatedfeatures(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures',
                                          related_name='relatedfeatures_samplingfeatureid', db_column='SamplingFeatureID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedfeatureid = models.ForeignKey('Samplingfeatures', related_name='relatedfeature_relatedfeatureid', db_column='RelatedFeatureID')  # Field name made lowercase.
    spatialoffsetid = models.ForeignKey('Spatialoffsets', db_column='SpatialOffsetID', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedFeatures'


class Relatedmodels(models.Model):
    relatedid = models.IntegerField(db_column='RelatedID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, db_column='ModelID')  # Field name made lowercase.
    relationshiptypecv = models.CharField(db_column='RelationshipTypeCV', max_length=1)  # Field name made lowercase.
    relatedmodelid = models.BigIntegerField(db_column='RelatedModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedModels'


class Relatedresults(models.Model):
    relationid = models.IntegerField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', db_column='ResultID')  # Field name made lowercase.
    relationshiptypecv = models.TextField(db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Results', related_name='relatedresults_relatedresultid', db_column='RelatedResultID')  # Field name made lowercase.
    versioncode = models.TextField(db_column='VersionCode', blank=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='RelatedResultSequenceNumber', blank=True,
                                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedResults'


class Resultannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', db_column='ResultID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultAnnotations'


class Resultderivationequations(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(Derivationequations,
                                             db_column='DerivationEquationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultDerivationEquations'


class Resultextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', db_column='ResultID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultExtensionPropertyValues'


class Resultnormalizationvalues(models.Model):
    resultid = models.ForeignKey('Results', db_column='ResultID', primary_key=True)  # Field name made lowercase.
    normalizedbyreferencematerialvalueid = models.ForeignKey(Referencematerialvalues,
                                                             db_column='NormalizedByReferenceMaterialValueID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultNormalizationValues'


class Resulttypecv(models.Model):
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
        managed = False
        db_table = 'ResultTypeCV'


class Results(models.Model):
    resultid = models.BigIntegerField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    resultuuid = models.TextField(db_column='ResultUUID')  # Field name made lowercase.
    featureactionid = models.ForeignKey(Featureactions, db_column='FeatureActionID')  # Field name made lowercase.
    resulttypecv = models.ForeignKey(Resulttypecv, db_column='ResultTypeCV')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='UnitsID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', db_column='TaxonomicClassifierID', blank=True,
                                              null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey(Processinglevels, db_column='ProcessingLevelID')  # Field name made lowercase.
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
        managed = False
        db_table = 'Results'


class Resultsdataquality(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Results, db_column='ResultID')  # Field name made lowercase.
    dataqualityid = models.ForeignKey(Dataquality, db_column='DataQualityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultsDataQuality'


class Samplingfeatureannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureAnnotations'


class Samplingfeatureextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureExtensionPropertyValues'


class Samplingfeatureexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures',
                                          db_column='SamplingFeatureID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    samplingfeatureexternalidentifier = models.TextField(
        db_column='SamplingFeatureExternalIdentifier')  # Field name made lowercase.
    samplingfeatureexternalidentiferuri = models.TextField(db_column='SamplingFeatureExternalIdentiferURI',
                                                           blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureExternalIdentifiers'


class Samplingfeatures(models.Model):
    samplingfeatureid = models.IntegerField(db_column='SamplingFeatureID',
                                            primary_key=True)  # Field name made lowercase.
    samplingfeaturetypecv = models.TextField(db_column='SamplingFeatureTypeCV')  # Field name made lowercase.
    samplingfeaturecode = models.TextField(db_column='SamplingFeatureCode')  # Field name made lowercase.
    samplingfeaturename = models.TextField(db_column='SamplingFeatureName', blank=True)  # Field name made lowercase.
    samplingfeaturedescription = models.TextField(db_column='SamplingFeatureDescription',
                                                  blank=True)  # Field name made lowercase.
    samplingfeaturegeotypecv = models.TextField(db_column='SamplingFeatureGeotypeCV',
                                                blank=True)  # Field name made lowercase.
    featuregeometry = models.TextField(db_column='FeatureGeometry',
                                       blank=True)  # Field name made lowercase. This field type is a guess.
    elevation_m = models.FloatField(db_column='Elevation_m', blank=True, null=True)  # Field name made lowercase.
    elevationdatumcv = models.TextField(db_column='ElevationDatumCV', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatures'


class Sectionresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Sectionresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResultValueAnnotations'


class Sectionresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Sectionresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.BigIntegerField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.BigIntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xaggregationinterval = models.FloatField(db_column='XAggregationInterval')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_xlocationunitsid', db_column='XLocationUnitsID')  # Field name made lowercase.
    zlocation = models.BigIntegerField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='ZAggregationInterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_zlocationunitsid', db_column='ZLocationUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='sectionresults_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResultValues'


class Sectionresults(models.Model):
    resultid = models.ForeignKey(Results, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='sectionresults_ylocationunitsid', db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='IntendedXSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedxspacingunitsid', db_column='IntendedXSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='IntendedZSpacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedzspacingunitsid', db_column='IntendedZSpacingUnitsID', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResults'


class Simulations(models.Model):
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
        managed = False
        db_table = 'Simulations'


class Sites(models.Model):
    samplingfeatureid = models.ForeignKey(Samplingfeatures, db_column='SamplingFeatureID',
                                          primary_key=True)  # Field name made lowercase.
    sitetypecv = models.TextField(db_column='SiteTypeCV')  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    latlondatumid = models.ForeignKey('Spatialreferences', db_column='LatLonDatumID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sites'


class Spatialoffsets(models.Model):
    spatialoffsetid = models.IntegerField(db_column='SpatialOffsetID', primary_key=True)  # Field name made lowercase.
    spatialoffsettypecv = models.TextField(db_column='SpatialOffsetTypeCV')  # Field name made lowercase.
    offset1value = models.FloatField(db_column='Offset1Value')  # Field name made lowercase.
    offset1unitid = models.IntegerField(db_column='Offset1UnitID')  # Field name made lowercase.
    offset2value = models.FloatField(db_column='Offset2Value', blank=True, null=True)  # Field name made lowercase.
    offset2unitid = models.IntegerField(db_column='Offset2UnitID', blank=True, null=True)  # Field name made lowercase.
    offset3value = models.FloatField(db_column='Offset3Value', blank=True, null=True)  # Field name made lowercase.
    offset3unitid = models.IntegerField(db_column='Offset3UnitID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpatialOffsets'


class Spatialreferenceexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences',
                                           db_column='SpatialReferenceID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    spatialreferenceexternalidentifier = models.TextField(
        db_column='SpatialReferenceExternalIdentifier')  # Field name made lowercase.
    spatialreferenceexternalidentifieruri = models.TextField(db_column='SpatialReferenceExternalIdentifierURI',
                                                             blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpatialReferenceExternalIdentifiers'


class Spatialreferences(models.Model):
    spatialreferenceid = models.IntegerField(db_column='SpatialReferenceID',
                                             primary_key=True)  # Field name made lowercase.
    srscode = models.TextField(db_column='SRSCode', blank=True)  # Field name made lowercase.
    srsname = models.TextField(db_column='SRSName')  # Field name made lowercase.
    srsdescription = models.TextField(db_column='SRSDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpatialReferences'


class Specimenbatchpostions(models.Model):
    featureactionid = models.ForeignKey(Featureactions, db_column='FeatureActionID',
                                        primary_key=True)  # Field name made lowercase.
    batchpositionnumber = models.IntegerField(db_column='BatchPositionNumber')  # Field name made lowercase.
    batchpositionlabel = models.TextField(db_column='BatchPositionLabel', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecimenBatchPostions'


class Specimentaxonomicclassifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Specimens', db_column='SamplingFeatureID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers',
                                              db_column='TaxonomicClassifierID')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecimenTaxonomicClassifiers'


class Specimens(models.Model):
    samplingfeatureid = models.ForeignKey(Samplingfeatures, db_column='SamplingFeatureID',
                                          primary_key=True)  # Field name made lowercase.
    specimentypecv = models.TextField(db_column='SpecimenTypeCV')  # Field name made lowercase.
    specimenmediumcv = models.TextField(db_column='SpecimenMediumCV')  # Field name made lowercase.
    isfieldspecimen = models.BooleanField(db_column='IsFieldSpecimen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specimens'


class Spectraresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Spectraresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpectraResultValueAnnotations'


class Spectraresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Spectraresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    excitationwavelength = models.FloatField(db_column='ExcitationWavelength')  # Field name made lowercase.
    emissionwavelength = models.FloatField(db_column='EmissionWavelength')  # Field name made lowercase.
    wavelengthunitsid = models.ForeignKey('Units', related_name='spectralresultsvalues_wavelengthunitsid', db_column='WavelengthUnitsID')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpectraResultValues'


class Spectraresults(models.Model):
    resultid = models.ForeignKey(Results, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='spectralresults_xlocationunitsid', db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='spectralresults_zlocationunitsid', db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(Spatialreferences, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedwavelengthspacing = models.FloatField(db_column='IntendedWavelengthSpacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedwavelengthspacingunitsid = models.ForeignKey('Units', related_name='spectralresult_intendedwavelengthspacingunitsid', db_column='IntendedWavelengthSpacingUnitsID',
                                                         blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpectraResults'


class Taxonomicclassifierexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers',
                                              db_column='TaxonomicClassifierID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    taxonomicclassifierexternalidentifier = models.TextField(
        db_column='TaxonomicClassifierExternalIdentifier')  # Field name made lowercase.
    taxonomicclassifierexternalidentifieruri = models.TextField(db_column='TaxonomicClassifierExternalIdentifierURI',
                                                                blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxonomicClassifierExternalIdentifiers'


class Taxonomicclassifiers(models.Model):
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
        managed = False
        db_table = 'TaxonomicClassifiers'


class Timeseriesresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Timeseriesresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResultValueAnnotations'


class Timeseriesresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Timeseriesresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    censorcodecv = models.TextField(db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResultValues'


class Timeseriesresults(models.Model):
    resultid = models.ForeignKey(Results, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_xlocationunits', db_column='XLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_ylocationunits', db_column='YLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_zlocationunits', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(Spatialreferences, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='timeseriesresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResults'


class Trajectoryresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Trajectoryresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrajectoryResultValueAnnotations'


class Trajectoryresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Trajectoryresults', db_column='ResultID')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='XLocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_xlocationunitsid', db_column='XLocationUnitsID')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='YLocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_ylocationunitsid', db_column='YLocationUnitsID')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units',  related_name='trajectoryresultvalues_zlocationunitsid', db_column='ZLocationUnitsID')  # Field name made lowercase.
    trajectorydistance = models.FloatField(db_column='TrajectoryDistance')  # Field name made lowercase.
    trajectorydistanceaggregationinterval = models.FloatField(
        db_column='TrajectoryDistanceAggregationInterval')  # Field name made lowercase.
    trajectorydistanceunitsid = models.IntegerField(db_column='TrajectoryDistanceUnitsID')  # Field name made lowercase.
    censorcode = models.TextField(db_column='CensorCode')  # Field name made lowercase.
    qualitycodecv = models.TextField(db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='TimeAggregationInterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',  related_name='trajectoryresultvalues_timeaggregationintervalunitsid',
                                                       db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrajectoryResultValues'


class Trajectoryresults(models.Model):
    resultid = models.ForeignKey(Results, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(Spatialreferences, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtrajectoryspacing = models.FloatField(db_column='IntendedTrajectorySpacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedtrajectoryspacingunitsid = models.ForeignKey('Units', related_name='trajectoryresults_intendedtrajectoryspacingunitsid', db_column='IntendedTrajectorySpacingUnitsID',
                                                         blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='trajectoryresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrajectoryResults'


class Transectresultvalueannotations(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Transectresultvalues', db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransectResultValueAnnotations'


class Transectresultvalues(models.Model):
    valueid = models.BigIntegerField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Transectresults', db_column='ResultID')  # Field name made lowercase.
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
        managed = False
        db_table = 'TransectResultValues'


class Transectresults(models.Model):
    resultid = models.ForeignKey(Results, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='transectresults_zlocationunitsid', db_column='ZLocationUnitsID', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(Spatialreferences, db_column='SpatialReferenceID', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtransectspacing = models.FloatField(db_column='IntendedTransectSpacing', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtransectspacingunitsid = models.ForeignKey('Units', db_column='IntendedTransectSpacingUnitsID', blank=True,
                                                       null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='IntendedTimeSpacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='transectresults_intendedtimespacingunitsid', db_column='IntendedTimeSpacingUnitsID', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.TextField(db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransectResults'


class Units(models.Model):
    unitsid = models.IntegerField(db_column='UnitsID', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.TextField(db_column='UnitsTypeCV')  # Field name made lowercase.
    unitsabbreviation = models.TextField(db_column='UnitsAbbreviation')  # Field name made lowercase.
    unitsname = models.TextField(db_column='UnitsName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'


class Variableextensionpropertyvalues(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', db_column='VariableID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariableExtensionPropertyValues'


class Variableexternalidentifiers(models.Model):
    bridgeid = models.IntegerField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', db_column='VariableID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems,
                                                   db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    variableexternalidentifer = models.TextField(db_column='VariableExternalIdentifer')  # Field name made lowercase.
    variableexternalidentifieruri = models.TextField(db_column='VariableExternalIdentifierURI',
                                                     blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariableExternalIdentifiers'


class Variables(models.Model):
    variableid = models.IntegerField(db_column='VariableID', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.TextField(db_column='VariableTypeCV')  # Field name made lowercase.
    variablecode = models.TextField(db_column='VariableCode')  # Field name made lowercase.
    variablenamecv = models.TextField(db_column='VariableNameCV')  # Field name made lowercase.
    variabledefinition = models.TextField(db_column='VariableDefinition', blank=True)  # Field name made lowercase.
    speciationcv = models.TextField(db_column='SpeciationCV', blank=True)  # Field name made lowercase.
    nodatavalue = models.FloatField(db_column='NoDataValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Variables'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'