"""
Restaurant application admin configuration.

This module registers models with the Django admin site,
allowing administrators to manage restaurant data through the admin interface.
"""

from django.contrib import admin
from .models import Menu, Booking


# Register Menu model for admin interface
# This allows CRUD operations on menu items through /admin
admin.site.register(Menu)

# Register Booking model for admin interface
# This allows viewing and managing reservations through /admin
admin.site.register(Booking)