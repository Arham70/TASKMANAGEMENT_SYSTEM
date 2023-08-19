from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

model = CustomUser

list_display = ('email', 'password','first_name','last_name', 'is_active',
                'is_staff', 'is_superuser', 'last_login',)
list_filter = ('is_active', 'is_staff', 'is_superuser')
fieldsets = [
    (None, {'fields': ('username', 'email', 'password')}),
    ('Permissions', {'fields': ('is_staff', 'is_active',
                                'is_superuser', 'groups', 'user_permissions')}),
    ('Dates', {'fields': ('last_login', 'date_joined')})
]

admin.site.register(CustomUser)
