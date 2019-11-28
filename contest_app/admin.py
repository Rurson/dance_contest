from django.contrib import admin

from contest_app.models import Contest, Membership, Vote, Stage


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 3
    ordering = ['-member_type']


class ContestAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


class MembershipAdmin(admin.ModelAdmin):
    model = Membership
    ordering = ['contest', 'user']
    list_display = ['user', 'contest']


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0


class StageAdmin(admin.ModelAdmin):
    inlines = [VoteInline]


admin.site.register(Contest, ContestAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Vote)
admin.site.register(Stage, StageAdmin)
