from django.conf.urls import url
# import our views from the directory we are in
from . import views
 
# 3 Add a namespace so Django knows what directory to load
# if another app has views with the same name
app_name = 'polls'
 
    # 3 Add the 3 views
    # The data surrounded by parentheses is sent to the function
    # ?P<question_id> defines the name for the data within
    # the parentheses
    # [0-9]+ says we will match 1 or more numbers
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
# Using generic views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]