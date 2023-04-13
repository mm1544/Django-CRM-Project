from .models import Team

# Adding a custom context processor. Now I am able to use 'team' in each template. I will add change to 'tealcrm\settings.py' to 'TEMPLATES'
def active_team(request):
    if request.user.is_authenticated:
        if request.user.userprofile.active_team:
            # Selecting an 'active' team
            active_team = request.user.userprofile.active_team
        else:
            # Selecting first team in the list...
            active_team = Team.objects.filter(created_by=request.user)[0]
    else:
        active_team = None

    return {'active_team': active_team}