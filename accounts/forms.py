from django import forms
from django.contrib.auth.models import User


def get_username(user):
    if user:
        if user.__contains__('@'):
            return user.split('@')[0]
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = get_username(cleaned_data.get('username'))
        password = cleaned_data.get('password')
        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'The user with username {username} does not exist!')
        if not self.user.check_password(password):
            raise forms.ValidationError(f'Password for user {username} is not correct!')


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
