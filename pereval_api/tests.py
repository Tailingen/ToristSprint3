from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *

class PerevalAddedTest(APITestCase):
    def setUp(self):
        self.user = Users.objects.create_user(name='testuser',
                                              last_name='testuser',
                                              patronymic='testuser',
                                              phone=123456789,
                                              email='test@mail.com')
        self.coords = Coords.objects.create(latitude=123, longitude=123, height=123)


    def PerevalCreateTest(self):
        pereval1 = Pereval_added.objects.create(users=self.user,
                                                coord_id=self.coords,
                                                beautyTitle='TestTitle',
                                                title='TestTitle',
                                                other_titles='TestTitle',
                                                connect=123,
                                                winter_level='hard',
                                                spring_level='hard',
                                                summer_level='easy',
                                                autumn_level='medium',
                                                status='new')
        return pereval1


    def ImageTestCreate(self):
        img1 = Pereval_images.objects.create(pereval_added=Pereval_added.objects.get(id=1),
                                             image_name='test_image',
                                             image='test.jpg')
        return img1
