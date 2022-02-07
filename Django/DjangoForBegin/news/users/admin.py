from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomeUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff',]


admin.site.register(CustomUser, CustomUserAdmin)
