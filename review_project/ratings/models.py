from django.db import models
from django.contrib.auth.models import User
from establishments.models import Establishment

RATING_VALUE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class StarRating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name="star_ratings")
    rating = models.IntegerField(default=0, null=True, blank=True, choices=RATING_VALUE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.establishment} - STARS: {self.rating}"

    class Meta:
        unique_together = ['user', 'establishment']
        ordering = ['-created']


class PriceRating(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name="price_ratings")
    rating = models.IntegerField(default=0, null=True, blank=True, choices=RATING_VALUE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.establishment} - PRICE: {self.rating}"

    class Meta:
        unique_together = ['user', 'establishment']
        ordering = ['-created']