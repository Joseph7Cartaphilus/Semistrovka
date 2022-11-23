from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input your username', }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Input your password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input your name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input your surname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input your username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Input your email adress'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Input your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'
