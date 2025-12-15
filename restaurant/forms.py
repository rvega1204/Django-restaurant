"""
Restaurant application forms.

This module defines forms for the Little Lemon restaurant,
including the booking form for table reservations.
"""

from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    """
    Form for creating and editing table reservations.

    This ModelForm automatically generates form fields based on the Booking model,
    including all fields: first_name, last_name, guest_number, and comment.

    Attributes:
        Meta.model: Links to the Booking model
        Meta.fields: Includes all fields from the Booking model
    """

    class Meta:
        model = Booking
        fields = "__all__"
