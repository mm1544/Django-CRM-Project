# Need to have a separate urls.py file for each app.
# Need to import this file into MAIN project's urls.py file.
from django.urls import path

# Importing all views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]