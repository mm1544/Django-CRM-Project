from django.contrib import admin

from .models import Lead

# Need to register model to be able to see on Admin dashboard.
admin.site.register(Lead)