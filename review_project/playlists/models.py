import uuid
from django.db import models
from django.contrib.auth.models import User
from establishments.models import Establishment


class Playlist(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    establishment = models.ManyToManyField(Establishment, blank=True, related_name='rel_to_list')
    created = models.DateTimeField(auto_now_add=True)
    # for future expansion
    # users_following = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
