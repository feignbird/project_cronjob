from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
admin.site.unregister(User)


class UserAdminAdv(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')
    list_search = ('username', 'first_name', 'last_name', 'email')


admin.site.register(User, UserAdminAdv)
