from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Userprofile

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # print(str(form))

        # Creating user and userprofile if submited form is valid
        if form.is_valid():
            user = form.save()

            Userprofile.objects.create(user=user)

            # Redirect to Login page
            return redirect('/log-in/')
    else:
        form = UserCreationForm()


    return render(request, 'userprofile/signup.html', {'form': form})