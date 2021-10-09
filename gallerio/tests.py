from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.cat = Image(name = 'cat', description = 'This cat was made in china')

    # Testing instance
    def test_instace(self):
        self.assertTrue(isinstance(self.cat,Image))

    # # Testing Save Method
    # def test_save_method(self):
    #     self.cat.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images) > 0)
