from django.conf.urls import url, include
from django.contrib import admin
from views import index, team_details

urlpatterns = [
    url(r'^$', index, name='main_page'),
    url(r'^team/(?P<team_id>[\d]+)/$', team_details, name='team_details')
]