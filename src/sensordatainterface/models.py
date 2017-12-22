from __future__ import unicode_literals

import inspect
import uuid

import sys
from django.db import models
from django.conf import settings

# Create your models here.


class ActionAnnotation(models.Model):
    bridgeid = models.AutoField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='actionid')  # Field name made lowercase.
    annotationid = models.ForeignKey('Annotation', db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionannotations'


class ActionBy(models.Model):
    bridgeid = models.AutoField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', related_name="actionby", db_column='actionid')  # Field name made lowercase.
    affiliationid = models.ForeignKey('Affiliation', db_column='affiliationid')  # Field name made lowercase.
    isactionlead = models.BooleanField(
        db_column='isactionlead', default=None)  # , default=False)  # Field name made lowercase. <- How to fix Warnings
    roledescription = models.TextField(db_column='roledescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionby'


class ActionDirective(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='actionid')  # Field name made lowercase.
    directiveid = models.ForeignKey('Directive', db_column='directiveid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actiondirectives'


class ActionExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Action', db_column='actionid')  # Field name made lowercase.
    propertyid = models.ForeignKey('ExtensionProperties', db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionextensionpropertyvalues'


class Action(models.Model):
    actionid = models.AutoField(db_column='actionid', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.ForeignKey('CvActiontype', db_column='actiontypecv')  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='methodid')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='begindatetime')  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='begindatetimeutcoffset')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='enddatetime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='enddatetimeutcoffset', blank=True,
                                               null=True)  # Field name made lowercase.
    actiondescription = models.TextField(db_column='actiondescription', blank=True)  # Field name made lowercase.
    actionfilelink = models.FileField(db_column='actionfilelink', upload_to='actionfilelinks/%Y/%m/%d',
                                      blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actions'


class Affiliation(models.Model):
    affiliationid = models.AutoField(db_column='affiliationid', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('People', related_name='affiliation',
                                 db_column='personid')  # Field name made lowercase.
    organizationid = models.ForeignKey('Organization', related_name='affiliation', db_column='organizationid',
                                       blank=True,
                                       null=True)  # Field name made lowercase.
    isprimaryorganizationcontact = models.NullBooleanField(
        db_column='isprimaryorganizationcontact', default=None)  # Field name made lowercase.
    affiliationstartdate = models.DateField(db_column='affiliationstartdate')  # Field name made lowercase.
    affiliationenddate = models.DateField(db_column='affiliationenddate', blank=True,
                                          null=True)  # Field name made lowercase.
    primaryphone = models.TextField(db_column='primaryphone', blank=True)  # Field name made lowercase.
    primaryemail = models.TextField(db_column='primaryemail')  # Field name made lowercase.
    primaryaddress = models.TextField(db_column='primaryaddress', blank=True)  # Field name made lowercase.
    personlink = models.TextField(db_column='personlink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'affiliations'


class Annotation(models.Model):
    annotationid = models.AutoField(db_column='annotationid', primary_key=True)  # Field name made lowercase.
    annotationtypecv = models.ForeignKey('CvAnnotationtype', db_column='annotationtypecv')  # Field name made lowercase.
    annotationcode = models.TextField(db_column='annotationcode', blank=True)  # Field name made lowercase.
    annotationtext = models.TextField(db_column='annotationtext')  # Field name made lowercase.
    annotationdatetime = models.DateTimeField(db_column='annotationdatetime', blank=True,
                                              null=True)  # Field name made lowercase.
    annotationutcoffset = models.IntegerField(db_column='annotationutcoffset', blank=True,
                                              null=True)  # Field name made lowercase.
    annotationlink = models.TextField(db_column='annotationlink', blank=True)  # Field name made lowercase.
    annotatorid = models.ForeignKey('People', db_column='annotatorid', blank=True,
                                    null=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='citationid', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'annotations'


class AuthorList(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='citationid')  # Field name made lowercase.
    personid = models.ForeignKey('People', db_column='personid')  # Field name made lowercase.
    authororder = models.IntegerField(db_column='authororder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authorlists'


class CvTerm(models.Model):
    termid = models.IntegerField(db_column='termid', primary_key=True)  # Field name made lowercase.
    term = models.TextField(db_column='term')  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    odmvocabulary = models.TextField(db_column='odmvocabulary')  # Field name made lowercase.
    sourcevocabulary = models.TextField(db_column='sourcevocabulary', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cvterms'


class CalibrationAction(models.Model):
    actionid = models.OneToOneField(Action, related_name='calibrationaction', db_column='actionid',
                                 primary_key=True)  # Field name made lowercase.
    calibrationcheckvalue = models.FloatField(db_column='calibrationcheckvalue', blank=True,
                                              null=True)  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariable',
                                                   db_column='instrumentoutputvariableid')  # Field name made lowercase.
    calibrationequation = models.TextField(db_column='calibrationequation', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationactions'


class CalibrationReferenceEquipment(models.Model):
    bridgeid = models.AutoField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(CalibrationAction, related_name='calibrationreferenceequipment',
                                 db_column='actionid')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipment', db_column='equipmentid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationreferenceequipment'


class CalibrationStandard(models.Model):
    bridgeid = models.AutoField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(CalibrationAction, related_name='calibrationstandard',
                                 db_column='actionid')  # Field name made lowercase.
    referencematerialid = models.ForeignKey('ReferenceMaterial',
                                            db_column='referencematerialid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calibrationstandards'


class CategoricalResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('CategoricalResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresultvalueannotations'


class CategoricalResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('CategoricalResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.TextField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresultvalues'


class CategoricalResult(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='xlocationunitsid', blank=True,
                                           null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='ylocationunitsid', blank=True,
                                           null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.IntegerField(db_column='zlocationunitsid', blank=True,
                                           null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoricalresults'


class CitationExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='citationid')  # Field name made lowercase.
    propertyid = models.ForeignKey('ExtensionProperties', db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citationextensionpropertyvalues'


class CitationExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citation', db_column='citationid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey('ExternalIdentifierSystem',
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    citationexternalidentifer = models.TextField(db_column='citationexternalidentifer')  # Field name made lowercase.
    citationexternalidentiferuri = models.TextField(db_column='citationexternalidentiferuri',
                                                    blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citationexternalidentifiers'


class Citation(models.Model):
    citationid = models.IntegerField(db_column='citationid', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='title')  # Field name made lowercase.
    publisher = models.TextField(db_column='publisher')  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='publicationyear')  # Field name made lowercase.
    citationlink = models.TextField(db_column='citationlink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citations'


class DataloggerFile(models.Model):
    dataloggerfileid = models.AutoField(db_column='dataloggerfileid', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('DataloggerProgramFile', db_column='programid')  # Field name made lowercase.
    dataloggerfilename = models.TextField(db_column='dataloggerfilename')  # Field name made lowercase.
    dataloggerfiledescription = models.TextField(db_column='dataloggerfiledescription',
                                                 blank=True)  # Field name made lowercase.
    dataloggerfilelink = models.TextField(db_column='dataloggerfilelink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerfiles'


class DataQuality(models.Model):
    dataqualityid = models.IntegerField(db_column='dataqualityid', primary_key=True)  # Field name made lowercase.
    dataqualitytypecv = models.ForeignKey('CvDataqualitytype', db_column='dataqualitytypecv')  # Field name made lowercase.
    dataqualitycode = models.TextField(db_column='dataqualitycode')  # Field name made lowercase.
    dataqualityvalue = models.FloatField(db_column='dataqualityvalue', blank=True,
                                         null=True)  # Field name made lowercase.
    dataqualityvalueunitsid = models.ForeignKey('Units', db_column='dataqualityvalueunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    dataqualitydescription = models.TextField(db_column='dataqualitydescription',
                                              blank=True)  # Field name made lowercase.
    dataqualitylink = models.TextField(db_column='dataqualitylink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataquality'


class DatasetCitation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey('Dataset', db_column='datasetid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='citationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasetcitations'


class Dataset(models.Model):
    datasetid = models.IntegerField(db_column='datasetid', primary_key=True)  # Field name made lowercase.
    datasetuuid = models.TextField(db_column='datasetuuid')  # Field name made lowercase.
    datasettypecv = models.ForeignKey('CvDatasettype', db_column='datasettypecv')  # Field name made lowercase.
    datasetcode = models.TextField(db_column='datasetcode')  # Field name made lowercase.
    datasettitle = models.TextField(db_column='datasettitle')  # Field name made lowercase.
    datasetabstract = models.TextField(db_column='datasetabstract')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasets'


class DatasetsResult(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Dataset, db_column='datasetid')  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='resultid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasetsresults'


class DataloggerFileColumn(models.Model):
    dataloggerfilecolumnid = models.AutoField(db_column='dataloggerfilecolumnid',
                                              primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='resultid', blank=True, null=True)  # Field name made lowercase.
    dataloggerfileid = models.ForeignKey(DataloggerFile, related_name='dataloggerfilecolumn',
                                         db_column='dataloggerfileid')  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariable', related_name='dataloggerfilecolumn',
                                                   db_column='instrumentoutputvariableid')  # Field name made lowercase.
    columnlabel = models.TextField(db_column='columnlabel')  # Field name made lowercase.
    columndescription = models.TextField(db_column='columndescription', blank=True)  # Field name made lowercase.
    measurementequation = models.TextField(db_column='measurementequation', blank=True)  # Field name made lowercase.
    scaninterval = models.FloatField(db_column='scaninterval', blank=True, null=True)  # Field name made lowercase.
    scanintervalunitsid = models.ForeignKey('Units', db_column='scanintervalunitsid', blank=True,
                                            null=True)  # Field name made lowercase.
    recordinginterval = models.FloatField(db_column='recordinginterval', blank=True,
                                          null=True)  # Field name made lowercase.
    recordingintervalunitsid = models.ForeignKey('Units', related_name='column_recordingintervalunitsid',
                                                 db_column='recordingintervalunitsid', blank=True,
                                                 null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv',
                                              blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerfilecolumns'


class DataloggerProgramFile(models.Model):
    programid = models.AutoField(db_column='programid', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')  # Field name made lowercase.
    programname = models.TextField(db_column='programname')  # Field name made lowercase.
    programdescription = models.TextField(db_column='programdescription', blank=True)  # Field name made lowercase.
    programversion = models.TextField(db_column='programversion', blank=True)  # Field name made lowercase.
    programfilelink = models.TextField(db_column='programfilelink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataloggerprogramfiles'


class DerivationEquation(models.Model):
    derivationequationid = models.IntegerField(db_column='derivationequationid',
                                               primary_key=True)  # Field name made lowercase.
    derivationequation = models.TextField(db_column='derivationequation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'derivationequations'


class Directive(models.Model):
    directiveid = models.IntegerField(db_column='directiveid', primary_key=True)  # Field name made lowercase.
    directivetypecv = models.ForeignKey('CvDirectivetype', db_column='directivetypecv')  # Field name made lowercase.
    directivedescription = models.TextField(db_column='directivedescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'directives'


class Equipment(models.Model):
    equipmentid = models.AutoField(db_column='equipmentid', primary_key=True)  # Field name made lowercase.
    equipmentcode = models.TextField(db_column='equipmentcode')  # Field name made lowercase.
    equipmentname = models.TextField(db_column='equipmentname')  # Field name made lowercase.
    equipmenttypecv = models.ForeignKey('CvEquipmenttype', db_column='equipmenttypecv')  # Field name made lowercase.
    equipmentmodelid = models.ForeignKey('EquipmentModel', related_name='equipment',
                                         db_column='equipmentmodelid')  # Field name made lowercase.
    equipmentserialnumber = models.TextField(db_column='equipmentserialnumber')  # Field name made lowercase.
    equipmentownerid = models.ForeignKey('People', db_column='equipmentownerid')  # Field name made lowercase.
    equipmentvendorid = models.ForeignKey('Organization', related_name='equipment',
                                          db_column='equipmentvendorid')  # Field name made lowercase.
    equipmentpurchasedate = models.DateTimeField(db_column='equipmentpurchasedate')  # Field name made lowercase.
    equipmentpurchaseordernumber = models.TextField(db_column='equipmentpurchaseordernumber',
                                                    blank=True)  # Field name made lowercase.
    equipmentdescription = models.TextField(db_column='equipmentdescription', blank=True)  # Field name made lowercase.
    equipmentdocumentationlink = models.FileField(db_column='equipmentdocumentationlink', upload_to='equipmentdocumentation',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipment'


class EquipmentAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, db_column='equipmentid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipmentannotations'


class EquipmentModel(models.Model):
    equipmentmodelid = models.AutoField(db_column='equipmentmodelid', primary_key=True)  # Field name made lowercase.
    modelmanufacturerid = models.ForeignKey('Organization',
                                            db_column='modelmanufacturerid')  # Field name made lowercase.
    modelpartnumber = models.TextField(db_column='modelpartnumber', blank=True)  # Field name made lowercase.
    modelname = models.TextField(db_column='modelname')  # Field name made lowercase.
    modeldescription = models.TextField(db_column='modeldescription', blank=True)  # Field name made lowercase.
    isinstrument = models.BooleanField(db_column='isinstrument', default=None)  # Field name made lowercase.

    modelspecificationsfilelink = models.FileField(db_column='modelspecificationsfilelink',
                                                   upload_to='modelspecifications', blank=True)

    modellink = models.TextField(db_column='modellink', blank=True)  # Field name made lowercase.

    def natural_key(self):
        return self.modelname

    class Meta:
        managed = False
        db_table = 'equipmentmodels'


class EquipmentUsed(models.Model):
    bridgeid = models.AutoField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name='equipmentused',
                                 db_column='actionid')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, related_name='equipmentused',
                                    db_column='equipmentid', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipmentused'


class ExtensionProperties(models.Model):
    propertyid = models.IntegerField(db_column='propertyid', primary_key=True)  # Field name made lowercase.
    propertyname = models.TextField(db_column='propertyname')  # Field name made lowercase.
    propertydescription = models.TextField(db_column='propertydescription', blank=True)  # Field name made lowercase.
    propertydatatypecv = models.ForeignKey('CvPropertydatatype', db_column='propertydatatypecv')  # Field name made lowercase.
    propertyunitsid = models.ForeignKey('Units', db_column='propertyunitsid', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extensionproperties'


class ExternalIdentifierSystem(models.Model):
    externalidentifiersystemid = models.IntegerField(db_column='externalidentifiersystemid',
                                                     primary_key=True)  # Field name made lowercase.
    externalidentifiersystemname = models.TextField(
        db_column='externalidentifiersystemname')  # Field name made lowercase.
    identifiersystemorganizationid = models.ForeignKey('Organization',
                                                       db_column='identifiersystemorganizationid')  # Field name made lowercase.
    externalidentifiersystemdescription = models.TextField(db_column='externalidentifiersystemdescription',
                                                           blank=True)  # Field name made lowercase.
    externalidentifiersystemurl = models.TextField(db_column='externalidentifiersystemurl',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'externalidentifiersystems'


class FeatureAction(models.Model):
    featureactionid = models.AutoField(db_column='featureactionid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature', related_name="featureaction",
                                          db_column='samplingfeatureid')  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name="featureaction",
                                 db_column='actionid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'featureactions'


class InstrumentOutputVariable(models.Model):
    instrumentoutputvariableid = models.AutoField(db_column='instrumentoutputvariableid',
                                                  primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(EquipmentModel, related_name='instrumentoutputvariable',
                                db_column='modelid')  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', related_name='instrumentoutputvariable',
                                   db_column='variableid')  # Field name made lowercase.
    instrumentmethodid = models.ForeignKey('Method', db_column='instrumentmethodid')  # Field name made lowercase.
    instrumentresolution = models.TextField(db_column='instrumentresolution', blank=True)  # Field name made lowercase.
    instrumentaccuracy = models.TextField(db_column='instrumentaccuracy', blank=True)  # Field name made lowercase.
    instrumentrawoutputunitsid = models.ForeignKey('Units',
                                                   db_column='instrumentrawoutputunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instrumentoutputvariables'


class MaintenanceAction(models.Model):
    actionid = models.OneToOneField(Action, db_column='actionid', related_name='maintenanceaction',
                                 primary_key=True)  # Field name made lowercase.
    isfactoryservice = models.BooleanField(db_column='isfactoryservice', default=None)  # Field name made lowercase.
    maintenancecode = models.TextField(db_column='maintenancecode', blank=True)  # Field name made lowercase.
    maintenancereason = models.TextField(db_column='maintenancereason', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maintenanceactions'


class MeasurementResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('MeasurementResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurementresultvalueannotations'


class MeasurementResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('MeasurementResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'measurementresultvalues'


class MeasurementResult(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='measurement_xlocationunitsid',
                                         db_column='xlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='measurement_ylocationunitsid',
                                         db_column='ylocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    db_table = 'measurementresults'


class MethodAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='methodid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodannotations'


class MethodCitation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='methodid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='citationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodcitations'


class MethodExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='methodid')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodextensionpropertyvalues'


class MethodExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', db_column='methodid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    methodexternalidentifier = models.TextField(db_column='methodexternalidentifier')  # Field name made lowercase.
    methodexternalidentifieruri = models.TextField(db_column='methodexternalidentifieruri',
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methodexternalidentifiers'


class Method(models.Model):
    methodid = models.AutoField(db_column='methodid', primary_key=True)  # Field name made lowercase.
    methodtypecv = models.ForeignKey('CvMethodtype', db_column='methodtypecv')  # Field name made lowercase.
    methodcode = models.TextField(db_column='methodcode')  # Field name made lowercase.
    methodname = models.TextField(db_column='methodname')  # Field name made lowercase.
    methoddescription = models.TextField(db_column='methoddescription', blank=True)  # Field name made lowercase.
    methodlink = models.TextField(db_column='methodlink', blank=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Organization', db_column='organizationid', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'methods'


class ModelAffiliation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey('Models', db_column='modelid')  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliation, db_column='affiliationid')  # Field name made lowercase.
    isprimary = models.BooleanField(db_column='isprimary', default=None)  # Field name made lowercase.
    roledescription = models.TextField(db_column='roledescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modelaffiliations'


class Models(models.Model):
    modelid = models.IntegerField(db_column='modelid', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(db_column='modelcode', max_length=255)  # Field name made lowercase.
    modelname = models.CharField(db_column='modelname', max_length=255)  # Field name made lowercase.
    modeldescription = models.CharField(db_column='modeldescription', max_length=500,
                                        blank=True)  # Field name made lowercase.
    version = models.TextField(db_column='version', blank=True)  # Field name made lowercase.
    modellink = models.TextField(db_column='modellink', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'models'


class Organization(models.Model):
    organizationid = models.AutoField(db_column='organizationid', primary_key=True)  # Field name made lowercase.
    organizationtypecv = models.ForeignKey('CvOrganizationtype', db_column='organizationtypecv')  # Field name made lowercase.
    organizationcode = models.TextField(db_column='organizationcode')  # Field name made lowercase.
    organizationname = models.TextField(db_column='organizationname')  # Field name made lowercase.
    organizationdescription = models.TextField(db_column='organizationdescription',
                                               blank=True)  # Field name made lowercase.
    organizationlink = models.TextField(db_column='organizationlink', blank=True)  # Field name made lowercase.
    parentorganizationid = models.ForeignKey('self', db_column='parentorganizationid', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organizations'

    def __str__(self):
        return self.organizationname

    def __unicode__(self):
        return self.organizationname


class People(models.Model):
    personid = models.AutoField(db_column='personid', primary_key=True)  # Field name made lowercase.
    personfirstname = models.TextField(db_column='personfirstname')  # Field name made lowercase.
    personmiddlename = models.TextField(db_column='personmiddlename', blank=True)  # Field name made lowercase.
    personlastname = models.TextField(db_column='personlastname')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'


class PersonExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(People, db_column='personid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    personexternalidentifier = models.TextField(db_column='personexternalidentifier')  # Field name made lowercase.
    personexternalidenifieruri = models.TextField(db_column='personexternalidenifieruri',
                                                  blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personexternalidentifiers'


class PointCoverageResultValueAnnotation(models.Model):
    bridgeid = models.BigIntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('PointCoverageResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalueannotations'


class PointCoverageResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('PointCoverageResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.BigIntegerField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='point_xlocationunitsid',
                                         db_column='xlocationunitsid')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='point_ylocationunitsid',
                                         db_column='ylocationunitsid')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalues'


class PointCoverageResult(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='zlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='intendedxspacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='point_intendedxspacingunitsid',
                                                db_column='intendedxspacingunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedyspacing = models.FloatField(db_column='intendedyspacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedyspacingunitsid = models.ForeignKey('Units', related_name='point_intendedyspacingunitsid',
                                                db_column='intendedyspacingunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(
        db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pointcoverageresults'


class ProcessingLevel(models.Model):
    processinglevelid = models.IntegerField(db_column='processinglevelid',
                                            primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.TextField(db_column='processinglevelcode')  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    explanation = models.TextField(db_column='explanation', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'processinglevels'


class ProfileResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('ProfileResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresultvalueannotations'


class ProfileResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('ProfileResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='zaggregationinterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='zlocationunitsid')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='profile_timeaggregationintervalunitsid',
                                                       db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresultvalues'


class ProfileResult(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='profile_xlocationunitsid', db_column='xlocationunitsid',
                                         blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='profile_ylocationunitsid', db_column='ylocationunitsid',
                                         blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='intendedzspacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', db_column='intendedzspacingunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='intendedtimespacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='profile_intendedtimespacingunitsid',
                                                   db_column='intendedtimespacingunitsid', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profileresults'


class ReferenceMaterialExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('ReferenceMaterial',
                                            db_column='referencematerialid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    referencematerialexternalidentifier = models.TextField(
        db_column='referencematerialexternalidentifier')  # Field name made lowercase.
    referencematerialexternalidentifieruri = models.TextField(db_column='referencematerialexternalidentifieruri',
                                                              blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerialexternalidentifiers'


class ReferenceMaterialValue(models.Model):
    # TODO: Change database table to identity and update here.
    referencematerialvalueid = models.IntegerField(db_column='referencematerialvalueid',
                                                   primary_key=True)
    referencematerialid = models.ForeignKey('ReferenceMaterial', related_name='referencematerialvalue',
                                            db_column='referencematerialid')  # Field name made lowercase.
    referencematerialvalue = models.FloatField(db_column='referencematerialvalue')  # Field name made lowercase.
    referencematerialaccuracy = models.FloatField(db_column='referencematerialaccuracy', blank=True,
                                                  null=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='variableid')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='unitsid')  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, db_column='citationid', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerialvalues'


class ReferenceMaterial(models.Model):
    # TODO: Change database table to identity and update here.
    referencematerialid = models.IntegerField(db_column='referencematerialid',
                                           primary_key=True)  # Field name made lowercase.
    referencematerialmediumcv = models.ForeignKey('CvMedium', db_column='referencematerialmediumcv')  # Field name made lowercase.
    referencematerialorganizationid = models.ForeignKey(Organization,
                                                        db_column='referencematerialorganizationid')  # Field name made lowercase.
    referencematerialcode = models.TextField(db_column='referencematerialcode')  # Field name made lowercase.
    referencemateriallotcode = models.TextField(db_column='referencemateriallotcode',
                                                blank=True)  # Field name made lowercase.
    referencematerialpurchasedate = models.DateTimeField(db_column='referencematerialpurchasedate', blank=True,
                                                         null=True)  # Field name made lowercase.
    referencematerialexpirationdate = models.DateTimeField(db_column='referencematerialexpirationdate', blank=True,
                                                           null=True)  # Field name made lowercase.
    referencematerialcertificatelink = models.FileField(db_column='referencematerialcertificatelink',
                                                        blank=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature', db_column='samplingfeatureid', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencematerials'


class RelatedAction(models.Model):
    relationid = models.AutoField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Action, related_name='relatedaction',
                                 db_column='actionid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedactionid = models.ForeignKey(Action, related_name='parent_relatedaction',
                                        db_column='relatedactionid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedactions'


class RelatedAnnotation(models.Model):
    relationid = models.IntegerField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, related_name='relatedannonations_annotationid',
                                     db_column='annotationid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedannotationid = models.ForeignKey(Annotation, related_name='relatedannotation_relatedannontationid',
                                            db_column='relatedannotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedannotations'


class RelatedCitation(models.Model):
    relationid = models.IntegerField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey(Citation, related_name='relatedcitations_citationid',
                                   db_column='citationid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedcitationid = models.ForeignKey(Citation, related_name='relatedcitations_relatedcitationid',
                                          db_column='relatedcitationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedcitations'


class RelatedDataset(models.Model):
    relationid = models.IntegerField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Dataset, related_name='relateddatasets_datasetid',
                                  db_column='datasetid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relateddatasetid = models.ForeignKey(Dataset, related_name='relateddatasets_relateddatasetid',
                                         db_column='relateddatasetid')  # Field name made lowercase.
    versioncode = models.TextField(db_column='versioncode', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relateddatasets'


class RelatedEquipment(models.Model):
    relationid = models.AutoField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_equipmentid',
                                    db_column='equipmentid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedequipmentid = models.ForeignKey(Equipment, related_name='relatedequipment_relatedequipmentid',
                                           db_column='relatedequipmentid')  # Field name made lowercase.
    relationshipstartdatetime = models.DateTimeField(
        db_column='relationshipstartdatetime')  # Field name made lowercase.
    relationshipstartdatetimeutcoffset = models.IntegerField(
        db_column='relationshipstartdatetimeutcoffset')  # Field name made lowercase.
    relationshipenddatetime = models.DateTimeField(db_column='relationshipenddatetime', blank=True,
                                                   null=True)  # Field name made lowercase.
    relationshipenddatetimeutcoffset = models.IntegerField(db_column='relationshipenddatetimeutcoffset', blank=True,
                                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedequipment'


class RelatedFeatures(models.Model):
    relationid = models.IntegerField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          related_name='relatedfeatures_samplingfeatureid',
                                          db_column='samplingfeatureid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedfeatureid = models.ForeignKey('SamplingFeature', related_name='relatedfeature_relatedfeatureid',
                                         db_column='relatedfeatureid')  # Field name made lowercase.
    spatialoffsetid = models.ForeignKey('SpatialOffsets', db_column='spatialoffsetid', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedfeatures'


class RelatedModel(models.Model):
    relatedid = models.IntegerField(db_column='relatedid', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, db_column='modelid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv', max_length=1)  # Field name made lowercase.
    relatedmodelid = models.BigIntegerField(db_column='relatedmodelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedmodels'


class RelatedResult(models.Model):
    relationid = models.IntegerField(db_column='relationid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='resultid')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey('CvRelationshiptype', db_column='relationshiptypecv')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Result', related_name='relatedresults_relatedresultid',
                                        db_column='relatedresultid')  # Field name made lowercase.
    versioncode = models.TextField(db_column='versioncode', blank=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='relatedresultsequencenumber', blank=True,
                                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatedresults'


class ResultAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='resultid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='begindatetime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='enddatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultannotations'


class ResultDerivationEquation(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(DerivationEquation,
                                             db_column='derivationequationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultderivationequations'


class ResultExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Result', db_column='resultid')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultextensionpropertyvalues'


class ResultNormalizationValue(models.Model):
    resultid = models.OneToOneField('Result', db_column='resultid', primary_key=True)  # Field name made lowercase.
    normalizedbyreferencematerialvalueid = models.ForeignKey(ReferenceMaterialValue,
                                                             db_column='normalizedbyreferencematerialvalueid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultnormalizationvalues'


class Result(models.Model):
    resultid = models.AutoField(db_column='resultid', primary_key=True)  # Field name made lowercase.
    resultuuid = models.TextField(db_column='resultuuid', default=uuid.uuid4)  # Field name made lowercase.
    featureactionid = models.ForeignKey(FeatureAction, db_column='featureactionid')  # Field name made lowercase.
    resulttypecv = models.ForeignKey('CvResulttype', db_column='resulttypecv')  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='variableid')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', db_column='unitsid')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier', db_column='taxonomicclassifierid', blank=True,
                                              null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey(ProcessingLevel, db_column='processinglevelid')  # Field name made lowercase.
    resultdatetime = models.DateTimeField(db_column='resultdatetime', blank=True,
                                          null=True)  # Field name made lowercase.
    resultdatetimeutcoffset = models.BigIntegerField(db_column='resultdatetimeutcoffset', blank=True,
                                                     null=True)  # Field name made lowercase.
    validdatetime = models.DateTimeField(db_column='validdatetime', blank=True, null=True)  # Field name made lowercase.
    validdatetimeutcoffset = models.BigIntegerField(db_column='validdatetimeutcoffset', blank=True,
                                                    null=True)  # Field name made lowercase.
    statuscv = models.ForeignKey('CvStatus', db_column='statuscv', blank=True)  # Field name made lowercase.
    sampledmediumcv = models.ForeignKey('CvMedium', db_column='sampledmediumcv')  # Field name made lowercase.
    valuecount = models.IntegerField(db_column='valuecount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'results'


class ResultsDataQuality(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Result, db_column='resultid')  # Field name made lowercase.
    dataqualityid = models.ForeignKey(DataQuality, db_column='dataqualityid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resultsdataquality'


class SamplingFeatureAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='samplingfeatureid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureannotations'


class SamplingFeatureExtPropertyVal(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='samplingfeatureid')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureextensionpropertyvalues'


class SamplingFeatureExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('SamplingFeature',
                                          db_column='samplingfeatureid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    samplingfeatureexternalidentifier = models.TextField(
        db_column='samplingfeatureexternalidentifier')  # Field name made lowercase.
    samplingfeatureexternalidentiferuri = models.TextField(db_column='samplingfeatureexternalidentiferuri',
                                                           blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatureexternalidentifiers'


class SamplingFeature(models.Model):
    samplingfeatureid = models.AutoField(db_column='samplingfeatureid',
                                         primary_key=True)  # Field name made lowercase.
    samplingfeaturetypecv = models.ForeignKey('CvSamplingfeaturetype', db_column='samplingfeaturetypecv')  # Field name made lowercase.
    samplingfeaturecode = models.TextField(db_column='samplingfeaturecode')  # Field name made lowercase.
    samplingfeaturename = models.TextField(db_column='samplingfeaturename', blank=True)  # Field name made lowercase.
    samplingfeaturedescription = models.TextField(db_column='samplingfeaturedescription',
                                                  blank=True)  # Field name made lowercase.
    samplingfeaturegeotypecv = models.ForeignKey('CvSamplingfeaturegeotype', db_column='samplingfeaturegeotypecv',
                                                blank=True, null=True)  # Field name made lowercase.
    elevation_m = models.FloatField(db_column='elevation_m', blank=True, null=True)  # Field name made lowercase.
    elevationdatumcv = models.ForeignKey('CvElevationdatum', db_column='elevationdatumcv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplingfeatures'


class SectionResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('SectionResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresultvalueannotations'


class SectionResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('SectionResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.BigIntegerField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.BigIntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation')  # Field name made lowercase.
    xaggregationinterval = models.FloatField(db_column='xaggregationinterval')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_xlocationunitsid',
                                         db_column='xlocationunitsid')  # Field name made lowercase.
    zlocation = models.BigIntegerField(db_column='zlocation')  # Field name made lowercase.
    zaggregationinterval = models.FloatField(db_column='zaggregationinterval')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='sectionresults_zlocationunitsid',
                                         db_column='zlocationunitsid')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='sectionresults_timeaggregationintervalunitsid',
                                                       db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresultvalues'


class SectionResult(models.Model):
    resultid = models.OneToOneField(Result, db_column='resultid', primary_key=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='sectionresults_ylocationunitsid',
                                         db_column='ylocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference', db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedxspacing = models.FloatField(db_column='intendedxspacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedxspacingunitsid',
                                                db_column='intendedxspacingunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedzspacing = models.FloatField(db_column='intendedzspacing', blank=True,
                                         null=True)  # Field name made lowercase.
    intendedzspacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedzspacingunitsid',
                                                db_column='intendedzspacingunitsid', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='intendedtimespacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='sectionresults_intendedtimespacingunitsid',
                                                   db_column='intendedtimespacingunitsid', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionresults'


class Simulation(models.Model):
    simulationid = models.IntegerField(db_column='simulationid', primary_key=True)  # Field name made lowercase.
    actionid = models.BigIntegerField(db_column='actionid')  # Field name made lowercase.
    simulationname = models.CharField(db_column='simulationname', max_length=255)  # Field name made lowercase.
    simulationdescription = models.CharField(db_column='simulationdescription', max_length=500,
                                             blank=True)  # Field name made lowercase.
    simulationstartdatetime = models.DateTimeField(db_column='simulationstartdatetime')  # Field name made lowercase.
    simulationstartdatetimeutcoffset = models.IntegerField(
        db_column='simulationstartdatetimeutcoffset')  # Field name made lowercase.
    simulationenddatetime = models.DateTimeField(db_column='simulationenddatetime')  # Field name made lowercase.
    simulationenddatetimeutcoffset = models.IntegerField(
        db_column='simulationenddatetimeutcoffset')  # Field name made lowercase.
    timestepvalue = models.FloatField(db_column='timestepvalue')  # Field name made lowercase.
    timestepunitsid = models.BigIntegerField(db_column='timestepunitsid')  # Field name made lowercase.
    inputdatasetid = models.BigIntegerField(db_column='inputdatasetid', blank=True,
                                            null=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, db_column='modelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'simulations'


class Sites(models.Model):
    samplingfeatureid = models.OneToOneField(SamplingFeature, related_name='sites',
                                          db_column='samplingfeatureid',
                                          primary_key=True)  # Field name made lowercase.
    sitetypecv = models.ForeignKey('CvSitetype', db_column='sitetypecv')  # Field name made lowercase.
    latitude = models.FloatField(db_column='latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='longitude')  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference',
                                           db_column='spatialreferenceid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sites'


class SpatialOffsets(models.Model):
    spatialoffsetid = models.IntegerField(db_column='spatialoffsetid', primary_key=True)  # Field name made lowercase.
    spatialoffsettypecv = models.ForeignKey('CvSpatialoffsettype', db_column='spatialoffsettypecv')  # Field name made lowercase.
    offset1value = models.FloatField(db_column='offset1value')  # Field name made lowercase.
    offset1unitid = models.IntegerField(db_column='offset1unitid')  # Field name made lowercase.
    offset2value = models.FloatField(db_column='offset2value', blank=True, null=True)  # Field name made lowercase.
    offset2unitid = models.IntegerField(db_column='offset2unitid', blank=True, null=True)  # Field name made lowercase.
    offset3value = models.FloatField(db_column='offset3value', blank=True, null=True)  # Field name made lowercase.
    offset3unitid = models.IntegerField(db_column='offset3unitid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialoffsets'


class SpatialReferenceExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('SpatialReference',
                                           db_column='spatialreferenceid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    spatialreferenceexternalidentifier = models.TextField(
        db_column='spatialreferenceexternalidentifier')  # Field name made lowercase.
    spatialreferenceexternalidentifieruri = models.TextField(db_column='spatialreferenceexternalidentifieruri',
                                                             blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spatialreferenceexternalidentifiers'


class SpatialReference(models.Model):
    spatialreferenceid = models.IntegerField(db_column='spatialreferenceid',
                                             primary_key=True)  # Field name made lowercase.
    srscode = models.TextField(db_column='srscode', blank=True)  # Field name made lowercase.
    srsname = models.TextField(db_column='srsname')  # Field name made lowercase.
    srsdescription = models.TextField(db_column='srsdescription', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.srsname

    def __unicode__(self):
        return self.srsname

    class Meta:
        managed = False
        db_table = 'spatialreferences'


class SpecimenBatchPostion(models.Model):
    featureactionid = models.OneToOneField(FeatureAction, db_column='featureactionid',
                                        primary_key=True)  # Field name made lowercase.
    batchpositionnumber = models.IntegerField(db_column='batchpositionnumber')  # Field name made lowercase.
    batchpositionlabel = models.TextField(db_column='batchpositionlabel', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimenbatchpostions'


class SpecimenTaxonomicClassifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Specimens', db_column='samplingfeatureid')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier',
                                              db_column='taxonomicclassifierid')  # Field name made lowercase.
    citationid = models.IntegerField(db_column='citationid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimentaxonomicclassifiers'


class Specimens(models.Model):
    samplingfeatureid = models.OneToOneField(SamplingFeature, db_column='samplingfeatureid',
                                          primary_key=True)  # Field name made lowercase.
    specimentypecv = models.ForeignKey('CvSpecimentype', db_column='specimentypecv')  # Field name made lowercase.
    specimenmediumcv = models.ForeignKey('CvMedium', db_column='specimenmediumcv')  # Field name made lowercase.
    isfieldspecimen = models.BooleanField(db_column='isfieldspecimen', default=None)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimens'


class SpectraResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('SpectraResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresultvalueannotations'


class SpectraResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('SpectraResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    excitationwavelength = models.FloatField(db_column='excitationwavelength')  # Field name made lowercase.
    emissionwavelength = models.FloatField(db_column='emissionwavelength')  # Field name made lowercase.
    wavelengthunitsid = models.ForeignKey('Units', related_name='spectralresultsvalues_wavelengthunitsid',
                                          db_column='wavelengthunitsid')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresultvalues'


class SpectraResult(models.Model):
    resultid = models.OneToOneField(Result, db_column='resultid', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='spectralresults_xlocationunitsid',
                                         db_column='xlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='spectralresults_zlocationunitsid',
                                         db_column='ylocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', db_column='zlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedwavelengthspacing = models.FloatField(db_column='intendedwavelengthspacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedwavelengthspacingunitsid = models.ForeignKey('Units',
                                                         related_name='spectralresult_intendedwavelengthspacingunitsid',
                                                         db_column='intendedwavelengthspacingunitsid',
                                                         blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectraresults'


class TaxonomicClassifierExtId(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifier',
                                              db_column='taxonomicclassifierid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    taxonomicclassifierexternalidentifier = models.TextField(
        db_column='taxonomicclassifierexternalidentifier')  # Field name made lowercase.
    taxonomicclassifierexternalidentifieruri = models.TextField(db_column='taxonomicclassifierexternalidentifieruri',
                                                                blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonomicclassifierexternalidentifiers'


class TaxonomicClassifier(models.Model):
    taxonomicclassifierid = models.IntegerField(db_column='taxonomicclassifierid',
                                                primary_key=True)  # Field name made lowercase.
    taxonomicclassifiertypecv = models.ForeignKey('CvTaxonomicclassifiertype', db_column='taxonomicclassifiertypecv')  # Field name made lowercase.
    taxonomicclassifiername = models.TextField(db_column='taxonomicclassifiername')  # Field name made lowercase.
    taxonomicclassifiercommonname = models.TextField(db_column='taxonomicclassifiercommonname',
                                                     blank=True)  # Field name made lowercase.
    taxonomicclassifierdescription = models.TextField(db_column='taxonomicclassifierdescription',
                                                      blank=True)  # Field name made lowercase.
    parenttaxonomicclassifierid = models.ForeignKey('self', db_column='parenttaxonomicclassifierid', blank=True,
                                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonomicclassifiers'


class TimeSeriesResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TimeSeriesResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalueannotations'


class TimeSeriesResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TimeSeriesResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalues'


class TimeSeriesResult(models.Model):
    resultid = models.OneToOneField(Result, db_column='resultid', primary_key=True)  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation', blank=True, null=True)  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_xlocationunits',
                                         db_column='xlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation', blank=True, null=True)  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_ylocationunits',
                                         db_column='ylocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='timeseriesresults_zlocationunits',
                                         db_column='zlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='intendedtimespacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='timeseriesresults_intendedtimespacingunitsid',
                                                   db_column='intendedtimespacingunitsid', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeseriesresults'


class TrajectoryResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TrajectoryResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalueannotations'


class TrajectoryResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TrajectoryResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation')  # Field name made lowercase.
    xlocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_xlocationunitsid',
                                         db_column='xlocationunitsid')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation')  # Field name made lowercase.
    ylocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_ylocationunitsid',
                                         db_column='ylocationunitsid')  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation')  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='trajectoryresultvalues_zlocationunitsid',
                                         db_column='zlocationunitsid')  # Field name made lowercase.
    trajectorydistance = models.FloatField(db_column='trajectorydistance')  # Field name made lowercase.
    trajectorydistanceaggregationinterval = models.FloatField(
        db_column='trajectorydistanceaggregationinterval')  # Field name made lowercase.
    trajectorydistanceunitsid = models.IntegerField(db_column='trajectorydistanceunitsid')  # Field name made lowercase.
    censorcode = models.TextField(db_column='censorcode')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       related_name='trajectoryresultvalues_timeaggregationintervalunitsid',
                                                       db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalues'


class TrajectoryResult(models.Model):
    resultid = models.OneToOneField(Result, db_column='resultid', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtrajectoryspacing = models.FloatField(db_column='intendedtrajectoryspacing', blank=True,
                                                  null=True)  # Field name made lowercase.
    intendedtrajectoryspacingunitsid = models.ForeignKey('Units',
                                                         related_name='trajectoryresults_intendedtrajectoryspacingunitsid',
                                                         db_column='intendedtrajectoryspacingunitsid',
                                                         blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='intendedtimespacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='trajectoryresults_intendedtimespacingunitsid',
                                                   db_column='intendedtimespacingunitsid', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trajectoryresults'


class TransectResultValueAnnotation(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('TransectResultValue', db_column='valueid')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotation, db_column='annotationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresultvalueannotations'


class TransectResultValue(models.Model):
    valueid = models.BigIntegerField(db_column='valueid', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('TransectResult', db_column='resultid')  # Field name made lowercase.
    datavalue = models.FloatField(db_column='datavalue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='valuedatetime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.DateTimeField(db_column='valuedatetimeutcoffset')  # Field name made lowercase.
    xlocation = models.FloatField(db_column='xlocation')  # Field name made lowercase.
    xlocationunitsid = models.IntegerField(db_column='xlocationunitsid')  # Field name made lowercase.
    ylocation = models.FloatField(db_column='ylocation')  # Field name made lowercase.
    ylocationunitsid = models.IntegerField(db_column='ylocationunitsid')  # Field name made lowercase.
    transectdistance = models.FloatField(db_column='transectdistance')  # Field name made lowercase.
    transectdistanceaggregationinterval = models.FloatField(
        db_column='transectdistanceaggregationinterval')  # Field name made lowercase.
    transectdistanceunitsid = models.IntegerField(db_column='transectdistanceunitsid')  # Field name made lowercase.
    censorcodecv = models.ForeignKey('CvCensorcode', db_column='censorcodecv')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey('CvQualitycode', db_column='qualitycodecv')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.
    timeaggregationinterval = models.FloatField(db_column='timeaggregationinterval')  # Field name made lowercase.
    timeaggregationintervalunitsid = models.IntegerField(
        db_column='timeaggregationintervalunitsid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresultvalues'


class TransectResult(models.Model):
    resultid = models.OneToOneField(Result, db_column='resultid', primary_key=True)  # Field name made lowercase.
    zlocation = models.FloatField(db_column='zlocation', blank=True, null=True)  # Field name made lowercase.
    zlocationunitsid = models.ForeignKey('Units', related_name='transectresults_zlocationunitsid',
                                         db_column='zlocationunitsid', blank=True,
                                         null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(SpatialReference, db_column='spatialreferenceid', blank=True,
                                           null=True)  # Field name made lowercase.
    intendedtransectspacing = models.FloatField(db_column='intendedtransectspacing', blank=True,
                                                null=True)  # Field name made lowercase.
    intendedtransectspacingunitsid = models.ForeignKey('Units', db_column='intendedtransectspacingunitsid', blank=True,
                                                       null=True)  # Field name made lowercase.
    intendedtimespacing = models.FloatField(db_column='intendedtimespacing', blank=True,
                                            null=True)  # Field name made lowercase.
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='transectresults_intendedtimespacingunitsid',
                                                   db_column='intendedtimespacingunitsid', blank=True,
                                                   null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey('CvAggregationstatistic', db_column='aggregationstatisticcv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transectresults'


class Units(models.Model):
    unitsid = models.IntegerField(db_column='unitsid', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.ForeignKey('CvUnitstype', db_column='unitstypecv')  # Field name made lowercase.
    unitsabbreviation = models.TextField(db_column='unitsabbreviation')  # Field name made lowercase.
    unitsname = models.TextField(db_column='unitsname')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'units'


class VariableExtensionPropertyValue(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='variableid')  # Field name made lowercase.
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid')  # Field name made lowercase.
    propertyvalue = models.TextField(db_column='propertyvalue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variableextensionpropertyvalues'


class VariableExternalIdentifier(models.Model):
    bridgeid = models.IntegerField(db_column='bridgeid', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variable', db_column='variableid')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystem,
                                                   db_column='externalidentifiersystemid')  # Field name made lowercase.
    variableexternalidentifer = models.TextField(db_column='variableexternalidentifer')  # Field name made lowercase.
    variableexternalidentifieruri = models.TextField(db_column='variableexternalidentifieruri',
                                                     blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variableexternalidentifiers'


class Variable(models.Model):
    variableid = models.IntegerField(db_column='variableid', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.ForeignKey('CvVariabletype', db_column='variabletypecv')  # Field name made lowercase.
    variablecode = models.TextField(db_column='variablecode')  # Field name made lowercase.
    variablenamecv = models.ForeignKey('CvVariablename', db_column='variablenamecv')  # Field name made lowercase.
    variabledefinition = models.TextField(db_column='variabledefinition', blank=True)  # Field name made lowercase.
    speciationcv = models.ForeignKey('CvSpeciation', db_column='speciationcv', blank=True)  # Field name made lowercase.
    nodatavalue = models.FloatField(db_column='nodatavalue')  # Field name made lowercase.

    def natural_key(self):
        return self.variablecode + ' ' + self.variabletypecv.name

    class Meta:
        managed = False
        db_table = 'variables'


class CvActiontype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_actiontype'


class CvAggregationstatistic(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_aggregationstatistic'


class CvAnnotationtype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_annotationtype'


class CvCensorcode(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_censorcode'


class CvDataqualitytype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_dataqualitytype'


class CvDatasettype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_datasettype'


class CvDirectivetype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_directivetype'


class CvElevationdatum(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_elevationdatum'


class CvEquipmenttype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_equipmenttype'


class CvMedium(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_medium'


class CvMethodtype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_methodtype'


class CvOrganizationtype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_organizationtype'


class CvPropertydatatype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_propertydatatype'


class CvQualitycode(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cv_qualitycode'


class CvRelationshiptype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_relationshiptype'


class CvResulttype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_resulttype'


class CvSitetype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_sitetype'


class CvSpatialoffsettype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_spatialoffsettype'


class CvSpeciation(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_speciation'


class CvSpecimentype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_specimentype'


class CvStatus(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_status'


class CvTaxonomicclassifiertype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_taxonomicclassifiertype'


class CvUnitstype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_unitstype'


class CvVariablename(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_variablename'


class CvVariabletype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_variabletype'


class CvSamplingfeaturetype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturetype'


class CvSamplingfeaturegeotype(models.Model):
    term = models.TextField(db_column='term')  # Field name made lowercase.
    name = models.TextField(db_column='name', primary_key=True)  # Field name made lowercase.
    definition = models.TextField(db_column='definition', blank=True)  # Field name made lowercase.
    category = models.TextField(db_column='category', blank=True)  # Field name made lowercase.
    sourcevocabularyuri = models.TextField(db_column='sourcevocabularyuri', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturegeotype'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'


# TODO: make something more sophisticated than this later on
sqlserver_schema_fix = 'ODM2].['
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
classes = [model for name, model in clsmembers if issubclass(model, models.Model)]
database_manager = settings.DATABASES['ODM2']['ENGINE']

for model in classes:
    if database_manager == u'sql_server.pyodbc':
        model._meta.db_table = sqlserver_schema_fix + model._meta.db_table
    # can add more fixes there depending on the database engine
