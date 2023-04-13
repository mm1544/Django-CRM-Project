### Views in this file will be converted from Function Views to Class Views ###

# To be able to show message when e.g. lead is deleted
from django.contrib import messages
# For authentication (it is used in Class based views instead of 'dispatch')
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.views import View

from .forms import AddLeadForm, AddCommentForm, AddFileForm
from .models import Lead

from client.models import Client, Comment as ClientComment
from team.models import Team

## Custom Class based View (converted from function based view 'leads_list')
class LeadListView(LoginRequiredMixin, ListView):
    model = Lead

    ########### It is not needed becuase instead we use LoginRequiredMixin
    # # Needed for authentication
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    ###########

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, converted_to_client=False)


## Function based view (now converted into Class based view 'LeadListView')
# @login_required
# def leads_list(request):
#     # Want to get all the leads from database.
#     leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

#     return render(request, 'lead/leads_list.html', {
#         'leads': leads,
#     })


### Class based view
class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # Adding extra form to the DetailView
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        context['fileform'] = AddFileForm()

        return context
    
    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    

### Func based view
# @login_required
# def leads_detail(request, pk):
#     # 'pk' --> primary key, ID of a lead on DB
#     # 'filter(created_by=request.user)' --> to get only those leads, which belong to signed-in user.
#     # v1
#     # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
#     # v2
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

#     return render(request, 'lead/leads_detail.html', {
#         'lead': lead
#     })


### Class based view
class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    
    # We want to be able to delte leads created only by the logged in user.
    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))
    
    # Fixes error(?)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

### Func based view
# @login_required
# def leads_delete(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
#     lead.delete()

#     messages.success(request, 'The lead "{}" was deleted.'.format(lead.name))

#     return redirect('leads:list')


### Class based view
class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit lead'

        return context
    
    # We want to be able to update leads created only by the logged in user.
    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))


# ### Func based view
# @login_required
# def leads_edit(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

#     if request.method == 'POST':
#         # (!!!) Need to pass 'instance=lead' so that DJ knows that we want to update the information, but NOT creating a ned lead.
#         form = AddLeadForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()

#             messages.success(request, 'The changes were saved.')

#             return redirect('leads:list')
        
#     else:
#         form = AddLeadForm(instance=lead)

#     return render(request, 'lead/leads_edit.html', {'form': form})


### Class based view
class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.request.user.userprofile.active_team
        context['team'] = team
        context['title'] = 'Add lead'

        return context
    
    
    def form_valid(self, form):
        team = self.request.user.userprofile.active_team
        # Creating new Lead
        # 'created_by' is not set yet, therefore we would get an error, therefore we need to pass 'commit=False' - will prevent entry to be saved into database.
        self.object = form.save(commit=False)
        # 'self.object' is a new lead
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()

        # Redirecting to the front page of the Leads
        return redirect(self.get_success_url())


# ### Func based view
# @login_required # To require authentication
# def add_lead(request):
#     team = Team.objects.filter(created_by=request.user)[0]
#     if request.method == 'POST':
#         form = AddLeadForm(request.POST)

#         if form.is_valid():
#             team = Team.objects.filter(created_by=request.user)[0]
#             # Creating new Lead
#             # 'created_by' is not set yet, therefore we would get an error, therefore we need to pass 'commit=False' - will prevent entry to be saved into database.
#             lead = form.save(commit=False)
#             # Logged-in user will be the person who creted this Lead.
#             lead.created_by = request.user
#             lead.team = team
#             lead.save()

#             messages.success(request, 'The lead was created.')

#             # After Lead creation we want to redirect user to Leads page where all the leads are listed.
#             return redirect('leads:list') # Passing-in URL Name and DJ will take care of it.

#     else:
#         # It it is not a POST request, we will have an empty form.

#         form = AddLeadForm()

#     # If 'form.is_valid()' is not valid, then errors will be added to the Form, and Dj will show the error messages.
#     return render(request, 'lead/add_lead.html', {
#         'form': form,
#         'team': team,
#         })


class AddFileView(LoginRequiredMixin, View):
    # Because it will be a post request
    def post(self, request, *args, **kwargs):
        # Primary key
        pk = kwargs.get('pk')
        # 'request.FILES' (!!)
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            team = self.request.user.userprofile.active_team
            file = form.save(commit=False)
            file.team = team
            file.lead_id = pk
            file.created_by = request.user
            file.save()


            return redirect('leads:detail', pk=pk)



class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        content = request.POST.get('content')

        form = AddCommentForm(request.POST)

        if form.is_valid():
            team = self.request.user.userprofile.active_team
            # 'commit=False' because need to set a Team
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            # lead_id ?
            comment.lead_id = pk
            comment.save()


        return redirect('leads:detail', pk=pk)


### Class based view
class ConvertToClientView(LoginRequiredMixin, View):
    # Overwriting method
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        team = self.request.user.userprofile.active_team

        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by=request.user,
            team=team,
            )
        
        lead.converted_to_client = True
        lead.save()

        # Will convert all existing Lead Comments to the newly creted Client Comments
        comments = lead.comments.all()

        for comment in comments:
            ClientComment.objects.create(
                client = client,
                content = comment.content,
                created_by = comment.created_by,
                team = team,
                # created_at = comment.created_at,
            )

        messages.success(request, 'The lead "{}" was converted to a client.'.format(lead.name))
    
        return redirect('leads:list')


# ### Func based view
# @login_required
# def convert_to_client(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
#     team = Team.objects.filter(created_by=request.user)[0]

#     client = Client.objects.create(
#         name=lead.name,
#         email=lead.email,
#         description=lead.description,
#         created_by=request.user,
#         team=team,
#         )
    
#     lead.converted_to_client = True
#     lead.save()

#     messages.success(request, 'The lead "{}" was converted to a client.'.format(lead.name))
    
#     return redirect('leads:list')