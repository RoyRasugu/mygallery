from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.cat = Image(name = 'cat', description = 'This cat was made in china')

    # Testing instance
    def test_instace(self):
        self.assertTrue(isinstance(self.cat,Image))

    # Testing Save Method
    def test_save_method(self):
        self.cat.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        Image.delete_photo(self.photo.id)
        photos = Image.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_get_photo_by_id(self):
        photo = Image.get_photo_by_id(self.photo.id)
        self.assertEqual(photo, self.photo)

    def test_search_photo_by_category(self):
        photos = Image.search_photo_by_category("Test")
        self.assertFalse(len(photos) > 0)

    def test_filter_by_location(self):
        photos = Image.filter_by_location(self.photo.id)
        self.assertTrue(len(photos) > 0)

class LocationTestClass(TestCase):
    """
    Testing the Location class
    """
    def setUp(self):
        """
        Creating a new instance of the Location class
        """
        self.place = Location(city = "Nakuru", country = "Kenya")
        self.place.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_save_method(self):
        places = Location.objects.all()
        self.assertTrue(len(places) > 0)
        

class CategoryTestClass(TestCase):
    """
    Testing the Category class
    """
    def setUp(self):
        """
        Creating a new instance of the Category class
        """
        self.category = Category(name = "Test")
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)