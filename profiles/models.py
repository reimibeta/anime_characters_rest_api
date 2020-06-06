from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Help Django work with our custom user model. """

    def create_user(self, email, name, password=None, raw_password=None):
        """ Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, raw_password=raw_password)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, raw_password):
        """ Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password, raw_password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Respents a " user profile " inside our system. """
    NORMAL_AUTH = 1
    FACEBOOK_AUTH = 2
    GMAIL_AUTH = 3
    AUTH_CHOICES = (
        (NORMAL_AUTH,'normal'),
        (FACEBOOK_AUTH,'facebook'),
        (GMAIL_AUTH,'gmail')
    )
    social_auth = models.PositiveSmallIntegerField(choices=AUTH_CHOICES, null=True, blank=True)

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    raw_password = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get a users short name. """
        return self.name

    def get_short_name(self):
        """ Used to get a users short name. """
        return self.name

    def __str__(self):
        """ Django uses this when it needs to convert the object to a string """

        return self.email