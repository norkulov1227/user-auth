from django.core.validators import RegexValidator


phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Phone number must be entered in the format: '+998XXXXXXXXX'. Exactly 13 characters allowed."
    )
