import uuid as uuid_lib

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse



class ProfileManager(models.Manager):

    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    joined = models.DateTimeField("Date Joined", auto_now_add=True)
    img = models.ImageField(upload_to='profiles/profile_pictures',
                            default='/profiles/profile_pictures/default_profile_picture.png')
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    objects = ProfileManager()

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('profile')

    def get_update_url(self):
        return reverse('profile_update')

    def natural_key(self):
        return (self.slug,)
    natural_key.dependencies = ['user.user']



