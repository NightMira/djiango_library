from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя:
    - username (login)
    - email
    - full_name
    - phone
    - password1 / password2
    """

    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'phone',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Bootstrap оформление всех полей
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })

    def clean_email(self):
        """
        Проверка уникальности email
        """
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")

        return email

    def save(self, commit=True):
        """
        Сохранение пользователя
        """
        user = super().save(commit=False)

        user.email = self.cleaned_data.get('email')
        user.full_name = self.cleaned_data.get('full_name')
        user.phone = self.cleaned_data.get('phone') or ""

        if commit:
            user.save()

        return user