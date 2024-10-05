"""
# app/core/tests/test_models.py

All test cases for the models (Databases) will be written here.
"""

from django.test import TestCase
# Default User Model
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test case for all the models."""

    def test_create_user_with_email(self):
        """Test: Create a user successfully with email instead of username."""
        creds = {
            'email': 'test@example.com',
            'password': 'testPassword123',
        }

        # Create user
        user = get_user_model().objects.create_user(
            email=creds['email'],
            password=creds['password']
        )

        # Assertions
        self.assertEqual(user.email, creds['email'])
        self.assertTrue(user.check_password(creds['password']))
