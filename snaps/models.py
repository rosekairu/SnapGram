from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class ModelMethods:
    """
    Define CRUD operation methods for db models
    """
    def save_model(self):
        """
        Save relational model data to database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.save()

    def delete_model(self):
        """
        Delete relational model data from database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.delete()

    def update_model(self, **kwargs):
        """
        Update relational model data in database

        Args:
            kwargs: model attributes to be updated
        Returns:
            None (NoneType)
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.save()


class Profile(models.Model, ModelMethods):
    profile_photo = CloudinaryField('profile_photo', default = "image/upload/v1583754861/person_placeholder_l8auvx.jpg")
    bio = models.TextField(default = '')
    user = models.OneToOneField(User, on_delete = models.CASCADE, default=None)

    @staticmethod
    def search_by_username(search_username):
        searched_users = User.objects.filter(username__icontains = search_username).all()
        return searched_users
    
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=32)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    likes = models.IntegerField(default=0)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    @classmethod
    def get_user_images(cls, search_user):
        all_images = cls.objects.filter(user = search_user).all()
        return all_images

class Comment(models.Model, ModelMethods):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE, default=None)

class Followers(models.Model, ModelMethods):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="users")
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name="followers")

class ImageLike(models.Model, ModelMethods):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
