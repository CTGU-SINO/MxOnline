__author__ = 'ct'
__date__ = '18-10-8 下午2:20'

from organization.views import OrgView, AddUserAskView, OrgHomeView

from django.urls import path, re_path

# 要写上app的名字
app_name = "organization"

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
]
