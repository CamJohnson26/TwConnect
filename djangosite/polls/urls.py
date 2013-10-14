from django.conf.urls.defaults import *
from models import Ticket

info_dict = {
    'queryset': Ticket.objects.all()
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^new/$', 'django.views.generic.create_update.create_object', { 'model': Ticket } ),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)