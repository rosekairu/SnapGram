from django.test import TestCase
from .models import Profile, Image, comments

# Create your tests here.
class ProfileTestClass(TestCase):
    #Set Up method
    def setUp(self):
        self.profile = Profile(profile_photo='yes we can', bio='very awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    #Testing save method
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.image = Image(image='imageurl', image_name='fashion', image_caption='cool denim', profile='cool', likes='45', pub_date='12-03-2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,image))

    #Testing the save method
    def test_save_method(self):
        self.image.save_image()
        image = image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_method(self):
        self.image.save_delete()
        self.image.delete_image()
        image = image.objects.all()
        self.assertTrue(len(image)==0)  


class commentsTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.comments = comments(comments='i love it', date='12-12-2018', image='imageurl')

    def test_instance(self):
        self.assertTrue(isinstance(self.comments,comments))

    #Testing the save method
    def test_save_method(self):
        self.comments.save_comments()
        comments = comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_method(self):
        self.comments.delete_comments()
        comments = comments.objects.all()
        self.assertTrue(len(comments)==0)