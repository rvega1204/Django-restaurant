# Little Lemon Restaurant

A Django web application for managing a restaurant's online presence, including menu display and table reservations.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Models](#database-models)
- [URL Routes](#url-routes)
- [Testing](#testing)
- [Admin Interface](#admin-interface)
- [UI Features](#ui-features)
- [Code Documentation](#code-documentation)
- [Error Handling](#error-handling)
- [Security Features](#security-features)
- [Contributing](#contributing)

## 🎯 Overview

Little Lemon is a full-featured restaurant website built with Django 4.1. It allows customers to browse the menu, view individual dishes, and make table reservations. The application includes an admin interface for managing menu items and viewing reservations.

## ✨ Features

- **Homepage**: Welcome page with restaurant information
- **About Page**: Details about the restaurant
- **Menu Display**: Browse all available menu items
- **Menu Item Details**: View detailed information about specific dishes
- **Table Reservations**:
  - Online booking form with CSRF protection
  - Advanced form validation with error handling
  - Success notifications with auto-dismiss (3 seconds)
  - Error notifications with visual feedback
  - Automatic form clearing after submission
  - Personalized success messages with customer name
- **Error Handling**:
  - Try-catch blocks for database operations
  - Graceful handling of non-existent menu items
  - User-friendly error messages
  - Color-coded notifications (green for success, red for errors)
- **Admin Panel**: Manage menu items and reservations
- **Responsive Design**: Mobile-friendly interface
- **Comprehensive Test Suite**: 18 automated tests covering models, forms, views, error handling, and integration
- **Code Documentation**: Complete docstrings following Google style guide

## 🛠 Tech Stack

- **Backend**: Django 4.1.1
- **Language**: Python 3.12.6
- **Database**: SQLite (default, configurable)
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Django Templates

## 📁 Project Structure

```
littlelemon/
├── littlelemon/           # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── restaurant/            # Main application
│   ├── models.py         # Database models (Booking, Menu)
│   ├── views.py          # View functions with error handling
│   ├── forms.py          # Forms (BookingForm)
│   ├── urls.py           # App URL patterns
│   ├── admin.py          # Admin configuration
│   ├── tests.py          # Test suite (18 tests)
│   └── templates/        # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── about.html
│       ├── book.html
│       ├── menu.html
│       └── menu_item.html
├── db.sqlite3            # Database file
├── manage.py             # Django management script
└── README.md             # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.12+ installed
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone or navigate to the project directory**

2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 💻 Usage

### For Customers

1. **Browse Menu**: Navigate to `/menu/` to see all available dishes
2. **View Dish Details**: Click on any menu item to see detailed information
3. **Make a Reservation**:
   - Go to `/book/`
   - Fill in the reservation form:
     - First Name
     - Last Name
     - Number of Guests
     - Special Comments/Requests
   - Submit the form
   - See a success notification (auto-dismisses after 3 seconds)

### For Administrators

1. **Access Admin Panel**: Go to `/admin/` and log in
2. **Manage Menu Items**:
   - Add, edit, or delete menu items
   - Set name, price, and description
3. **View Reservations**:
   - See all customer bookings
   - View guest details and special requests

## 📊 Database Models

### Booking Model
Represents a table reservation.

**Fields:**
- `first_name` (CharField): Customer's first name (max 200 chars)
- `last_name` (CharField): Customer's last name (max 200 chars)
- `guest_number` (IntegerField): Number of guests
- `comment` (CharField): Special requests or comments (max 1000 chars)

### Menu Model
Represents a menu item/dish.

**Fields:**
- `name` (CharField): Dish name (max 255 chars)
- `price` (IntegerField): Price in dollars
- `description` (CharField): Dish description (max 1000 chars)

## 🌐 URL Routes

| URL Pattern | View | Name | Description |
|------------|------|------|-------------|
| `/` | `home` | home | Homepage |
| `/about/` | `about` | about | About page |
| `/book/` | `book` | book | Reservation form |
| `/menu/` | `menu` | menu | All menu items |
| `/menu_item/<int:pk>/` | `display_menu_item` | menu_item | Single menu item |

## 🧪 Testing

The project includes a comprehensive test suite with **18 tests** covering:

### Test Categories

1. **Model Tests** (4 tests)
   - Booking model creation and string representation
   - Menu model creation and string representation

2. **Form Tests** (3 tests)
   - Valid form submission
   - Invalid/empty form handling
   - Correct data saving

3. **View Tests** (10 tests)
   - Homepage loading
   - About page loading
   - Booking form display (GET)
   - Valid booking submission (POST)
   - Invalid booking handling with error messages
   - Success message personalization (includes customer name)
   - Menu list display
   - Menu item detail view
   - Non-existent menu item error handling with redirect
   - Error message display for missing menu items

4. **Integration Tests** (1 test)
   - Complete booking workflow end-to-end

### Running Tests

```bash
# Run all tests
python manage.py test restaurant

# Run specific test class
python manage.py test restaurant.tests.BookingModelTest

# Run specific test
python manage.py test restaurant.tests.ViewsTest.test_book_view_post_valid

# Run with verbose output
python manage.py test restaurant --verbosity=2
```

### Test Coverage

- **Models**: 100% coverage
- **Forms**: 100% coverage
- **Views**: 100% coverage (including error handling)
- **Error Handling**: Comprehensive coverage
- **Integration**: Full booking workflow tested

## 🔧 Admin Interface

The admin interface (`/admin/`) provides management capabilities for:

### Registered Models

1. **Menu**
   - CRUD operations for menu items
   - Manage dish names, prices, and descriptions

2. **Booking**
   - View all reservations
   - Access customer information
   - Read special requests and comments

### Admin Features

- User-friendly interface
- Search and filter capabilities
- Bulk actions
- Change history tracking

## 🎨 UI Features

### Notification System

- **Success Notifications**:
  - Fixed position toast notification (top-right)
  - Green background (#4CAF50) with checkmark icon (✓)
  - Personalized message with customer name
  - Smooth slide-in animation from right
  - Auto-dismiss after 3 seconds
  - Fade-out transition effect

- **Error Notifications**:
  - Same positioning and animation as success
  - Red background (#f44336) with X icon (✗)
  - Clear, user-friendly error messages
  - Auto-dismiss after 3 seconds

### Form Behavior

- **Validation**:
  - Real-time form validation
  - Error messages for invalid data
  - Required field enforcement

- **Submission**:
  - Automatic form clearing after successful submission
  - POST-Redirect-GET pattern to prevent duplicate submissions
  - CSRF protection enabled
  - Try-catch error handling for database operations

## 📝 Code Documentation

All Python files include comprehensive documentation:

- **Module-level docstrings**: Describe file purpose
- **Class docstrings**: Explain model/form functionality
- **Function docstrings**: Detail parameters, returns, and exceptions
- **Inline comments**: Clarify complex logic

Documentation follows Google-style Python docstring conventions.

## ⚠️ Error Handling

The application implements robust error handling throughout:

### Booking System Errors

1. **Database Save Errors**:
   - Try-catch blocks around all database operations
   - User-friendly error messages displayed
   - Error logging for debugging purposes
   - Form data preserved on error

2. **Form Validation Errors**:
   - Empty or invalid fields are caught before submission
   - Clear error messages guide user corrections
   - Red error notifications with visual feedback

### Menu System Errors

1. **Non-Existent Menu Items**:
   - Graceful handling of invalid menu item IDs
   - Automatic redirect to menu page
   - Error notification explaining the issue
   - No application crashes or 500 errors

### Error Message Types

| Error Type | Color | Icon | Behavior |
|-----------|-------|------|----------|
| Validation Error | Red (#f44336) | ✗ | Shows validation message |
| Database Error | Red (#f44336) | ✗ | Shows generic error message |
| Not Found Error | Red (#f44336) | ✗ | Redirects + shows message |
| Success | Green (#4CAF50) | ✓ | Shows personalized message |

## 🔒 Security Features

- CSRF protection on all forms
- Secret key management (change in production!)
- Django's built-in SQL injection protection
- XSS protection via template auto-escaping
- Exception handling to prevent sensitive error exposure

## 🚧 Development Notes

### Debug Mode

Currently running in DEBUG mode. **Important**: Set `DEBUG = False` in production!

### Database

Using SQLite for development. For production, consider:
- PostgreSQL
- MySQL
- MariaDB

### Static Files

Static files are served by Django's development server. For production:
```bash
python manage.py collectstatic
```

## 📄 Files Overview

### Core Python Files

- **models.py**: Database schema definitions with comprehensive docstrings
- **views.py**: Request handling, business logic, and error handling
- **forms.py**: Form definitions and validation rules
- **urls.py**: URL routing configuration with comments
- **admin.py**: Admin interface customization (Menu & Booking models)
- **tests.py**: Automated test suite with 18 tests

### Templates

- **base.html**: Base template with common layout
- **index.html**: Homepage
- **about.html**: About page
- **book.html**: Reservation form with success/error notifications
- **menu.html**: Menu items list
- **menu_item.html**: Individual dish details

### Configuration Files

- **.gitignore**: Comprehensive gitignore for Django projects
- **README.md**: Complete project documentation
- **manage.py**: Django management script

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Include docstrings for all functions and classes (Google style)
- Write tests for new features
- Keep comments in English
- Add error handling for new views

## 📧 Support

For issues or questions, please open an issue in the project repository.

## 🙏 Acknowledgments

- Django Documentation
- Django Community

---

**Version**: 1.0.0
**Django Version**: 4.1.1
**Python Version**: 3.12.6
**Last Updated**: December 2025
