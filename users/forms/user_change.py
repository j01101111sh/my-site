from django.contrib.auth.forms import UserChangeForm

from users.models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("bio", "location", "website")
