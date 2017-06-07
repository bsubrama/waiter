from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from .api import ContentChannelList, ContentChannelDetail, RunsForContentChannelList
from .api import ContentChannelRunListCreate, ContentChannelRunDetail
from .api import ChannelRunEventListCreate

urlpatterns = [
    url(regex=r'channels/$',
        view=ContentChannelList.as_view(),
        name='list_details'),
    #
    url(regex=r'channels/(?P<channel_id>[0-9A-Fa-f-]+)/$',
        view=ContentChannelDetail.as_view(),
        name='channel_details'),
    #
    url(regex=r'channels/(?P<channel_id>[0-9A-Fa-f-]+)/runs/$',
        view=RunsForContentChannelList.as_view(),
        name='runs_for_channel'),
    #
    #
    url(regex=r'channelruns/$',
        view=ContentChannelRunListCreate.as_view(),
        name='list_runs'),
    #
    url(regex=r'channelruns/(?P<run_id>[0-9A-Fa-f-]+)/$',
        view=ContentChannelRunDetail.as_view(),
        name='run_details'),
    #
    url(regex=r'channelruns/(?P<run_id>[0-9A-Fa-f-]+)/events/$',
        view=ChannelRunEventListCreate.as_view(),
        name='events_for_run'),
]

urlpatterns = format_suffix_patterns(urlpatterns)