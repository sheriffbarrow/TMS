from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models
import math
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
Image_Folder = "media/"

# Create your models here.
# Create your models here.


CS = Choices(
    ('Solved', _('Solved')),
    ('Not Solved', _('Not Solved')),
)


class Office(models.Model):
    office = models.CharField(max_length=255)

    def __str__(self):
        return self.office


class Room(models.Model):
    room_number = models.IntegerField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number)


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries', default=1)
    slug = models.SlugField()
    office = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    complaint = models.CharField(max_length=100)
    additional_Info = models.TextField(max_length=50, default='unkown')
    solution = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='entry_modifiers', default=1)
    signatory = models.CharField(max_length=255)
    signature = models.ImageField(upload_to='base64/url/')

    def __str__(self):
        return self.complaint

    def get_absolute_url(self):
        return reverse('graTMS:view-complaint', kwargs={'pk': self.id})


class Signature(models.Model):
    signature = models.ImageField(upload_to='base64/url/')
