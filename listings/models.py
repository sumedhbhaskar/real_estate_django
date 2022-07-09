from django.db import models
from django.urls import reverse

class Listings(models.Model):
    title = models.CharField(max_length=150)
    
    price = models.CharField(max_length=10)
    num_beds = models.IntegerField()
    num_baths = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.TextField()
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("listing_detail", kwargs={"pk": self.pk})
    
