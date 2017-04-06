from django.test import TestCase
from sensordatainterface.urls import lists_urls, detail_urls
from sensordatainterface.views.detail_views import DeploymentDetail
from sensordatainterface.models import Sites, Action, EquipmentModel, SamplingFeature, SpatialReference, \
    FeatureAction, Method, People, Organization, Equipment, EquipmentUsed, CalibrationAction, Variable, Units, \
    InstrumentOutputVariable, RelatedAction
from django.conf import settings
import datetime
import helper_classes


class TestURLs(TestCase):
    def test_site_url(self):
        samplingfeature = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='Climate Site near Knowlton',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2178.1008,
            elevationdatumcv='EGM96'
        )

        samplingfeature2 = SamplingFeature.objects.create(
            samplingfeatureid=5,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_Wilkins_AA',
            samplingfeaturename='Wilkins Sensor Site',
            samplingfeaturedescription='Stream Site near Wilkins',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=3001.1008,
            elevationdatumcv='EGM96'
        )

        spatialreference = SpatialReference.objects.create(
            spatialreferenceid=1,
            srscode='4269',
            srsname='WGS84',
            srsdescription='Terrain is getting dry'
        )

        site = Sites.objects.create(
            samplingfeatureid=samplingfeature,
            sitetypecv='Stream',
            latitude=40.40,
            longitude=10.10,
            latlondatumid=spatialreference
        )
        site2 = Sites.objects.create(
            samplingfeatureid=samplingfeature2,
            sitetypecv='Atmosphere',
            latitude=90.90,
            longitude=80.80,
            latlondatumid=spatialreference
        )

        objects, response = getListObjects('sites/', 'home')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 2)
        for site in objects:
            self.assertTrue(
                site.samplingfeatureid.samplingfeaturecode=='RB_KF_C'
                or site.samplingfeatureid.samplingfeaturecode=='LR_Wilkins_AA'
            )
            self.assertTrue(
                site.samplingfeatureid.samplingfeaturename=='Knowlton Fork Climate'
                or site.samplingfeatureid.samplingfeaturename=='Wilkins Sensor Site'
            )
            self.assertTrue(
                site.sitetypecv=='Stream'
                or site.sitetypecv=='Atmosphere'
            )
            self.assertTrue(
                site.latitude==90.90
                or site.latitude==40.40
            )

        Sites.objects.all().delete()
        SamplingFeature.objects.all().delete()
        SpatialReference.objects.all().delete()

    def test_site_detail(self):
        samplingfeature = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='helohneloolohjellohelooljhelol',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2178.1008,
            elevationdatumcv='EGM96'
        )

        samplingfeature2 = SamplingFeature.objects.create(
            samplingfeatureid=5,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_Wilkins_AA',
            samplingfeaturename='Wilkins is a nice guy',
            samplingfeaturedescription='He likes pancakes',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=3001.1008,
            elevationdatumcv='EGM96'
        )

        spatialreference = SpatialReference.objects.create(
            spatialreferenceid=1,
            srscode='4269',
            srsname='WGS84',
            srsdescription='for the power granted by AmumRa'
        )

        site = Sites.objects.create(
            samplingfeatureid=samplingfeature,
            sitetypecv='Stream',
            latitude=40.40,
            longitude=10.10,
            latlondatumid=spatialreference
        )
        site2 = Sites.objects.create(
            samplingfeatureid=samplingfeature2,
            sitetypecv='Atmosphere',
            latitude=90.90,
            longitude=80.80,
            latlondatumid=spatialreference
        )

        site, response = getDetailObject('sites/site-detail/', 'site_detail', 100)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(site.samplingfeatureid.samplingfeaturecode, 'RB_KF_C')
        self.assertEqual(site.sitetypecv, 'Stream')
        self.assertEqual(site.longitude, 10.10)
        self.assertEqual(site.samplingfeatureid.samplingfeaturename, 'Knowlton Fork Climate')
        self.assertEqual(site.latlondatumid.srscode, '4269')

        Sites.objects.all().delete()
        SamplingFeature.objects.all().delete()
        SpatialReference.objects.all().delete()

    def test_visits_url(self):
        samplingfeature = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='Climate Site near Knowlton',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2345.1685,
            elevationdatumcv='EGM96'
        )

        samplingfeature2 = SamplingFeature.objects.create(
            samplingfeatureid=150,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_ARBR_A',
            samplingfeaturename='Logan River Aquatic',
            samplingfeaturedescription='Logan River site Sensors',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2178.1008,
            elevationdatumcv='EGM96'
        )

        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2011, 8, 22),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2011, 8, 24),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_site_visit_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'Deployment',
            methodid = method,
            begindatetime = datetime.datetime(2014, 12, 30),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2014, 12, 31),
            enddatetimeutcoffset = -7,
            actiondescription = 'Deloyed equipment',
            actionfilelink = 'www.file.com'
        )

        featureaction = FeatureAction.objects.create(
            featureactionid = 100,
            samplingfeatureid = samplingfeature,
            actionid = action
        )

        featureaction2 = FeatureAction.objects.create(
            featureactionid = 150,
            samplingfeatureid = samplingfeature2,
            actionid = action2
        )

        non_site_visit_featureaction = FeatureAction.objects.create(
            featureactionid = 200,
            samplingfeatureid = samplingfeature2,
            actionid = non_site_visit_action
        )

        objects, response = getListObjects('site-visits/site-visits/', 'site_visits')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 2)

        for visit in objects:
            self.assertEqual(visit.actionid.actiontypecv, 'SiteVisit')
            if visit.featureactionid == 100:
                self.assertEqual(visit.actionid.begindatetime, datetime.datetime(2010, 12, 24))
                self.assertEqual(visit.samplingfeatureid.samplingfeaturecode, 'RB_KF_C')
                self.assertEqual(visit.samplingfeatureid.samplingfeaturename, 'Knowlton Fork Climate')

            if visit.featureactionid == 150:
                self.assertEqual(visit.actionid.begindatetime, datetime.datetime(2011, 8, 22))
                self.assertEqual(visit.samplingfeatureid.samplingfeaturecode, 'LR_ARBR_A')
                self.assertEqual(visit.samplingfeatureid.samplingfeaturename, 'Logan River Aquatic')

            if visit.featureactionid == 200:
                self.fail()

        FeatureAction.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()
        SamplingFeature.objects.all().delete()

    def test_visits_detail(self):
        samplingfeature = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='Climate Site near Knowlton',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2345.1685,
            elevationdatumcv='EGM96'
        )

        samplingfeature2 = SamplingFeature.objects.create(
            samplingfeatureid=150,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='LR_ARBR_A',
            samplingfeaturename='Logan River Aquatic',
            samplingfeaturedescription='Logan River site Sensors',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2178.1008,
            elevationdatumcv='EGM96'
        )

        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2011, 8, 22),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2011, 8, 24),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_site_visit_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'Deployment',
            methodid = method,
            begindatetime = datetime.datetime(2014, 12, 30),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2014, 12, 31),
            enddatetimeutcoffset = -7,
            actiondescription = 'Deloyed equipment',
            actionfilelink = 'www.file.com'
        )

        featureaction = FeatureAction.objects.create(
            featureactionid = 100,
            samplingfeatureid = samplingfeature,
            actionid = action
        )

        featureaction2 = FeatureAction.objects.create(
            featureactionid = 150,
            samplingfeatureid = samplingfeature2,
            actionid = action2
        )

        non_site_visit_featureaction = FeatureAction.objects.create(
            featureactionid = 200,
            samplingfeatureid = samplingfeature2,
            actionid = non_site_visit_action
        )

        visit, response = getDetailObject('site-visits/visit-detail/', 'site_visit_detail', 150)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(visit, featureaction2)
        self.assertNotEqual(visit, featureaction)
        self.assertNotEqual(visit, non_site_visit_action)

        visit, response = getDetailObject('site-visits/visit-detail/', 'site_visit_detail', 100)

        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(visit, featureaction2)
        self.assertEqual(visit, featureaction)
        self.assertNotEqual(visit, non_site_visit_action)

        SamplingFeature.objects.all().delete()
        Method.objects.all().delete()
        Action.objects.all().delete()
        FeatureAction.objects.all().delete()

    def test_deployments_url(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'Equipment deployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_deployment_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2012, 4, 10),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 4, 11),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment_used = EquipmentUsed.objects.create(
            bridgeid = 100,
            actionid = action,
            equipmentid = equipment
        )

        equipment_used2 = EquipmentUsed.objects.create(
            bridgeid = 150,
            actionid = action2,
            equipmentid = equipment2
        )

        equipment_used3 = EquipmentUsed.objects.create(
            bridgeid = 200,
            actionid = non_deployment_action,
            equipmentid = equipment2
        )

        objects, response = getListObjects('site-visits/deployments/', 'deployments')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 2)

        for deployment in objects:
            if deployment.bridgeid == 100:
                self.assertEqual(deployment.actionid.begindatetime, datetime.datetime(2010, 12, 24))
                self.assertEqual(deployment.equipmentid.equipmentserialnumber, '7492634SH')
                self.assertEqual(deployment.equipmentid.equipmenttypecv, 'Temperature Sensor')

            elif deployment.bridgeid == 150:
                self.assertEqual(deployment.actionid.begindatetime, datetime.datetime(2010, 10, 3))
                self.assertEqual(deployment.equipmentid.equipmentserialnumber, '7492345SH')
                self.assertEqual(deployment.equipmentid.equipmenttypecv, 'Water Sensor')

            elif deployment.bridgeid == 200:
                self.fail()

            self.assertTrue(
                deployment.actionid.actiontypecv == 'Instrument deployment' or
                deployment.actionid.actiontypecv == 'Equipment deployment'
            )

            self.assertEqual(deployment.equipmentid.equipmentmodelid.modelmanufacturerid.organizationname, 'Fenix Equipment')
            self.assertEqual(deployment.equipmentid.equipmentmodelid.modelpartnumber, '53453')


        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Organization.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_deployments_detail(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'Equipment deployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_deployment_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2012, 4, 10),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 4, 11),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment_used = EquipmentUsed.objects.create(
            bridgeid = 100,
            actionid = action,
            equipmentid = equipment
        )

        equipment_used2 = EquipmentUsed.objects.create(
            bridgeid = 150,
            actionid = action2,
            equipmentid = equipment2
        )

        equipment_used3 = EquipmentUsed.objects.create(
            bridgeid = 200,
            actionid = non_deployment_action,
            equipmentid = equipment2
        )

        deployment, response = getDetailObject('site-visits/deployment-detail/', 'deployment_detail', slug=150)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(deployment, equipment_used2)
        self.assertEqual(deployment.actionid, action2)
        self.assertEqual(deployment.equipmentid, equipment2)

        self.assertNotEqual(deployment, equipment_used)
        self.assertNotEqual(deployment, equipment_used3)


        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Organization.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_calibrations_url(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'Instrument calibration',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'Instrument calibration',
            methodid = method,
            begindatetime = datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_deployment_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2012, 4, 10),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 4, 11),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment_used = EquipmentUsed.objects.create(
            bridgeid = 100,
            actionid = action,
            equipmentid = equipment
        )

        equipment_used2 = EquipmentUsed.objects.create(
            bridgeid = 150,
            actionid = action2,
            equipmentid = equipment2
        )

        equipment_used3 = EquipmentUsed.objects.create(
            bridgeid = 200,
            actionid = non_deployment_action,
            equipmentid = equipment2
        )

        variable = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        units = Units.objects.create(
            unitsid = 1,
            unitstypecv = 'pH',
            unitsabbreviation = 'pH',
            unitsname = 'Acidity'
        )

        output_variable = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        calibration_action = CalibrationAction.objects.create(
            actionid = action,
            calibrationcheckvalue = 17.0,
            instrumentoutputvariableid = output_variable,
            calibrationequation = 'X^2'
        )

        calibration_action2 = CalibrationAction.objects.create(
            actionid = action2,
            calibrationcheckvalue = 8.0,
            instrumentoutputvariableid = output_variable,
            calibrationequation = 'X^5'
        )


        objects, response = getListObjects('site-visits/calibrations/', 'calibrations')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 2)

        for calibration in objects:
            if calibration.bridgeid == 100:
                self.assertEqual(calibration.actionid.begindatetime, datetime.datetime(2010, 12, 24))
                self.assertEqual(calibration.equipmentid.equipmentserialnumber, '7492634SH')
                self.assertEqual(calibration.equipmentid.equipmenttypecv, 'Temperature Sensor')

            elif calibration.bridgeid == 150:
                self.assertEqual(calibration.actionid.begindatetime, datetime.datetime(2010, 10, 3))
                self.assertEqual(calibration.equipmentid.equipmentserialnumber, '7492345SH')
                self.assertEqual(calibration.equipmentid.equipmenttypecv, 'Water Sensor')

            elif calibration.bridgeid == 200:
                self.fail()

            self.assertTrue(calibration.actionid.actiontypecv == 'Instrument calibration')
            self.assertEqual(calibration.equipmentid.equipmentmodelid.modelmanufacturerid.organizationname, 'Fenix Equipment')
            self.assertEqual(calibration.equipmentid.equipmentmodelid.modelname, 'Climate')


        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Organization.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Variable.objects.all().delete()
        Units.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_calibrations_detail(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'Instrument calibration',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'Instrument calibration',
            methodid = method,
            begindatetime = datetime.datetime(2010, 10, 3),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 10, 4),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        non_deployment_action = Action.objects.create(
            actionid = 200,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2012, 4, 10),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 4, 11),
            enddatetimeutcoffset = -7,
            actiondescription = 'Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment_used = EquipmentUsed.objects.create(
            bridgeid = 100,
            actionid = action,
            equipmentid = equipment
        )

        equipment_used2 = EquipmentUsed.objects.create(
            bridgeid = 150,
            actionid = action2,
            equipmentid = equipment2
        )

        equipment_used3 = EquipmentUsed.objects.create(
            bridgeid = 200,
            actionid = non_deployment_action,
            equipmentid = equipment2
        )

        variable = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        units = Units.objects.create(
            unitsid = 1,
            unitstypecv = 'pH',
            unitsabbreviation = 'pH',
            unitsname = 'Acidity'
        )

        output_variable = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        calibration_action = CalibrationAction.objects.create(
            actionid = action,
            calibrationcheckvalue = 17.0,
            instrumentoutputvariableid = output_variable,
            calibrationequation = 'X^2'
        )

        calibration_action2 = CalibrationAction.objects.create(
            actionid = action2,
            calibrationcheckvalue = 8.0,
            instrumentoutputvariableid = output_variable,
            calibrationequation = 'X^5'
        )

        calibration, response = getDetailObject('site-visits/calibration-detail/', 'calibration_detail', 150)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(calibration, equipment_used2)
        self.assertEqual(calibration.actionid, action2)
        self.assertEqual(calibration.equipmentid, equipment2)

        self.assertNotEqual(calibration, equipment_used)
        self.assertNotEqual(calibration, equipment_used3)

        EquipmentUsed.objects.all().delete()
        Equipment.objects.all().delete()
        Organization.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Variable.objects.all().delete()
        Units.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_activities_url(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        parent_action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2008, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2008, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Parent 1:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        parent_action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2009, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2009, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Parent 2:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_1 = Action.objects.create(
            actionid = 200,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 1-1:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_1_2 = Action.objects.create(
            actionid = 250,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2011, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2011, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 1-2: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_2 = Action.objects.create(
            actionid = 300,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2012, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 2-1: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_2_2 = Action.objects.create(
            actionid = 350,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2013, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2013, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 2-2: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        related_action_1_1 = RelatedAction.objects.create(
            relationid = 1,
            actionid = child_action_1,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action
        )

        related_action_1_2 = RelatedAction.objects.create(
            relationid = 2,
            actionid = child_action_1_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action
        )

        related_action_2_1 = RelatedAction.objects.create(
            relationid = 3,
            actionid = child_action_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action2
        )

        related_action_2_2 = RelatedAction.objects.create(
            relationid = 4,
            actionid = child_action_2_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action2
        )

        activities = [child_action_1, child_action_1_2, child_action_2, child_action_2_2]

        objects, response = getListObjects('site-visits/other-activities/', 'field_activities')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 4)

        for activity in objects:
            self.assertIn(activity, activities)
            if activity.actionid == 200:
                self.assertEqual(activity.actiontypecv, 'InstrumentDeployment')
                self.assertEqual(activity.begindatetime, datetime.datetime(2010, 12, 24))
                self.assertEqual(activity.actiondescription, 'Child 1-1:Made different calibrations and Deployments',)

        RelatedAction.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_activities_detail(self):
        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = None
        )

        parent_action = Action.objects.create(
            actionid = 100,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2008, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2008, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Parent 1:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        parent_action2 = Action.objects.create(
            actionid = 150,
            actiontypecv = 'SiteVisit',
            methodid = method,
            begindatetime = datetime.datetime(2009, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2009, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Parent 2:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_1 = Action.objects.create(
            actionid = 200,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2010, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2010, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 1-1:Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_1_2 = Action.objects.create(
            actionid = 250,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2011, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2011, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 1-2: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_2 = Action.objects.create(
            actionid = 300,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2012, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2012, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 2-1: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        child_action_2_2 = Action.objects.create(
            actionid = 350,
            actiontypecv = 'InstrumentDeployment',
            methodid = method,
            begindatetime = datetime.datetime(2013, 12, 24),
            begindatetimeutcoffset = -7,
            enddatetime = datetime.datetime(2013, 12, 25),
            enddatetimeutcoffset = -7,
            actiondescription = 'Child 2-2: Made different calibrations and Deployments',
            actionfilelink = 'www.file.com'
        )

        related_action_1_1 = RelatedAction.objects.create(
            relationid = 1,
            actionid = child_action_1,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action
        )

        related_action_1_2 = RelatedAction.objects.create(
            relationid = 2,
            actionid = child_action_1_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action
        )

        related_action_2_1 = RelatedAction.objects.create(
            relationid = 3,
            actionid = child_action_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action2
        )

        related_action_2_2 = RelatedAction.objects.create(
            relationid = 4,
            actionid = child_action_2_2,
            relationshiptypecv = 'Is child of',
            relatedactionid = parent_action2
        )

        samplingfeature = SamplingFeature.objects.create(
            samplingfeatureid=100,
            samplingfeaturetypecv='Site',
            samplingfeaturecode='RB_KF_C',
            samplingfeaturename='Knowlton Fork Climate',
            samplingfeaturedescription='Climate Site near Knowlton',
            samplingfeaturegeotypecv='2D-Point',
            elevation_m=2345.1685,
            elevationdatumcv='EGM96'
        )

        featureaction = FeatureAction.objects.create(
            featureactionid = 300,
            samplingfeatureid = samplingfeature,
            actionid = child_action_2
        )

        featureaction2 = FeatureAction.objects.create(
            featureactionid = 350,
            samplingfeatureid = samplingfeature,
            actionid = child_action_1_2
        )

        featureaction3 = FeatureAction.objects.create(
            featureactionid = 100,
            samplingfeatureid = samplingfeature,
            actionid = child_action_2_2
        )

        featureaction4 = FeatureAction.objects.create(
            featureactionid = 150,
            samplingfeatureid = samplingfeature,
            actionid = parent_action
        )

        action, response = getDetailObject('site-visits/field-activity-detail/', 'field_activity_detail', 300)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(action, featureaction)
        self.assertNotEqual(action, child_action_1_2)
        self.assertNotEqual(action, child_action_2_2)
        self.assertNotEqual(action, parent_action)


        RelatedAction.objects.all().delete()
        FeatureAction.objects.all().delete()
        SamplingFeature.objects.all().delete()
        Action.objects.all().delete()
        Method.objects.all().delete()

    def test_equipment_url(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment3 = Equipment.objects.create(
            equipmentid = 3,
            equipmentcode = 'MBH14',
            equipmentname = 'SpecialSensor',
            equipmenttypecv = 'X-Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492623SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipments = [equipment, equipment2, equipment3]

        objects, response = getListObjects('inventory/equipment/', 'equipment')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 3)

        for equ in objects:
            self.assertIn(equ, equipments)
            if equ.equipmentid == 2:
                self.assertEqual(equ.equipmentserialnumber, '7492345SH')
                self.assertEqual(equ.equipmenttypecv, 'Water Sensor')
                self.assertEqual(equ.equipmentcode, 'MBH13')
                self.assertEqual(equ.equipmentmodelid.modelname, 'Climate')
                self.assertEqual(equ.equipmentmodelid.modelmanufacturerid.organizationname, 'Fenix Equipment')
                self.assertEqual(equ.equipmentownerid.personfirstname, 'Chris')

        Equipment.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()

    def test_equipment_detail(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization,
            modelpartnumber = '45678',
            modelname = 'Waters',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        people = People.objects.create(
            personid = 100,
            personfirstname = 'Chris',
            personmiddlename = 'A.',
            personlastname = 'Cox'
        )

        equipment = Equipment.objects.create(
            equipmentid = 1,
            equipmentcode = 'MBH12',
            equipmentname = 'ClimateSensor',
            equipmenttypecv = 'Temperature Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492634SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment2 = Equipment.objects.create(
            equipmentid = 2,
            equipmentcode = 'MBH13',
            equipmentname = 'AquaticSensor',
            equipmenttypecv = 'Water Sensor',
            equipmentmodelid = model2,
            equipmentserialnumber = '7492345SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equipment3 = Equipment.objects.create(
            equipmentid = 3,
            equipmentcode = 'MBH14',
            equipmentname = 'SpecialSensor',
            equipmenttypecv = 'X-Sensor',
            equipmentmodelid = model,
            equipmentserialnumber = '7492623SH',
            equipmentownerid = people,
            equipmentvendorid = organization,
            equipmentpurchasedate = datetime.datetime(2014, 2, 13),
            equipmentpurchaseordernumber = 'PO875934',
            equipmentdescription = 'Multiple Sensors',
            equipmentdocumentationlink = 'www.equipment.org'
        )

        equ, response = getDetailObject('inventory/equipment-detail/', 'equipment_detail', 2)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(equ, equipment2)
        self.assertEqual(equ.equipmentmodelid, model2)
        self.assertEqual(equ.equipmentserialnumber, '7492345SH')

        self.assertNotEqual(equ, equipment)
        self.assertNotEqual(equ, equipment3)
        self.assertNotEqual(equ.equipmentmodelid, model)

        Equipment.objects.all().delete()
        People.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()

    def test_factory_service_url(self):
        pass

    def test_factory_service_detail(self):
        pass

    def test_output_variables_url(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization,
            modelpartnumber = '49273',
            modelname = 'Water Sensor',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        variable = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        variable2 = Variable.objects.create(
            variableid = 5,
            variabletypecv = 'Climate',
            variablecode = 'AirTemp_Avg',
            variablenamecv = 'Air Temperature',
            variabledefinition = 'Temperature in the Air',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        units = Units.objects.create(
            unitsid = 1,
            unitstypecv = 'pH',
            unitsabbreviation = 'pH',
            unitsname = 'Acidity'
        )

        units2 = Units.objects.create(
            unitsid = 5,
            unitstypecv = 'dgC',
            unitsabbreviation = 'dgC',
            unitsname = 'Temperature'
        )

        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = organization
        )

        output_variable = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        output_variable2 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 5,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        output_variable3 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 10,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        objects, response = getListObjects('inventory/sensor-output-variables/', 'sensor_output')

        output_variables = [output_variable, output_variable2, output_variable3]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 3)

        for output_var in objects:
            self.assertIn(output_var, output_variables)
            if output_var.instrumentoutputvariableid == 10:
                self.assertEqual(output_var.variableid.variablecode, 'AirTemp_Avg')
                self.assertEqual(output_var.variableid.variablenamecv, 'Air Temperature')
                self.assertEqual(output_var.modelid.modelname, 'Water Sensor')

            self.assertEqual(output_var.instrumentmethodid.methodcode, 'MTH16')
            self.assertEqual(output_var.instrumentmethodid.methodname, 'Sensor Reading')

        InstrumentOutputVariable.objects.all().delete()
        Method.objects.all().delete()
        Units.objects.all().delete()
        Variable.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()

    def test_output_variables_detail(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization,
            modelpartnumber = '49273',
            modelname = 'Water Sensor',
            modeldescription = 'CommonModel',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        variable = Variable.objects.create(
            variableid = 1,
            variabletypecv = 'Aquatic',
            variablecode = 'pH',
            variablenamecv = 'pH',
            variabledefinition = 'Water Acidity',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        variable2 = Variable.objects.create(
            variableid = 5,
            variabletypecv = 'Climate',
            variablecode = 'AirTemp_Avg',
            variablenamecv = 'Air Temperature',
            variabledefinition = 'Temperature in the Air',
            speciationcv = 'Specifiation',
            nodatavalue = 9999.9
        )

        units = Units.objects.create(
            unitsid = 1,
            unitstypecv = 'pH',
            unitsabbreviation = 'pH',
            unitsname = 'Acidity'
        )

        units2 = Units.objects.create(
            unitsid = 5,
            unitstypecv = 'dgC',
            unitsabbreviation = 'dgC',
            unitsname = 'Temperature'
        )

        method = Method.objects.create(
            methodid = 100,
            methodtypecv = 'Field Measurement',
            methodcode = 'MTH16',
            methodname = 'Sensor Reading',
            methoddescription = 'Sensor Constantly Reading',
            methodlink = 'www.thismethod.com',
            organizationid = organization
        )

        output_variable = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 1,
            modelid = model,
            variableid = variable,
            instrumentmethodid = method,
            instrumentresolution = 'Updated Span',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units
        )

        output_variable2 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 5,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        output_variable3 = InstrumentOutputVariable.objects.create(
            instrumentoutputvariableid = 10,
            modelid = model2,
            variableid = variable2,
            instrumentmethodid = method,
            instrumentresolution = 'Measure Different aspects',
            instrumentaccuracy = 'None',
            instrumentrawoutputunitsid = units2
        )

        output_var, response = getDetailObject('inventory/output-variable-detail/', 'output_variable_detail', 5)

        self.assertEqual(response.status_code, 200)


        self.assertEqual(output_var, output_variable2)
        self.assertEqual(output_var.modelid, model2)
        self.assertEqual(output_var.variableid, variable2)
        self.assertEqual(output_var.instrumentrawoutputunitsid, units2)

        self.assertNotEqual(output_var.modelid, model)
        self.assertNotEqual(output_var.variableid, variable)
        self.assertNotEqual(output_var.instrumentrawoutputunitsid, units)

        self.assertNotEqual(output_var, output_variable)
        self.assertNotEqual(output_var, output_variable3)




        InstrumentOutputVariable.objects.all().delete()
        Method.objects.all().delete()
        Units.objects.all().delete()
        Variable.objects.all().delete()
        EquipmentModel.objects.all().delete()
        Organization.objects.all().delete()

        pass

    def test_models_url(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        organization2 = Organization.objects.create(
            organizationid = 150,
            organizationtypecv = 'Organization',
            organizationcode = 'CampSci',
            organizationname = 'Campbell Scientific',
            organizationdescription = 'Measurement & Control Products for Long-term Monitoring',
            organizationlink = 'http://www.campbellsci.com/',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'model1',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization2,
            modelpartnumber = '62345',
            modelname = 'Water',
            modeldescription = 'model2',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model3 = EquipmentModel.objects.create(
            equipmentmodelid = 200,
            modelmanufacturerid = organization,
            modelpartnumber = '73454',
            modelname = 'Climate',
            modeldescription = 'model3',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model4 = EquipmentModel.objects.create(
            equipmentmodelid = 250,
            modelmanufacturerid = organization2,
            modelpartnumber = '84563',
            modelname = 'CC5MPXWD',
            modeldescription = 'Weatherproof, low power digital camera',
            isinstrument = True,
            modelspecificationsfilelink = 'cc5mpx.pdf',
            modellink = 'www.model.com'
        )


        models = [model, model2, model3, model4]

        objects, response = getListObjects('inventory/equipment-models/', 'models')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(objects.count(), 4)

        for model in objects:
            self.assertIn(model, models)
            if model.equipmentmodelid == 250:
                self.assertEqual(model.modelname, 'CC5MPXWD')
                self.assertEqual(model.modelpartnumber, '84563')
                self.assertEqual(model.modelmanufacturerid.organizationname, 'Campbell Scientific')
                self.assertEqual(model.modeldescription, 'Weatherproof, low power digital camera')

        Organization.objects.all().delete()
        EquipmentModel.objects.all().delete()

    def test_models_detail(self):
        organization = Organization.objects.create(
            organizationid = 100,
            organizationtypecv = 'Manufacturer',
            organizationcode = 'DF10',
            organizationname = 'Fenix Equipment',
            organizationdescription = 'Climate Equipment and more',
            organizationlink = 'www.fenix.com',
            parentorganizationid = None
        )

        organization2 = Organization.objects.create(
            organizationid = 150,
            organizationtypecv = 'Organization',
            organizationcode = 'CampSci',
            organizationname = 'Campbell Scientific',
            organizationdescription = 'Measurement & Control Products for Long-term Monitoring',
            organizationlink = 'http://www.campbellsci.com/',
            parentorganizationid = None
        )

        model = EquipmentModel.objects.create(
            equipmentmodelid = 100,
            modelmanufacturerid = organization,
            modelpartnumber = '53453',
            modelname = 'Climate',
            modeldescription = 'model1',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model2 = EquipmentModel.objects.create(
            equipmentmodelid = 150,
            modelmanufacturerid = organization2,
            modelpartnumber = '62345',
            modelname = 'Water',
            modeldescription = 'model2',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model3 = EquipmentModel.objects.create(
            equipmentmodelid = 200,
            modelmanufacturerid = organization,
            modelpartnumber = '73454',
            modelname = 'Climate',
            modeldescription = 'model3',
            isinstrument = True,
            modelspecificationsfilelink = 'specs.pdf',
            modellink = 'www.model.com'
        )

        model4 = EquipmentModel.objects.create(
            equipmentmodelid = 250,
            modelmanufacturerid = organization2,
            modelpartnumber = '84563',
            modelname = 'CC5MPXWD',
            modeldescription = 'Weatherproof, low power digital camera',
            isinstrument = True,
            modelspecificationsfilelink = 'cc5mpx.pdf',
            modellink = 'www.model.com'
        )

        mod, response = getDetailObject('inventory/models-detail/', 'models_detail', 200)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(mod, model3)

        Organization.objects.all().delete()
        EquipmentModel.objects.all().delete()

def getListObjects(url, url_name, ):
    request = helper_classes.Request('GET', settings.SITE_URL + url)
    url = urlIndexHelper(lists_urls.urlpatterns, url_name)
    response = url.callback(request)
    return response.context_data['object_list'], response

def getDetailObject(url, url_name, slug):
    request = helper_classes.Request('GET', settings.SITE_URL + url)
    url = urlIndexHelper(detail_urls.urlpatterns, url_name)
    response = url.callback(request, slug=slug)
    return response.context_data['object'], response

def urlIndexHelper(urlpatterns, name):
    for entry in urlpatterns:
        if entry.name == name:
            return entry