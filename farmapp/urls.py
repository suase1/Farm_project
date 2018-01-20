from django.conf.urls import url
from farmapp.views import *
from django.urls import include
from django.conf import settings

urlpatterns = [
    url(r'^$', OrderFV, name='order'),
    url(r'^check/(?P<pk>\d+)/$', OrderCheck, name='ordercheck'),
    url(r'^edit/(?P<pk>\d+)/$', OrderEdit, name='orderedit'),
    url(r'^confirm/$', OrderConfirm.as_view(), name='orderconfirm'),
    url(r'^orderlist/$', OrderList.as_view(), name='orderlist'),
]
