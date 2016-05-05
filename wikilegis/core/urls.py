from django.conf.urls import url
from django.views.generic.base import TemplateView
from wikilegis.core.views import BillReport, CreateProposal

urlpatterns = [
    url(r'^$', 'wikilegis.core.views.index', name='index'),
    url(
        r'^bill/(?P<bill_id>\d+)/$',
        'wikilegis.core.views.show_bill',
        name='show_bill'),
    url(
        r'^bill/(?P<bill_id>\d+)/proposal/$',
        CreateProposal.as_view(),
        name='create_proposal'),
    url(
        r'^bill/(?P<bill_id>\d+)/proposal/(?P<segment_id>\d+)/$',
        'wikilegis.core.views.show_proposal',
        name='show_proposal'),
    url(
        r'^bill/(?P<bill_id>\d+)/segments/(?P<segment_id>\d+)/$',
        'wikilegis.core.views.show_segment',
        name='show_segment'),
    url(
        r'^bill/(?P<bill_id>\d+)/segments/(?P<segment_id>\d+)/amend/$',
        'wikilegis.core.views.create_amendment',
        name='create_amendment'),
    url(
        r'^amendments/(?P<amendment_id>\d+)/$',
        'wikilegis.core.views.show_amendment',
        name='show_amendment'),
    url(
        r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(
        r'^bill/(?P<pk>\d+)/report/$',
        BillReport.as_view(),
        name='bill_report'),
    url(
        r'^upvote/(?P<content_type>\d+)/(?P<object_id>\d+)/$',
        'wikilegis.core.views.upvote',
        name='upvote'),
    url(
        r'^downvote/(?P<content_type>\d+)/(?P<object_id>\d+)/$',
        'wikilegis.core.views.downvote',
        name='downvote'),
]
