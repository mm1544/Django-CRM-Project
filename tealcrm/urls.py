# To handle File download
from django.conf import settings
# To handle File download
from django.conf.urls.static import static
from django.contrib import admin
# Importing all of the views
from django.contrib.auth import views
from django.urls import path, include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [

    #1. url path 
    #2. view function name
    #3. name of this 'path'

    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    # Importing / including all urls from dashboard's app urls.py file.
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/', include('userprofile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    # Here will use built in Django view. It is class based view (??). Passing-in template.
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # To handle File download 