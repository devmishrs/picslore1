from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
#from .forms import UserAdminChangeForm, UserAdminCreationForm
from .forms import CustomUserCreationForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    form = UserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('first_name','username','is_active','is_staff', 'is_superuser')

    list_filter = ('is_superuser','is_active',)

    '''
    fieldsets = (
        (None, {'fields': ('first_name','email','password')}),
        ('Personal info': {'fields':()}),
        ('Permissions': {'fields':('is_superuser','is_staff', 'is_active')}),
    )
    '''
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number')}),
        ('Permissions', {'fields': ('is_superuser','is_staff','is_active',)}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2'),
        }),
    )

    ordering =('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

