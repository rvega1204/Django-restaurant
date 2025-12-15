"""
Restaurant application views.

This module contains all the view functions for the Little Lemon restaurant
website, handling requests for home, about, bookings, and menu pages.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Menu


def home(request):
    """
    Display the homepage.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered index.html template
    """
    return render(request, 'index.html')


def about(request):
    """
    Display the about page with restaurant information.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered about.html template
    """
    return render(request, 'about.html')


def book(request):
    """
    Handle table booking requests.

    Displays the booking form on GET requests. On POST requests, validates
    and saves the booking, then redirects to show a success message.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered book.html template with form context
        HttpResponseRedirect: Redirect to booking page on successful submission
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                # Attempt to save the booking
                booking = form.save()
                messages.success(
                    request,
                    f'Success reservation for {booking.first_name} {booking.last_name}!'
                )
                return redirect('book')  # Redirect to clear form and show message
            except Exception as e:
                # Handle any database or save errors
                messages.error(
                    request,
                    'An error occurred while saving your reservation. Please try again.'
                )
                # Log the error for debugging (in production, use proper logging)
                print(f"Booking save error: {str(e)}")
        else:
            # Form validation failed
            messages.error(
                request,
                'Please correct the errors below.'
            )
    else:
        # GET request - create empty form
        form = BookingForm()

    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    """
    Display all menu items.

    Retrieves all menu items from the database and displays them.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: Rendered menu.html template with menu items context
    """
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_items})


def display_menu_item(request, pk=None):
    """
    Display a specific menu item by primary key.

    Args:
        request: HttpRequest object
        pk (int, optional): Primary key of the menu item. Defaults to None.

    Returns:
        HttpResponse: Rendered menu_item.html template with menu item context
        HttpResponseRedirect: Redirect to menu page if item not found
    """
    menu_item = None

    if pk is not None:
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            # Item not found - show error and redirect to menu
            messages.error(request, f'Menu item with ID {pk} not found.')
            return redirect('menu')

    return render(request, 'menu_item.html', {'menu_item': menu_item})
