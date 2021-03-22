import re
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, RegexValidator


def check_file_size(value):
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 3 MB.')


validator_fn = [
    RegexValidator(r'[A-Z]([A-Z]?)[0-9]{2}([A-Z]?)([A-Z]?)([A-Z]?)[0-9]{3}([0-9]?){4}',
                   "Enter your Roll number(in correct "
                   "format like eg. B17CS006 ). "
                   "This will be used to login "),
    RegexValidator(r'[A-Z]{2}[0-9]{2}[A-Z]([A-Z]?)([a-z]?)[A-Z][0-9]{3}',
                   "Enter your Roll number(in correct "
                   "format like eg. MT19VSS006 ). "
                   "This will be used to login ")
]


def regex_validators(value):
    err = None
    for validator in validator_fn:
        try:
            validator(value)
            return value
        except ValidationError as exc:
            err = exc
    raise err


def validate_year(value):
    reg = re.compile(r'[1-5]')
    if not reg.match(value):
        raise ValidationError('Please enter a value between 1-5')
    return value


def validate_gpa(value):
    reg = re.compile(r'^\d\.?\d*$')
    if not reg.match(value):
        raise ValidationError('This field should contain only numeric values')
    return value


def validate_pincode(value):
    reg = re.compile(r'^[1-9]{1}[0-9]{2}\s?[0-9]{3}$')
    if not reg.match(value):
        raise ValidationError('Please enter a valid pincode')
    return value


def validate_domain(value):
    reg = re.compile(r'^[a-zA-Z\s]+$')
    if not reg.match(value):
        raise ValidationError('Please enter a valid domain name')
    return value


def validate_url(value):
    validator = URLValidator(message='Please enter a valid url')
    try:
        validator(value)
        return value
    except ValidationError:
        raise ValidationError('Please enter a valid url')
