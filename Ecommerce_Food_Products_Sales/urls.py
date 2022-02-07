"""Ecommerce_Food_Products_Sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static

from Ecommerce_Food_Products_Sales import settings
from Customer import views as Customer_views
from Owner import views as admin_views

urlpatterns = [
        url(r'^admin/', admin.site.urls),

        url(r'^$', Customer_views.userlogin, name="userlogin"),
        url(r'^register/$', Customer_views.register, name="register"),
        url(r'^viewdetails/$', Customer_views.viewdetails, name="viewdetails"),
        url(r'^viewmodeldetails/(?P<pk>\d+)/$', Customer_views.viewmodeldetails, name="viewmodeldetails"),
        url(r'^addtocard/(?P<pk>\d+)/$', Customer_views.addtocard, name="addtocard"),
        url(r'^feedback/$', Customer_views.feedback, name="feedback"),
        url(r'^mydetails',Customer_views.mydetails, name="mydetails"),
        url(r'^updatedetails',Customer_views.updatedetails, name="updatedetails"),
        url(r'^userchart/(?P<chart_type>\w+)', Customer_views.userchart, name="userchart"),
        url(r'^reviewspage/$',Customer_views.reviewspage, name="reviewspage"),
        url('^ordertacking/$', Customer_views.ordertacking, name="ordertacking"),
        url(r'^orderchart/(?P<schart_type>\w+)', Customer_views.orderchart, name="orderchart"),
        url('^userlogout/$', Customer_views.userlogout, name="userlogout"),


        url(r'^adminlogin/$',admin_views.adminlogin, name="adminlogin"),
        url(r'^uploadpage/$',admin_views.uploadpage, name="uploadpage"),
        url(r'^updatefood/$', admin_views.updatefood, name="updatefood"),
        url(r'^viewfeedback/$',admin_views.viewfeedback,name="viewfeedback"),
        url(r'^customerdetails/$',admin_views.customerdetails,name="customerdetails"),
        url(r'^foodchart/(?P<chart_type>\w+)', admin_views.foodchart, name="foodchart"),
        url('^adminlogout/$', admin_views.adminlogout, name="adminlogout"),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns  += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
