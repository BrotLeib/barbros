from datetime import date
import uuid as uuid_lib

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
    PermissionsMixin)
from django.db import models
from django.utils.text import slugify

from profiles.models import Profile
from .validators import validate_name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
            self, email, password, **kwargs):
        '''
        helper function for creating a user
        creates a user and profile
        '''
        email = self.normalize_email(email)
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop(
            'is_superuser', False)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        self._create_profile(user)
        return user

    def _create_profile(self, user):
        slug = slugify('{}-{}'.format(user.first_name, user.last_name))
        profile = Profile.objects.create(user=user, slug=slug)
        return profile

    def create_user(
            self, email, password=None,
            **extra_fields):
        return self._create_user(
            email, password, **extra_fields)

    def create_superuser(
            self, email, password,
            **extra_fields):
        return self._create_user(
            email, password,
            is_staff=True, is_superuser=True,
            **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=254, unique=True)
    first_name = models.CharField(max_length=255, validators=[validate_name])
    last_name = models.CharField(max_length=255, validators=[validate_name])
    is_staff = models.BooleanField('staff status', default=False, help_text=(
            'Designates whether the user can '
            'log into this admin site.'))
    is_active = models.BooleanField('active', default=True, help_text=(
            'Designates whether this user should '
            'be treated as active. Unselect this '
            'instead of deleting accounts.'))
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return self.profile.get_absolute_url()

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def published_posts(self):
        return self.blog_posts.filter(
            pub_date__lt=date.today())

    def natural_key(self):
        return (self.email,)
