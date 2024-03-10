from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    occupation = models.TextField(max_length=50,null=True)
    avatar = models.ImageField(null=True, default="blank.webp")
    birthday = models.DateField(null=True,blank=False)
    city = models.TextField(max_length=50,blank=True)
    country = models.TextField(max_length=50,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def uname(self):
        for i in self.email[::-1]:
            if i == '@':
                index = self.email.index(i)
                break

        return self.email[:index]

class blog(models.Model):
    caption = models.CharField(max_length=50,blank=False)
    body = models.TextField(blank=False)
    publish_date = models.DateField(blank=False,default=timezone.now())
    authorid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    thumbnail = models.ImageField(null=True, default="blank.webp")

    def bodypart(self):
        return self.body[:50]

class comments(models.Model):
    body = models.TextField(blank=False)
    publish_date = models.DateField(blank=False,default=timezone.now())
    authorid = models.ForeignKey(User,on_delete=models.SET_NULL,blank=False,null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    blog = models.ForeignKey(blog,on_delete=models.CASCADE,null=True)

class replies(models.Model):
    body = models.TextField(blank=False)
    publish_date = models.DateField(blank=False,default=timezone.now())
    authorid = models.ForeignKey(User,on_delete=models.SET_NULL,blank=False,null=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    comment = models.ForeignKey(comments,on_delete=models.CASCADE,null=True)

class follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE,null=True)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE,null=True)

    @classmethod
    def create(cls,user,follower):
        follower = cls(user=user,follower=follower)
        return follower
    class Meta:
        unique_together = ('user', 'follower')