from django.conf.urls import url
from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.ScanBooks, name='ScanBooks'),
    path('decode/', views.decodeAjax,name='decodeAjax'),

]