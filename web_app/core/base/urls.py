from django.contrib import admin
from django.urls import path

from . import views
from .views import IndexTemplateview
from .views import ContactTemplateView

app_name = 'base'
urlpatterns = [
    path('', IndexTemplateview.as_view(), name = 'index'),
    path('contact', ContactTemplateView.as_view(), name = 'contact'),
]
