from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from allauth.account.forms import LoginForm, SignupForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "first_name",
            "last_name",
        )


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget = forms.EmailInput(
            attrs={
                "type": "email",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "",
                "name": "email",
                "id": "email",
            }
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "",
                "name": "password",
                "id": "password",
            }
        )


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=50,
        label="First Name:",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "First Name",
                "name": "first_name",
                "id": "first_name",
            }
        ),
    )
    middle_name = forms.CharField(
        max_length=50,
        label="Middle Name:",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "Middle Name",
                "name": "middle_name",
                "id": "middle_name",
                "required": False,
            }
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        label="Last Name:",
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "Last Name",
                "name": "last_name",
                "id": "last_name",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "type": "email",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "Email",
                "name": "email",
                "id": "email",
            }
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "Password",
                "name": "password1",
                "id": "password1",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "border border-gray-200 rounded-full w-full pl-2 py-1 focus:outline-indigo-400",
                "placeholder": "Confirm password",
                "name": "password2",
                "id": "password2",
            }
        )
        self.fields["email"].label = "Email:"
        self.fields["password1"].label = "Password:"
        self.fields["password2"].label = "Confirm Password:"

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.middle_name = self.cleaned_data["middle_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
