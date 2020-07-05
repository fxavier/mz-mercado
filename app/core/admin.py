from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User


#
# def make_refund_accepted(modeladmin, request, queryset):
#     queryset.update(refund_requested=False, refund_granted=True)
#
#
# make_refund_accepted.short_description = 'Update orders to refund granted'


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'nome']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('nome',)}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser')}
         ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)