from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

"""
null=True: um sicherzustellen, dass das Feld nicht NULL (leer) sein kann
blank=True: um sicherzustellen, dass das Feld im Formular nicht leer gelassen werden kann
editable=False: wird verwendet, um anzugeben, ob ein Feld in einem Modell bearbeitbar (editierbar) sein soll oder nicht
"""

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids'),
    ('Studi', 'Studi'),
    ('Prof', 'Prof')
)

GROUP_INSTITUTES=(
    ('IDP', 'IDP'), 
    ('IDM', 'IDM'))

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal'),
)

MOVIE_CATEGORIES=(
    ('Physik', 'Physik'),
    ('Kunst', 'Kunst')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')  # Ändern Sie das related_name , related_name='custom_users
    # age = models.CharField(max_length=10, choices=AGE_CHOICES, default='Studi')
    # group_institutes = models.CharField(max_length=5, choices=GROUP_INSTITUTES, blank=True)

    # def __str__(self):
    #     return f"{self.username} - {self.age} - {self.group_institutes}"

class Profile(models.Model):
    name = models.CharField(max_length=225)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES, null=True, default='Studi')
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Ändern Sie das related_name , related_name='user_profiles

    # def save(self, *args, **kwargs):
    #     # Stellen Sie sicher, dass das Alterslimit mit dem Alter des Benutzers übereinstimmt
    #     self.age_limit = self.user.age
    #     super().save(*args, **kwargs)
    
    categories  = models.CharField(max_length=10, choices=MOVIE_CATEGORIES,default='Physik')
    group_institutes = models.CharField(max_length=10, choices=GROUP_INSTITUTES,default='IDP')
    
    def __str__(self):
        return f"{self.name} - {self.age_limit}"# - {self.categories} - {self.group_institutes}"
    

class Movie(models.Model):
    title:str = models.CharField(max_length=225,null=True)
    description:str=models.TextField(null=True)
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    
    # Define fields for videos directly in the Movie model
    video_file = models.FileField(upload_to='movies', blank=True, null=True)
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES,blank=True,null=True)
    
    group_institutes=models.CharField(max_length=5,choices=GROUP_INSTITUTES,blank=True,null=True)
    categories=models.CharField(max_length=10,choices=MOVIE_CATEGORIES,blank=True,null=True)
    
    def __str__(self):
        return f"{self.title}"
    # Das Feld für das Hochladen von mehreren Video-Dateien
    # videos=models.ManyToManyField('Video')
    # class Video(models.Model):
    # title:str = models.CharField(max_length=225,blank=True,null=True)
    # file=models.FileField(upload_to='movies')
    
    
    
    # Spalte "video_id" für die Video-Beziehung
    # video_id = models.PositiveIntegerField(blank=True, null=True)
    # video_title = models.CharField(max_length=225, blank=True, null=True)
    
    # file=models.FileField(upload_to='movies',blank=True,default=None, null=True)
    
    #categories = models.ForeignKey(Category, on_delete=models.CASCADE)
"""

from django.db import models
import uuid

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    alter = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    alters_limit = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')

    def save(self, *args, **kwargs):
        # Stellen Sie sicher, dass das Alterslimit mit dem Alter des Benutzers übereinstimmt
        self.alters_limit = self.user.alter
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Profile of {self.user.name}"


class CustomUser(AbstractUser):
    # profiles=models.ManyToManyField('Profile')
    profiles=models.ManyToManyField('Profile')
    age=models.CharField(max_length=10,choices=AGE_CHOICES,default='Studi')
    group_institutes=models.CharField(max_length=5,choices=GROUP_INSTITUTES, blank=True)
    
    
    def __str__(self):
        #return self.profiles +" "+self.age_limit +" "+self.group_institutes
        # return f"{self.username} - {self.age} - {self.group_institutes}"
        return f"{self.username} - {self.group_institutes}"
    
    
    # Implement logic to update the age field to unique values for users_with_duplicate_age


# class Category(models.Model):
#     category = models.CharField(max_length=10, choices=MOVIE_CATEGORIES)  # Define MOVIE_CATEGORIES

#     def __str__(self):
#         return self.category

class Profile(models.Model):
    name=models.CharField(max_length=225)
    # age_limit=models.CharField(max_length=5,choices=AGE_CHOICES, null=True)
    # age_limit=models.ForeignKey(CustomUser.age_limit, on_delete=models.CASCADE)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES, null=True, default='Studi')
    #age_limit = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='age', db_column='age_limit', blank=True)
    # age_limit = models.CharField(max_length=5, choices=AGE_CHOICES,default='Studi', blank=True)  # Add the age_limit field to Profile
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')

  
    def save(self, *args, **kwargs):
        # Stellen Sie sicher, dass das Alterslimit mit dem Alter des Benutzers übereinstimmt
        self.age_limit = self.user.alter
        super().save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
        # Automatically set the age_limit of the profile based on the associated CustomUser
        # self.age_limit = self.user.age_limit
        # super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name +" "+self.age_limit
        # return f"{self.name} - {self.user.age_limit}"


from django.db import models
import uuid

class CustomUser(models.Model):
    age = models.PositiveIntegerField()

class Profile(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    custom_user_age = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field='age', db_column='custom_user_age')


"""

"""
Original 

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)


    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')

"""


# class Video(models.Model):
#     title:str = models.CharField(max_length=225,blank=True,null=True)
#    # categories=models.CharField(max_length=10,choices=MOVIE_CATEGORIES)
#     file=models.FileField(upload_to='movies')

# class Category(models.Model):
#    category=models.CharField(max_length=10,choices=MOVIE_CATEGORIES)
#
#    def __str__(self):
#        return self.category


# @receiver(pre_save, sender=CustomUser)
# def sync_age_limit(sender, instance, **kwargs):
#     try:
#         profile = instance.profiles.first()
#         if profile:
#             profile.age_limit = instance.age_limit
#             profile.save()
#     except Profile.DoesNotExist:
#         # Handle the case where a user doesn't have a profile
#         pass

# # Register the signal
# pre_save.connect(sync_age_limit, sender=CustomUser)
