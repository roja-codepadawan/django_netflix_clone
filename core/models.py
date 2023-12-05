from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

"""
null=True: um sicherzustellen, dass das Feld nicht NULL (leer) sein kann
blank=True: um sicherzustellen, dass das Feld im Formular nicht leer gelassen werden kann
editable=False: wird verwendet, um anzugeben, ob ein Feld in einem Modell bearbeitbar (editierbar) sein soll oder nicht
"""


# Altersgruppen oder Altersbeschränkungen
AGE_CHOICES=(
    ('Studierende', 'Studierende'),
    ('Mitarbeiter', 'Mitarbeiter')
)

# mögliche Institute oder Gruppen von Instituten
GROUP_INSTITUTES=(
    ('Willkommen', 'Willkommen'),
    ('IDP', 'IDP'), 
    ('IDM', 'IDM')
)

# # Kursgruppen oder Kursnummern
# GROUP_COURSE=(
#     ('Willkommen', 'Willkommen'),
#     ('1','1'),
#     ('2','2'),
# )

# Semestergruppen
# GROUP_SEMSTER=(
#     ('Winter','WI'),
#     ('Sommer','SO'),
# )

# Filmkategorien class Category(models.Model):
#     class Meta:
#         verbose_name = "Kategorie"
#         verbose_name_plural = "Kategories"
MOVIE_CATEGORIES=(
    ('Willkommen', 'Willkommen'),
    ('Dokumentarfilm', 'Dokumentarfilm'),
    ('Physik', 'Physik'),
    ('Mathematik', 'Mathematik'),
    ('Informatik', 'Informatik'),
    ('Kunstgeschichte', 'Kunstgeschichte'),
    ('Chemie', 'Chemie'),
    ('Biologie', 'Biologie'),
    ('Wirtschaft', 'Wirtschaft'),
    ('Literatur', 'Literatur'),
    ('Geschichte', 'Geschichte'),
)

# Filmtypen, wie 'single' für Einzelfilme und 'seasonal' für saisonale Filme.
MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal'),
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile',verbose_name="Profile")
    age = models.CharField(verbose_name="User Status",max_length=20, choices=AGE_CHOICES,blank=True,null=True,default='Studierende')
    institut=models.CharField(verbose_name="Institut",max_length=20,choices=GROUP_INSTITUTES,blank=True,null=True,default='Willkommen')
    courses=models.ManyToManyField('Course',verbose_name="Kurse",default='Willkommen')
    # course=models.CharField(max_length=20,choices=GROUP_COURSE,blank=True,null=True,default='Willkommen')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Update profile age_limit and group_courses
        profiles = self.profiles.all()
        for profile in profiles:
            profile.age = self.age
            profile.institut = self.institut
            profile.courses.set(self.courses.all())  # Verwende die set() Methode
            # profile.group_courses = self.course
            profile.save()
            
        """
        custom_user = CustomUser.objects.get(id=1)
        # Verwende die set() Methode, um die many-to-many Beziehung zu aktualisieren
        custom_user.group_courses.set(selected_courses)  # Richtig

        """
    

    def __str__(self):
        # Erstelle eine Liste der Kurs-Titel aus den zugeordneten Kursen
        course_titles = [course.title for course in self.courses.all()]
        
        return f"{self.username} - Alter: {self.age} - Institut: {self.institut} - Kurse: {', '.join(course_titles)}"

class Profile(models.Model):
    name = models.CharField(max_length=225)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True,editable=None)
    age = models.CharField(verbose_name="Profil Status",max_length=20,choices=AGE_CHOICES,blank=True,null=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Ändern Sie das related_name , related_name='user_profiles

    # def save(self, *args, **kwargs):
    #     # Stellen Sie sicher, dass das Alterslimit mit dem Alter des Benutzers übereinstimmt
    #     self.age_limit = self.user.age
    #     super().save(*args, **kwargs)
    
    institut=models.CharField(verbose_name="Institut",max_length=20,blank=True,choices=GROUP_INSTITUTES)
    courses=models.ManyToManyField('Course',blank=True,verbose_name="Kurse",default='Willkommen')
    # group_course=models.CharField(max_length=20,choices=GROUP_COURSE,blank=True,null=True)
    
    def __str__(self):
        # Erstelle eine Liste der Kurs-Titel aus den zugeordneten Kursen
        course_titles = [course.title for course in self.courses.all()]
        
        return f"{self.name} - Alter: {self.age} - Institut: {self.institut} - Kurse: {', '.join(course_titles)}"
    
    class Meta:
        verbose_name_plural = "Profile"
    

class Movie(models.Model):
    title:str = models.CharField(max_length=225,null=True)
    description:str=models.TextField(null=True)
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True,editable=None)
    
    # Das Feld für das Hochladen von mehreren Video-Dateien
    videos=models.ManyToManyField('Video')
    # Define fields for videos directly in the Movie model
    # video_file = models.FileField(upload_to='movies', blank=True, null=True)
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    
    type=models.CharField(max_length=10,choices=MOVIE_TYPE,help_text="Einzel Film oder Serie(Veranstaltungsreihe)")
    
    age_limit=models.CharField(verbose_name="Status",max_length=20,choices=AGE_CHOICES,blank=True,null=True)
    
    institut=models.CharField(verbose_name="Institut",max_length=20,choices=GROUP_INSTITUTES,blank=True,null=True)
    courses=models.ManyToManyField('Course', verbose_name="Kurse")
    # group_courses=models.CharField(max_length=20,choices=GROUP_COURSE,blank=True,null=True)
    
    categories=models.CharField(verbose_name="Kategorie",max_length=20,choices=MOVIE_CATEGORIES,blank=True,null=True)
    
    def __str__(self):
        # Erstelle eine Liste der Kurs-Titel aus den zugeordneten Kursen
        course_titles = [course.title for course in self.courses.all()]
        
        return f"{self.title} - Alterslimit: {self.age_limit} - Institut: {self.institut} - Kurse: {', '.join(course_titles)}"
    
class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    
    def __str__(self):
        return f"{self.title}"
    
    
class Course(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Kurse"
       
"""

<----- bevor change Movie, Profile ------>

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
    
    group_institutes=models.CharField(max_length=20,choices=GROUP_INSTITUTES,blank=True,null=True)
    group_courses=models.CharField(max_length=20,choices=GROUP_COURSE,blank=True,null=True)
    
    def __str__(self):
        return f"{self.name} - {self.age_limit}"# - {self.categories} - {self.group_institutes}"
        
<----- end bevor change Movie, Profile ------>        
        

<----- Movie only -------->
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

<-----End Movie only -------->


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