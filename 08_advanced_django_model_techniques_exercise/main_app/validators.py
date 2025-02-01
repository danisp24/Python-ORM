from django.core.exceptions import ValidationError


def ValidateName(value):
    for char in value:
        if not (char.isalpha() or char.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def ValidatePhoneNumber(value):

    if value[:4] != '+359' or len(value) != 13:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
