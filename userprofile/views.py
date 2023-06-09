from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import Userprofile

from team.models import Team

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # print(str(form))

        # Creating user and userprofile if submited form is valid
        if form.is_valid():
            user = form.save()

            # For a new User it is mandatory to have a team.
            team = Team.objects.create(name='The team name', created_by=user) # 'request.user' doesn't exist yet, but 'user' exists
            team.members.add(user)
            team.save()

            Userprofile.objects.create(user=user, active_team=team)

            # Redirect to Login page
            return redirect('/log-in/')
    else:
        form = SignupForm()


    return render(request, 'userprofile/signup.html', {
        'form': form
        })

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')
