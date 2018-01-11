from django.conf.urls import url
from  user import api

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/investment/$',
       api.investment_detail, name='investments',),

    url(r'^(?P<user_id>[0-9]+)/investment/(?P<portfolio_id>[0-9]+)/$',
        api.update_units, name='unit_update',),
]