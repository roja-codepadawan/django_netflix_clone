from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
#from uuid import UUID

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids'),
    ('Studi', 'Studi'),
    ('Prof', 'Prof')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal'),
)

MOVIE_CATEGORIES=(
    ('Physik', 'Physik'),
    ('Kunst', 'Kunst')
)


class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')

class Category(models.Model):
    category = models.CharField(max_length=10, choices=MOVIE_CATEGORIES)  # Define MOVIE_CATEGORIES

    def __str__(self):
        return self.category

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
   # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    #categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    categories=models.CharField(max_length=10,choices=MOVIE_CATEGORIES) # categories = models.ManyToManyField(Category) # categories=models.CharField(max_length=10,choices=MOVIE_CATEGORIES)
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
   # categories=models.CharField(max_length=10,choices=MOVIE_CATEGORIES)
    file=models.FileField(upload_to='movies')

# class Category(models.Model):
#    category=models.CharField(max_length=10,choices=MOVIE_CATEGORIES)
#
#    def __str__(self):
#        return self.category
