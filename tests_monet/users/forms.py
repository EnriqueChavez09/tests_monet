from allauth.account.models import EmailAddress
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserChangeForm(UserChangeForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        self.save_m2m()
        last_email = EmailAddress.objects.filter(user=user).last()
        if last_email:
            last_email.email = user.email
            last_email.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save()
        EmailAddress.objects.create(
            user=user,
            email=user.email,
            verified=True,
            primary=True,
        )
        return user
