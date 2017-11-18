import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_name(value):
    if value.__len__() < 2:
        raise ValidationError(
            _('%(value)s ist zu kurz um ein Vorname zu sein. Hast du dich vertippt?')
        )

