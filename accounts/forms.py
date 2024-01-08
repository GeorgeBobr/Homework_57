from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.core.exceptions import ValidationError

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise ValidationError('Хотя бы одно из полей first_name или last_name должно быть заполнено.')

        return cleaned_data