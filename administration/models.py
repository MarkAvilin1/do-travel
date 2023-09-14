from django.db import models
from PIL import Image


# Create your models here.
class OffersEN(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/offers')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
    
        if img.height > 768:
            output_size = (768, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title


class OfferAr(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/offers')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
    
        if img.height > 768:
            output_size = (768, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title
