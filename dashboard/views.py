from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# '@login_required' - Django decorator which will redirect user to login page if you are not authenticated.
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')