from django.contrib import admin

from contest_app.models import Contest, Membership


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 3


class ContestAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


admin.site.register(Contest, ContestAdmin)
admin.site.register(Membership)
