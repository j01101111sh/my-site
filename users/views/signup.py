import logging

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm

User = get_user_model()
logger = logging.getLogger(__name__)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  # Assuming 'login' URL will exist
    template_name = "registration/signup.html"

    @staticmethod
    def _mask_email(email: str) -> str:
        masked_email = email
        if "@" in email:
            local, domain = email.rsplit("@", 1)
            if len(local) > 2:
                masked_email = f"{local[0]}{'*' * (len(local) - 2)}{local[-1]}@{domain}"
            elif len(local) == 2:
                masked_email = f"{local[0]}*@{domain}"
            elif len(local) == 1:
                masked_email = f"*@{domain}"
        return masked_email
