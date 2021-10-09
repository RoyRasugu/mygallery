from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    # image_image = models.ImageField(upload_to = 'images/', default = None)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
        
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

