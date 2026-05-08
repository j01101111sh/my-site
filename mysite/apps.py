from django.apps import AppConfig


class MysiteConfig(AppConfig):
    name = "mysite"

    def ready(self) -> None:
        """
        Import signals when the app is ready.
        """
        import mysite.signals  # noqa: F401
