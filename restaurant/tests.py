from django.test import TestCase, Client
from django.urls import reverse
from .models import Booking, Menu
from .forms import BookingForm


# Tests for Booking model
class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            first_name='John',
            last_name='Doe',
            guest_number=4,
            comment='Special occasion'
        )

    def test_booking_creation(self):
        """Test that a booking can be created"""
        self.assertEqual(self.booking.first_name, 'John')
        self.assertEqual(self.booking.last_name, 'Doe')
        self.assertEqual(self.booking.guest_number, 4)
        self.assertEqual(self.booking.comment, 'Special occasion')

    def test_booking_str(self):
        """Test the __str__ method of Booking"""
        self.assertEqual(str(self.booking), 'John Doe')


# Tests for Menu model
class MenuModelTest(TestCase):

    def setUp(self):
        self.menu_item = Menu.objects.create(
            name='Pizza',
            price=15,
            description='Delicious pizza'
        )

    def test_menu_creation(self):
        """Test that a menu item can be created"""
        self.assertEqual(self.menu_item.name, 'Pizza')
        self.assertEqual(self.menu_item.price, 15)
        self.assertEqual(self.menu_item.description, 'Delicious pizza')

    def test_menu_str(self):
        """Test the __str__ method of Menu"""
        self.assertEqual(str(self.menu_item), 'Pizza')


# Tests for BookingForm
class BookingFormTest(TestCase):

    def test_booking_form_valid(self):
        """Test that form is valid with correct data"""
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'guest_number': 2,
            'comment': 'Birthday dinner'
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid_empty(self):
        """Test that form is invalid without data"""
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())

    def test_booking_form_saves_correctly(self):
        """Test that form saves correctly"""
        form_data = {
            'first_name': 'Alice',
            'last_name': 'Johnson',
            'guest_number': 3,
            'comment': 'Anniversary'
        }
        form = BookingForm(data=form_data)
        if form.is_valid():
            booking = form.save()
            self.assertEqual(booking.first_name, 'Alice')
            self.assertEqual(Booking.objects.count(), 1)


# Tests for views
class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        Menu.objects.create(name='Pasta', price=12, description='Fresh pasta')
        Menu.objects.create(name='Salad', price=8, description='Green salad')

    def test_home_view(self):
        """Test that home view loads correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        """Test that about view loads correctly"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_book_view_get(self):
        """Test that book view loads the form"""
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')
        self.assertIsInstance(response.context['form'], BookingForm)

    def test_book_view_post_valid(self):
        """Test that a valid booking can be submitted"""
        form_data = {
            'first_name': 'Bob',
            'last_name': 'Williams',
            'guest_number': 5,
            'comment': 'Group dinner'
        }
        response = self.client.post(reverse('book'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.first_name, 'Bob')

    def test_book_view_post_invalid(self):
        """Test that invalid form does not save"""
        form_data = {
            'first_name': '',  # Empty field
            'last_name': 'Brown',
            'guest_number': 2,
            'comment': 'Test'
        }
        response = self.client.post(reverse('book'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Does not redirect
        self.assertEqual(Booking.objects.count(), 0)  # Not saved
        # Check that error message is displayed
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(str(messages_list[0]), 'Please correct the errors below.')

    def test_book_view_success_message(self):
        """Test that success message includes customer name"""
        form_data = {
            'first_name': 'Sarah',
            'last_name': 'Connor',
            'guest_number': 2,
            'comment': 'Window seat please'
        }
        response = self.client.post(reverse('book'), data=form_data, follow=True)
        # Check success message
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 1)
        self.assertIn('Sarah Connor', str(messages_list[0]))

    def test_menu_view(self):
        """Test that menu view displays all items"""
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertEqual(len(response.context['menu']), 2)

    def test_display_menu_item_view(self):
        """Test that a specific menu item can be viewed"""
        menu_item = Menu.objects.first()
        response = self.client.get(reverse('menu_item', args=[menu_item.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_item.html')
        self.assertEqual(response.context['menu_item'].name, 'Pasta')

    def test_display_menu_item_view_not_found(self):
        """Test that menu_item view handles non-existent objects"""
        # This test verifies that the view redirects when item doesn't exist
        response = self.client.get(reverse('menu_item', args=[999]))
        self.assertEqual(response.status_code, 302)  # Redirects to menu
        self.assertEqual(response.url, reverse('menu'))  # Redirects to menu page

    def test_display_menu_item_error_message(self):
        """Test that error message is shown for non-existent menu item"""
        response = self.client.get(reverse('menu_item', args=[999]), follow=True)
        messages_list = list(response.context['messages'])
        self.assertEqual(len(messages_list), 1)
        self.assertIn('not found', str(messages_list[0]).lower())


# Integration tests
class IntegrationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_booking_workflow(self):
        """Test complete booking workflow"""
        # 1. Access booking page
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)

        # 2. Submit booking form
        form_data = {
            'first_name': 'Charlie',
            'last_name': 'Davis',
            'guest_number': 6,
            'comment': 'Family reunion'
        }
        response = self.client.post(reverse('book'), data=form_data)

        # 3. Verify redirect
        self.assertEqual(response.status_code, 302)

        # 4. Verify booking was saved
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.first_name, 'Charlie')
        self.assertEqual(booking.guest_number, 6)
