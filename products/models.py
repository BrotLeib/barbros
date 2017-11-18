import uuid as uuid_lib

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Product(models.Model):
    BIKE = 'BK'
    ELECTRONIC = 'EL'
    CAR = 'CA'
    OTHER = 'OT'
    PRODUCT_TYPE_CHOICES = (
        (BIKE, 'BIKE'),
        (ELECTRONIC, 'TECHNIK'),
        (CAR, 'AUTO'),
        (OTHER, 'ANDERE'),
    )
    OWNED = 'OW'
    STOLEN = 'NO'
    PRODUCT_STATUS_CHOICES = (
        (OWNED, 'OWNED'),
        (STOLEN, 'STOLEN')
    )
    register_date = models.DateTimeField(auto_now_add=True)
    zip_code = models.CharField(max_length=6)
    key = models.CharField(max_length=6, unique=True)
    slug = models.SlugField(max_length=31, unique=True, blank=True, help_text='A label for the URL config')
    type = models.CharField(max_length=2, choices=PRODUCT_TYPE_CHOICES, default=BIKE)
    status = models.CharField(max_length=2, choices=PRODUCT_STATUS_CHOICES, default=OWNED)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False) # if product has be found within the last hours/days
    for_sale = models.BooleanField(default=False)
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type + self.key)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['register_date']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('product_detail', kwargs = {'slug': self.slug})
