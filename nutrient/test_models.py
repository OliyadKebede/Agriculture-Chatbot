from django.test import TestCase
from .models import  Crop

class CropTestCase(TestCase):
    def setUp(self):
        Crop.objects.create(name="Corn", sound="roar")
        Crop.objects.create(name="Flax", sound="meow")

    def test_Crop_can_create(self):
        """Animals that can speak are correctly identified"""
        corn = Crop.objects.get(name="Corn")
        flax = Crop.objects.get(name="Flax")

        self.assertEqual(str(corn), "Name: Corn")
        self.assertEqual(str(flax), "Name: Flax")

   