from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
    
class Profile(models.Model):
    profile_photo = models.ImageField('profile/', null = True)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        Profile.objects.all().delete()        
  


class Image(models.Model):
    image = models.ImageField(upload_to ='image/', null=True)
    image_name = models.CharField(max_length =30, null=True)
    image_caption = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-pub_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    @classmethod
    def search_by_user(cls,search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images

    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.get(id=image_id)
        return images   



class Comment(models.Model):
    comment = models.CharField(null = True, max_length= 5000, verbose_name = 'name')
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null= True)

    class Meta:
        verbose_name = "comments"
        verbose_name_plural = "comments"

    class Meta:
        ordering = ['-date']        

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()