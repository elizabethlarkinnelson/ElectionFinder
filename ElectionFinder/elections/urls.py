from django.urls import path

from . import views

app_name = 'elections'
urlpatterns = [
    # ex: /elections/
    path('', views.election_form, name='election_form'),
]