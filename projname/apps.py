from django.apps import AppConfig


class ProjNameConfig(AppConfig):
    name = "projname"

    def ready(self) -> None:
        """
        Import signals when the app is ready.
        """
        import projname.signals  # noqa: F401
