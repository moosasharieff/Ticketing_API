"""
# app/core/tests/test_admin.py

Test cases for modifying Django Admin Panel
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from unittest import skip # noqa


class AdminSiteTests(TestCase):
    """Test cases for Django Admin"""

    def setUp(self):
        """Setting up environment for the test cases."""

        # Creating user
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='userPassword@123',
            name='Test User'
        )

        # Creating Admin (Superuser)
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminPassword@123',
        )
        # Authenticating user to API calls
        self.client = Client()
        self.client.force_login(self.admin_user)

    def test_create_user_page(self):
        """Testing if user page is created.
        Note:
            core_user_add elaborates to:
            core -> Section name in Django Admin
            user -> Group name in Django Admin.
            add -> Means create user group in core section.

        """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        # Assertions
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # @skip('Test this in the end.')
    def test_users_list(self):
        """Testing if users are listed on
        Django Admin page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # Assertions
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    # @skip('Test this in the end.')
    def test_edit_user_page(self):
        """Test editing the user page.
        Note:
            core_user_change explains:
            core -> Section name in admin page
            user -> Group name in admin page
            change -> Means edit the group name of this section.

            """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        # Assertions
        self.assertEqual(res.status_code, status.HTTP_200_OK)
