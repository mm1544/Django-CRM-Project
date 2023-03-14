from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [

    #1. url path 
    #2. view function name
    #3. name of this 'path'

    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    path('sign-up', signup, name='signup'),
    # Here will use Class based views
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
