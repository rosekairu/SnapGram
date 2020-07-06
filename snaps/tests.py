from django.test import TestCase
from mimesis import Generic

from .models import User, Image, Profile, Comment, ImageLike, Followers

class UserModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.new_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_user, User))

    def tearDown(self):
        User.objects.all().delete()

class ProfileModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.default_profile = Profile()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.default_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()

class ImageModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.new_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

        self.user_image = Image(
            image = self.gen.person.avatar(),
            image_name = self.gen.person.title(),
            caption = self.gen.text.sentence(),
            user = self.new_user
        )

    def test_isinstance(self):
        self.assertTrue(isinstance(self.user_image, Image))

    def tearDown(self):
        Image.objects.all().delete()

class CommentModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.new_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

        self.user_image = Image(
            image = self.gen.person.avatar(),
            image_name = self.gen.person.title(),
            caption = self.gen.text.sentence(),
            user = self.new_user
        )

        self.new_comment = Comment(
            comment = self.gen.text.text(),
            user = self.new_user,
            image = self.user_image
        )
    
    def test_isinstance(self):
        self.assertTrue(self.new_comment, Comment)

    def tearDown(self):
        Comment.objects.all().delete()

class ImageLikeModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.new_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

        self.user_image = Image(
            image = self.gen.person.avatar(),
            image_name = self.gen.person.title(),
            caption = self.gen.text.sentence(),
            user = self.new_user
        )

        self.im_like = ImageLike(user = self.new_user, image = self.user_image)

    def test_isinstance(self):
        self.assertTrue(self.im_like, ImageLike)

    def tearDown(self):
        ImageLike.objects.all().delete()

class FollowersMModelTest(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.account_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

        self.follower_user = User(
            username = self.gen.person.username(),
            email = self.gen.person.email(),
            password = self.gen.person.password()
        )

        self.follower = Followers(user = self.account_user, follower = self.follower_user)

    def test_isinstance(self):
        self.assertTrue(self.follower, Followers)

    def tearDown(self):
        Followers.objects.all().delete()