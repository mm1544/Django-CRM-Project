from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    # For Class based view
    path('', views.LeadListView.as_view(), name='list'),
    # '<int:pk>' --> dynamic part of a URL. 'int' - integer; 'pk' - argument in view funtion 'def leads_detail(request, pk)'
    
    # For Class based view
    path('<int:pk>/', views.LeadDetailView.as_view(), name='detail'),
    # For Func based view
    # path('<int:pk>/', views.leads_detail, name='detail'),
    
    # For Class based view
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='delete'),
    # For Func based view
    # path('<int:pk>/delete/', views.leads_delete, name='delete'),
    
    # For Class based view
    path('<int:pk>/edit/', views.LeadUpdateView.as_view(), name='edit'),
    # For Func based view
    # path('<int:pk>/edit/', views.leads_edit, name='edit'),

    # For Class based view
    path('<int:pk>/convert/', views.ConvertToClientView.as_view(), name='convert'),
    # For Func based view
    # path('<int:pk>/convert/', views.convert_to_client, name='convert'),

    # For Func based view
    path('add/', views.LeadCreateView.as_view(), name='add'),
    # For Class based view
    # path('add-lead/', views.add_lead, name='add_lead'),
]