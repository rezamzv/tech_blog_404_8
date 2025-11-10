from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from accounts.forms import CustomUserChangeForm , CustomUserCreationForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets
    list_display = ['email','username', 'is_staff', 'is_active']

admin.site.register(CustomUser,CustomUserAdmin)