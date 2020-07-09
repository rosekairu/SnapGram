from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile,Comment

# Create your tests here.

class ProfileTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user('Happy', 'secret')
        cls.profile1 = Profile(profile_photo='https://unsplash.it/1200/768.jpg?image=76',bio='forever Happy',user=cls.user)

 # Testing  instance
    def test_instance(cls):
        cls.assertTrue(isinstance(cls.profile1, Profile))

   # Testing Save Method
    def save_method_test(self):
        self.profile1.save_profile()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)



# Image testing

class ImageTestClass(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up data for the whole TestCase
        self.user = User.objects.create_user('Happy', 'secret')
        self.new_profile = Profile(profile_photo='https://unsplash.it/1200/768.jpg?image=76',bio='Live life', user=self.user)
        self.new_image = Image(image_name='myimage', caption='Travel', user=self.user)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        User.objects.all().delete()

    # Testing Delete Method
    def test_delete_image(self):
        '''
        Test case to delete uploaded images
        '''
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def update_caption(self):
        '''
        Test case to update a  new image caption
        '''
        self.new_caption.save_caption()
        caption_id = self.new_caption.id
        Image.update_caption(id,"book.jpg","book")
        self.assertEqual(self.caption.caption,"book.jpg","book")

# Comment
class CommentTestCase(TestCase):
    '''
    Test case for the Comment class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(comment='very nice')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        '''
        Test case to save comment
        '''
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 0)


    def test_delete_comment(self):
        ''''
        Test to delete a comment in an image
        '''
        
        comment = Comment.objects.all()
        self.assertTrue(len(comment) == 0)