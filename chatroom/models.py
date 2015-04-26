from django.db import models
from swampdragon.models import SelfPublishModel
from .dragon_serializers import MessageSerializer


class Organization(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    organizations = models.ManyToManyField(Organization)


class Room(models.Model):
    name = models.CharField(max_length=75)
    organization = models.ManyToManyField(Organization)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Message(SelfPublishModel, models.Model):
    serializer_class = MessageSerializer
    user = models.ForeignKey('auth.User')
    text = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return '{}: {}'.format(self.user, self.text)
