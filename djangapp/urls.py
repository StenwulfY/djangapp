"""djangapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
"Match the url in the browser to a module in the porject"
from django.conf.urls import url
"Admin is going to load url for administration "
from django.contrib import admin
"Import a function from the class file "
from djangapp.views import hello_world, root_page, random_number
# point url file to polls app

from django.conf.urls import include

"""list all the urls to type 
Regular expression to acces pages"""
# the \d+ Represents 1 or more Numbers, this is a Regular Expression
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', hello_world),
    url(r'^$', root_page),
    url(r'random/(\d+)/$', random_number),
    url(r'^polls$', include('polls.urls')),
]
