from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^pensum/nuevo/$', views.ingresar_pensum, name='ingresar_pensum'),

    ]
