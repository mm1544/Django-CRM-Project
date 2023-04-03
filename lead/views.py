# To be able to show message when e.g. lead is deleted
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddLeadForm
from .models import Lead

from client.models import Client
from team.models import Team

@login_required
def leads_list(request):
    # Want to get all the leads from database.
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

    return render(request, 'lead/leads_list.html', {
        'leads': leads,
    })

@login_required
def leads_detail(request, pk):
    # 'pk' --> primary key, ID of a lead on DB
    # 'filter(created_by=request.user)' --> to get only those leads, which belong to signed-in user.
    # v1
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
    # v2
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    return render(request, 'lead/leads_detail.html', {
        'lead': lead
    })

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'The lead "{}" was deleted.'.format(lead.name))

    return redirect('leads_list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        # (!!!) Need to pass 'instance=lead' so that DJ knows that we want to update the information, but NOT creating a ned lead.
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes were saved.')

            return redirect('leads_list')
        
    else:
        form = AddLeadForm(instance=lead)

    return render(request, 'lead/leads_edit.html', {'form': form})

@login_required # To require authentication
def add_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            # Creating new Lead
            # 'created_by' is not set yet, therefore we would get an error, therefore we need to pass 'ommit=False' - will prevent entry to be saved into database.
            lead = form.save(commit=False)
            # Logged-in user will be the person who creted this Lead.
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, 'The lead was created.')

            # After Lead creation we want to redirect user to Leads page where all the leads are listed.
            return redirect('leads_list') # Passing-in URL Name and DJ will take care of it.

    else:
        # It it is not a POST request, we will have an empty form.

        form = AddLeadForm()

    # If 'form.is_valid()' is not valid, then errors will be added to the Form, and Dj will show the error messages.
    return render(request, 'lead/add_lead.html', {
        'form': form,
        'team': team,
        })

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        team=team,
        )
    
    lead.converted_to_client = True
    lead.save()

    messages.success(request, 'The lead "{}" was converted to a client.'.format(lead.name))
    
    return redirect('leads_list')