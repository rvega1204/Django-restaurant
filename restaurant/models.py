"""
Restaurant application models.

This module defines the database models for the Little Lemon restaurant,
including table reservations and menu items.
"""

from django.db import models


class Booking(models.Model):
    """
    Model representing a table reservation at the restaurant.

    Attributes:
        first_name (str): Customer's first name (max 200 characters)
        last_name (str): Customer's last name (max 200 characters)
        guest_number (int): Number of guests for the reservation
        comment (str): Additional comments or special requests (max 1000 characters)
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        """Return string representation of the booking (full name)."""
        return self.first_name + ' ' + self.last_name


class Menu(models.Model):
    """
    Model representing a menu item at the restaurant.

    Attributes:
        name (str): Name of the dish (max 255 characters)
        price (int): Price of the dish in dollars
        description (str): Detailed description of the dish (max 1000 characters)
    """
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        """Return string representation of the menu item (name)."""
        return self.name