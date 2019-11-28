from django.contrib import admin

from contest_app.models import Contest, Membership, Vote


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 3
    ordering = ['-type']


class ContestAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


class MembershipAdmin(admin.ModelAdmin):
    model = Membership
    ordering = ['contest', 'user']
    list_display = ['user', 'contest']


admin.site.register(Contest, ContestAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Vote)
