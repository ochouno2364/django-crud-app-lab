from django.db import models
from django.urls import reverse

BRANDS = (
    ('J', 'Jordan'),
    ('C', 'Converse'),
    ('P', 'Puma'),
    ('N', 'New Balance'),
)

# Create your models here.
class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    size = models.IntegerField()

    def get_absolute_url(self):
        return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})

class Release(models.Model):
    date = models.DateField('Release date')
    store = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(
        max_length=1,
        choices=BRANDS,
        default=BRANDS[0][0],
    )
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_brand_display()} on {self.date}"

    def get_absolute_url(self):
        return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})