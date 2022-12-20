from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


def password_validator(password1, password2):
    if len(password1) < 8:
        raise ValidationError('password is similar')
    if password1 != password2:
        raise ValidationError('passwords are not match')


def fullname_validator(full_name):
    try:
        u = User.objects.get(full_name=full_name)
    except User.DoesNotExist:
        u = None

    if u is not None:
        raise ValidationError('The name is exist')
