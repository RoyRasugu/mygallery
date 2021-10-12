from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category)
    image_image = models.ImageField(upload_to = 'images/', default = None)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(title__icontains = search_term)
        return images