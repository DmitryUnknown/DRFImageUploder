from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from restapi import settings


class Image(models.Model):
    username_validator = UnicodeUsernameValidator()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image_name = models.CharField(
        _('image_name'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A image with that filename already exists."),
        },
    )
    date = models.DateTimeField(auto_now_add=True)
    image_path = models.FilePathField(path=settings.MEDIA_ROOT)
    image_field = models.ImageField(null=True, blank=True, verbose_name="image", upload_to='.')

