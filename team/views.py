from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TeamForm
from .models import Team

@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)

    # Need to save this form if we press 'submit' button
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes were saved.')

            # Return/redirect user back to 'myaccount' page.
            return redirect('userprofile:myaccount')
    else:
        form = TeamForm(instance=team) # To pull out the data of certain team into the form we need to pass-in 'instance=team'

    return render(request, 'team/edit_team.html', {
        'team': team,
        'form': form,
    })