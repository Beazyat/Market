from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    A form class that inherits from UserCreationForm and is used to create a new user account.
    The form contains five fields: username, email, password1, password2, and class.

    The username field is a CharField widget that has a placeholder attribute with the value "Your username" and a class attribute with the value "w-full py-4 px-6 rounded-xl". This means that the input field will have a full width, a padding of 4 pixels on all sides, and a border radius of 12 pixels.

    The email field is a CharField widget that has a placeholder attribute with the value "Your email" and a class attribute with the value "w-full py-4 px-6 rounded-xl".

    The password1 and password2 fields are CharField widgets that have a placeholder attribute with the value "Your password" and a class attribute with the value "w-full py-4 px-6 rounded-xl".

    Overall, the SignupForm class provides a simple and intuitive interface for creating a new user account, with clear labels, placeholders, and styling to help users easily understand what information is required and how to enter it.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    # with widget you can write html code in there.
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Your email',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm password',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))

    '''
    beray sakht form login niaz nist ke barash view benevisi ya form khasi serfan
    bayad module 'AuthenticationForm' ro add bedi va formet ro ba on besazi.
    '''
