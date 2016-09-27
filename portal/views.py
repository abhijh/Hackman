from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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
                       "is_approved": participant.first().is_approved})


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


def join_team(request, is_approved=False):
    team_name = request.POST.get("team_name")
    college = request.POST.get("college")
    contact = request.POST.get("contact")
    user = request.user
    team = Team.objects.get(team_name=team_name)
    participant = Participant(user=user, college=college, contact=contact, team=team, is_approved=is_approved)
    participant.save()


def approve(user):
    participant = Participant.objects.filter(user=user)
    participant.first().is_approved = True
    participant.save()
