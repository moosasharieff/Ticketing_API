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

    def test_user_email_normalized(self):
        """Test if the emails provided by the user are normalized
        and saved to the user model."""

        sample_emails = [
            ["Sample@EXAMPLE.COM", "Sample@example.com"],
            ["SamPle@Example.COM", "SamPle@example.com"],
            ["SamPLEe@example.COM", "SamPLEe@example.com"],
            ["SAMPLE@EXAMPLE.com", "SAMPLE@example.com"],
        ]

        # Assertions
        for wrong_email, correct_email in sample_emails:
            user = get_user_model().objects.create_user(
                email= wrong_email,
                password= 'testPassword@123'
            )

            # Assertions
            self.assertEqual(user.email, correct_email)