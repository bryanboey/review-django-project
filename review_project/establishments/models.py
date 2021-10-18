import uuid
from django.db import models


class Establishment(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200, null=False)
    created = models.DateTimeField(auto_now_add=True)
    # consider adding tag field

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'address']
        # ordering = ['-created']

