import re
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator 

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
    

def validate_phone(value):
    reg = re.compile(r'^\+?\s?\(?[0-9]*\)?\s?[0-9]{10}$')
    if not reg.match(value):
        raise ValidationError('Please enter valid details')
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

