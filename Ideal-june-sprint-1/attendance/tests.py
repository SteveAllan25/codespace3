from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Attendance

User = get_user_model()

class AttendanceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            user_type='community'
        )
        self.client.login(username='testuser', password='password123')

    def test_check_in(self):
        response = self.client.post(reverse('check-in'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Attendance.objects.count(), 1)

    def test_double_check_in(self):
        self.client.post(reverse('check-in'))
        response = self.client.post(reverse('check-in'))
        self.assertEqual(response.status_code, 400)

    def test_check_out_without_check_in(self):
        response = self.client.post(reverse('check-out'))
        self.assertEqual(response.status_code, 400)

    def test_check_out_success(self):
        self.client.post(reverse('check-in'))
        response = self.client.post(reverse('check-out'))
        self.assertEqual(response.status_code, 200)
        attendance = Attendance.objects.first()
        self.assertIsNotNone(attendance.check_out)
