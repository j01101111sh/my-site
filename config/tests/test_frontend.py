from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class FrontendTests(TestCase):
    """
    Unit tests for frontend template rendering and static asset inclusion.
    """

    def test_base_template_includes_theme_scripts(self) -> None:
        """
        Test that the base template includes the necessary JS and CSS for dark mode.
        """
        response = self.client.get(reverse("splash"))

        self.assertEqual(response.status_code, 200)

        content = response.content.decode("utf-8")

        # Check for Bootstrap Icons
        self.assertIn("bootstrap-icons.css", content)

        # Check for Theme JS
        # Use regex to handle both standard filenames (dev) and hashed filenames (CI/prod)
        # Matches: js/theme.js OR js/theme.1234abcd.js
        self.assertRegex(content, r"js/theme(\.[a-f0-9]+)?\.js")

        # Check for inline script for FOUC prevention
        self.assertIn("data-bs-theme", content)

    def test_navbar_includes_toggle(self) -> None:
        """
        Test that the navbar includes the theme toggle button.
        """
        response = self.client.get(reverse("splash"))
        self.assertEqual(response.status_code, 200)
        content = response.content.decode("utf-8")

        # Check for the button ID
        self.assertIn('id="theme-toggle"', content)
