import logging

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# Initialize logging for the test suite
logger: logging.Logger = logging.getLogger(__name__)

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


class FaviconTests(TestCase):
    """
    Test suite for verifying frontend assets and visual identity markers.
    """

    def setUp(self) -> None:
        """
        Set up the test client before each test.
        """
        self.client: Client = Client()

    def test_homepage_contains_favicon(self) -> None:
        """
        Verifies that the root splash page renders successfully and
        includes the correct SVG favicon link tag representing the data analyst identity.
        """
        logger.info("Executing test_homepage_contains_favicon...")

        # Resolve the URL for the root splash page
        url: str = reverse("splash")
        response = self.client.get(url)

        # Ensure the page loads without server errors (HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Check that the specific static asset is referenced in the HTML payload
        expected_favicon_reference: str = "images/favicon.svg"
        self.assertContains(
            response,
            expected_favicon_reference,
            msg_prefix="The SVG favicon reference is missing from the base template.",
        )
        logger.info("Data analyst favicon correctly found in the homepage response.")
