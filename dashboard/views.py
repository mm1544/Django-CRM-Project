from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# '@login_required' - Django decorator which will redirect user to login page if you are not authenticated.
# In this way we make sure that unauthenticated users not accessing this view.
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')