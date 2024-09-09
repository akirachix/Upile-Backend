from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom admin class for managing CustomUser in the Django admin interface
class CustomUserAdmin(UserAdmin):
    model = CustomUser  # Specify the model that this admin class manages
    
    # Fields to be displayed in the list view of the admin interface
    list_display = (
        'username',  # Username of the user
        'email',     # Email address of the user
        'first_name', # First name of the user
        'last_name',  # Last name of the user
        'is_staff',   # Indicates if the user is a staff member
        'is_active',  # Indicates if the user account is active
        'phone_number', # Phone number of the user
        'role'        # Role of the user (e.g., police officer, mortuary staff)
    )
    
    list_filter = (
        'is_staff',    # Filter by whether the user is a staff member
        'is_superuser', # Filter by whether the user is a superuser
        'is_active',   # Filter by whether the user account is active
        'groups'       # Filter by user groups
    )
    
    # Ordering of users in the list view based on the username
    ordering = ('username',)

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
