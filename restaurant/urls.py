"""
Restaurant application URL configuration.

This module defines URL patterns for the Little Lemon restaurant website,
mapping URLs to their corresponding view functions.
"""

from django.urls import path
from . import views

# URL patterns for the restaurant app
urlpatterns = [
    # Homepage - displays landing page
    path('', views.home, name="home"),

    # About page - restaurant information
    path('about/', views.about, name="about"),

    # Booking page - table reservation form
    path('book/', views.book, name="book"),

    # Alternative home path
    path('home/', views.home, name="home"),

    # Menu page - displays all menu items
    path('menu/', views.menu, name="menu"),

    # Individual menu item detail page
    # <int:pk> captures the menu item's primary key as an integer
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]