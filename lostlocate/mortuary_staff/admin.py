from django.contrib import admin
from .models import MortuaryStaff

""" Register the MortuaryStaff model with the Django admin site"""
admin.site.register(MortuaryStaff)

# Import the admin site module from Django
from django.contrib import admin

""" Import the MortuaryStaff model from the current application's models"""
from .models import MortuaryStaff

""" Register the MortuaryStaff model with the Django admin site"""
""" This allows MortuaryStaff instances to be managed through the Django admin interface"""
admin.site.register(MortuaryStaff)

