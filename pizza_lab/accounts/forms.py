from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from pizza_lab.accounts.models import CustomUser  # type: ignore
from pizza_lab.accounts.models import Profile  # type: ignore

UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel

        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {'username': auth_forms.UsernameField}

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        if commit:
            profile.save()
        return user


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
