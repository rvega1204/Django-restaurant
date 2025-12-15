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
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success reservation!')
            return redirect('book')  # Redirect to clear form and show message
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

    Raises:
        Menu.DoesNotExist: If the menu item with given pk doesn't exist
    """
    if pk is not None:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = None

    return render(request, 'menu_item.html', {'menu_item': menu_item})
