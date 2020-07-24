from django.contrib import admin
from .models import Membership, UserMembership, Subscription


class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership')


admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(Membership)
admin.site.register(Subscription)
