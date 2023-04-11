from .models import Team

# Adding a custom context processor. Now I am able to use 'team' in each template. I will add change to 'tealcrm\settings.py' to 'TEMPLATES'
def team(request):
    team = Team.objects.filter(created_by=request.user)[0]

    return {'team': team}