from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from portal.models import Participant, Team


class ParticipantInline(admin.StackedInline):
    model = Participant
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ParticipantInline, )


class TeamAdmin(admin.ModelAdmin):
    class Meta:
        model = Team
    list_display = ['team_name', 'idea_title', 'idea_description']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)