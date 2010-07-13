from django.conf.urls.defaults import *
from django.views.generic import create_update
from django.views.generic.list_detail import object_list
from tickets.models import *
from tickets.forms import TicketPurchaseForm
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('tickets',
    url(r'^$', object_list,{
        'queryset':TicketedEvent.objects.all(),
        'template_object_name':'event',
        'template_name':'tickets/event_list.html',
        }),
    url(r'^(?P<event_slug>\w*)/$','views.purchase'),
    url(r'^payment/verification/', include('paypal.standard.ipn.urls')),
    url(r'^sold_out$',direct_to_template,{'template':"tickets/sold_out.html"},name="sold_out"),
    url(r'purchasedata$','views.purchase_data_csv'),
# list/types
# list/purchases
# ticket/buy
# payment/submit
# payment/initiated
# payment/verified
# payment/canceled
)

urlpatterns += patterns ('',
    url(r'^payment/initiated/','django.views.generic.simple.direct_to_template',
        {'template':'tickets/payment_initiated.html'}),
    url(r'^payment/canceled/','django.views.generic.simple.direct_to_template',
            {'template':'tickets/payment_canceled.html'}),
)