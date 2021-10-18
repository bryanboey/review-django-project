import uuid
from django.db import models
from django.contrib.auth.models import User
from establishments.models import Establishment


class Review(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='written_reviews')
    establishment = models.ForeignKey(
        Establishment, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews'
    )
    title = models.CharField(max_length=150)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
