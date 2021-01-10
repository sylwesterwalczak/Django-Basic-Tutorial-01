from django.urls import path
from .views import about_view, contact_view

app_name = 'common'

urlpatterns = [
    path('about-me', about_view, name = 'about_view'),
    path('contact', contact_view, name = 'contact_view'),
]