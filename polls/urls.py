from django.conf.urls import url
# import our views from the directory we are in
from . import views
# Attach the view to the url, root directory fro web app
urlpatterns = [
    url(r'^', views.index, name='index'),
]