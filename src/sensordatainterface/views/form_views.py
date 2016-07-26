from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from sensordatainterface.forms import *


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class SiteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'site/site_form.html'
    model = Sites
    fields = []

    def get_context_data(self, **kwargs):
        context = super(SiteCreateView, self).get_context_data(**kwargs)
        data = self.request.POST if self.request.POST else None
        context['site_form'] = SiteForm(data)
        context['sampling_feature_form'] = SamplingFeatureForm(data)
        context['form_type'] = 'site'
        return context

    # def post(self, request, *args, **kwargs):
    #     sampling_feature_form = SamplingFeatureForm(request.POST)



# def edit_site(request, site_id):
#     action = 'create'
#     if request.method == 'POST':
#         if request.POST['action'] == 'update':
#             samplingfeature = SamplingFeature.objects.get(pk=request.POST['item_id'])
#             site = Sites.objects.get(pk=request.POST['item_id'])
#             samp_feat_form = SamplingFeatureForm(request.POST, instance=samplingfeature)
#             sites_form = SiteForm(request.POST, instance=site)
#
#         else:
#             samp_feat_form = SamplingFeatureForm(request.POST)
#             sites_form = SiteForm(request.POST)
#
#         if samp_feat_form.is_valid() and sites_form.is_valid():
#             # IDENTITY_INSERT error solved by changing samplingfeatureid for SamplingFeatures to AutoField in models.py
#             samplingfeature = samp_feat_form.save(commit=False)
#             samplingfeature.samplingfeaturetypecv = CvSamplingfeaturetype.objects.get(term='site')
#             samplingfeature.save()
#
#             site = sites_form.save(commit=False)
#             site.samplingfeatureid = samplingfeature
#             site.save()
#
#             messages.add_message(request, messages.SUCCESS, 'Site ' + request.POST['action'] + 'd successfully')
#             return HttpResponseRedirect(
#                 reverse('site_detail',
#                         args=[samplingfeature.samplingfeatureid]))
#
#     elif site_id:
#         samplingfeature = SamplingFeature.objects.get(pk=site_id)
#         site = Sites.objects.get(pk=site_id)
#         samp_feat_form = SamplingFeatureForm(instance=samplingfeature)
#         sites_form = SiteForm(instance=site)
#         sites_form.initial['spatialreferenceid'] = site.spatialreferenceid.spatialreferenceid
#         action = 'update'
#
#     else:
#         samp_feat_form = SamplingFeatureForm()
#         sites_form = SiteForm()
#
#     return render(
#         request,
#         'sites/site-form.html',
#         {'render_forms': [samp_feat_form, sites_form], 'action': action, 'item_id': site_id, 'form_type': 'site'}
#     )