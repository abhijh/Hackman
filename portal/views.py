from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.models import User
from models import TeamForm, Team, Participant


def index(request):
    return render(request, "templates/portal/index.html")


@login_required(login_url='/')
def profile(request):
    participant = Participant.objects.filter(user=request.user)
    if participant.count() == 0:
        print "Does not exist", request.user
        return render(request, "templates/portal/new_user.html", {"teams": Team.objects.all()})
    else:
        return render(request, "templates/portal/profile.html",
                      {"members": Participant.objects.filter(team=participant.first().team),
                       "participant": participant.first(),
                       "team": participant.first().team})


@login_required(login_url='/')
def create(request):
    if request.method == "POST":
        team = TeamForm(request.POST)
        if team.is_valid():
            team.save()
            join_team(request, is_approved=True)
        return redirect("/accounts/profile")
    else:
        return HttpResponse("This method is not allowed here.")


@login_required(login_url='/')
def join(request):
    if request.method == "POST":
        join_team(request)
        return redirect("/accounts/profile")
    else:
        return HttpResponse("This method is not allowed here.")


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def approve(request):
    users = request.POST.getlist("users")
    if users is not None:
        for user in users:
            participant = Participant.objects.filter(user=User.objects.filter(username=user).first()).first()
            participant.is_approved = True
            participant.save()
    return redirect("/accounts/profile/")


def join_team(request, is_approved=False, is_paid=False):
    team_name = request.POST.get("team_name")
    college = request.POST.get("college")
    contact = request.POST.get("contact")
    user = request.user
    team = Team.objects.get(team_name=team_name)
    participant = Participant(user=user, college=college, contact=contact, team=team, is_approved=is_approved,
                              is_paid=is_paid)
    participant.save()


@login_required(login_url='/')
def is_available(request):
    if Team.objects.filter(team_name=request.GET.get("team_name")).count():
        return HttpResponse(False)
    else:
        return HttpResponse(True)


@login_required(login_url='/')
def teams(request):
    user = request.user
    if user.is_superuser:
        teams = Team.objects.all()
        participants = Participant.objects.all()
    # if Team.objects.filter(team_name=request.GET.get("team_name")).count():
        return render(request, "templates/portal/teams.html", {"teams":teams, "participants":participants})
    else:
        return HttpResponse("Yu are not authorized for this area.")