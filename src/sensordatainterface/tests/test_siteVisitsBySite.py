from django.test import TestCase
from sensordatainterface.models import SamplingFeature, Method, Action, FeatureAction, EquipmentUsed
from django.test import RequestFactory
from sensordatainterface.views import SiteVisitsBySite
from django.db.models import Q
import datetime
import helper_classes

class TestSiteVisitsBySite(TestCase):
    def setUp(self):
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

        FeatureAction.objects.create(
            featureactionid = 100,
            samplingfeatureid = samplingfeature,
            actionid = action
        )

        FeatureAction.objects.create(
            featureactionid = 150,
            samplingfeatureid = samplingfeature2,
            actionid = action2
        )

        FeatureAction.objects.create(
            featureactionid = 200,
            samplingfeatureid = samplingfeature2,
            actionid = non_site_visit_action
        )

    def test_get_context_data(self):
        valid_feature_actions = FeatureAction.objects.filter(
            actionid__featureaction__samplingfeatureid=150
        )
        invalid_feature_actions = FeatureAction.objects.filter(
            ~Q(actionid__featureaction__samplingfeatureid=150)
        )

        valid_actions = [obj.actionid for obj in valid_feature_actions]
        valid_samplingfeatures = [obj.samplingfeatureid for obj in valid_feature_actions]

        invalid_actions = Action.objects.filter(
            ~Q(actiontypecv='SiteVisit')
        )

        actions = Action.objects.filter(actiontypecv='SiteVisit')

        request = RequestFactory().get('site-visits/site-visits/site/150',)
        request.user = helper_classes.User()

        view = SiteVisitsBySite.as_view()

        response = view(request, name='site_visits_by_site', site_id=150)
        context = response.context_data['SiteVisits']
        site_name = response.context_data['site_name']

        for site_visit in context:
            self.assertIn(site_visit, valid_feature_actions)
            self.assertNotIn(site_visit, invalid_feature_actions)
            self.assertIn(site_visit.actionid, valid_actions)
            self.assertIn(site_visit.actionid, actions)
            self.assertNotIn(site_visit.actionid, invalid_actions)
            self.assertIn(site_visit.samplingfeatureid, valid_samplingfeatures)
            self.assertEqual(site_name.samplingfeaturename, 'Logan River Aquatic')

    def tearDown(self):
        SamplingFeature.objects.all().delete()
        Method.objects.all().delete()
        Action.objects.all().delete()
        FeatureAction.objects.all().delete()