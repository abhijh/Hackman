from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from models import TeamForm, Team, Participant


def index(request):
    return render(request, "templates/portal/index.html")


@login_required(login_url='/')
def profile(request):
    return render(request, "templates/portal/profile.html", {"teams": Team.objects.all()})


@login_required(login_url='/')
def create(request):
    if request.method == "POST":
        team = TeamForm(request.POST)
        if team.is_valid():
            team.save()
            join_team(request)
        return redirect("/accounts/profile")
    else:
        return HttpResponse("This method is not allowed here.")


@login_required(login_url='/')
def join(request):
    join_team(request)
    return redirect("/accounts/profile")


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('/')


def join_team(request):
    team_name = request.POST.get("team_name")
    college = request.POST.get("college")
    contact = request.POST.get("contact")
    user = request.user
    team = Team.objects.get(team_name=team_name)
    participant = Participant(user=user, college=college, contact=contact, team=team)
    participant.save()