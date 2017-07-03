"""TCSProj URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from ComplaintsForum.views import complaint_new
from Services.views import sla_new,service_new
from ChatBox.views import Login,Logout,Home,Post,Messages,register
from Dashboard.views import Dashboard



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^complaint_new/$', complaint_new, name='complaint_new'),
    url(r'^sla_new/$', sla_new, name='sla_new'),
    url(r'^login/$', Login, name='login'),
    url(r'^logout/$',Logout, name='logout'),
    url(r'^home/$', Home, name='home'),
    url(r'^post/$', Post, name='post'),
    url(r'^messages/$',Messages, name='messages'),
    url(r'^register/$', register , name='register'),
    url(r'^service_new/$', service_new , name='service_new'),
    url(r'^dashboard/$',Dashboard , name='dashboard'),
    

]
