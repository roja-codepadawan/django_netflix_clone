from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

"""
null=True: um sicherzustellen, dass das Feld nicht NULL (leer) sein kann
blank=True: um sicherzustellen, dass das Feld im Formular nicht leer gelassen werden kann
editable=False: wird verwendet, um anzugeben, ob ein Feld in einem Modell bearbeitbar (editierbar) sein soll oder nicht

blank=True erlaubt das Leerlassen des Feldes im Formular, und 
null=True erlaubt es, dass das Feld in der Datenbank NULL sein kann.
"""

# Altersgruppen oder Altersbeschränkungen
AGE_CHOICES=(
    ('Studierende', 'Studierende'),
    ('Mitarbeiter', 'Mitarbeiter')
)


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

class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True,editable=None)
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    
    age = models.CharField(verbose_name="Status", max_length=20, choices=AGE_CHOICES, blank=True, null=True, default='Studierende')
    institut=models.ManyToManyField('Institute', verbose_name="Institute")

    courses = models.ManyToManyField('Course', verbose_name="Kurse")


@receiver(post_save, sender=Profile)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created and not instance.name:
        instance.name = instance.user.username
        instance.save()


class CustomUser(AbstractUser):
    profiles = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)

    age = models.CharField(verbose_name="Status",max_length=20,choices=AGE_CHOICES,blank=True,null=True,default='Studierende')
    institut=models.ManyToManyField('Institute', verbose_name="Institute")

    courses = models.ManyToManyField('Course', verbose_name="Kurse")
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        profile = obj.profile  # Assuming 'profile' is the related name for the user in the Profile model
        profile.age = obj.age
        profile.institut.set(obj.institut.all())
        profile.courses.set(obj.courses.all())
        profile.save()
    
    def save(self, *args, **kwargs):
        # Speichern Sie zuerst den Benutzer
        super().save(*args, **kwargs)

        # Überprüfen Sie, ob das Profil bereits existiert
        if not self.profiles:
            # Erstellen Sie ein Profil für den Benutzer
            profile = Profile.objects.create(user=self)
            profile.save()
            self.profiles = profile
            self.save()  # Speichern Sie erneut, um das aktualisierte Profil zu setzen

        # Überprüfen Sie, ob der Benutzer Institute hat
        if not self.institut.exists():
            default_institute = Institute.objects.filter(title='Willkommen').first()
            if default_institute:
                self.institut.add(default_institute)
            
        # Überprüfen Sie, ob der Benutzer Kurse hat
        if not self.courses.exists():
            default_course = Course.objects.filter(title='Willkommen').first()
            if default_course:
                self.courses.add(default_course)

    def get_user_profile(self):
        return self.profiles

    def __str__(self):
        return f"{self.username}" #  - Name: {self.get_user_profile().name} - Alter: {self.age} - Institut: {self.institut} - Kursse: {self.courses}
     
@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, **kwargs):
    if instance.profiles:
        # Wenn das Profil existiert, aktualisieren Sie die entsprechenden Felder
        instance.profiles.name = instance.username
        instance.profiles.age = instance.age
        instance.profiles.institut.set(instance.institut.all()) # = instance.institut
        instance.profiles.courses.set(instance.courses.all())
        instance.profiles.save()

class Movie(models.Model):
    """
    Represents a movie in the application.

    Attributes:
        title (str): The title of the movie.
        description (str): The description of the movie.
        created (DateTimeField): The date and time when the movie was created.
        uuid (UUIDField): The unique identifier for the movie.
        videos (ManyToManyField): The videos associated with the movie.
        flyer (ImageField): The flyer image for the movie.
        type (str): The type of the movie (e.g., single film or series).
        age_limit (str): The age limit for the movie.
        institut (ManyToManyField): The institutes associated with the movie.
        courses (ManyToManyField): The courses associated with the movie.
        categories (str): The categories of the movie.

    Methods:
        __str__(): Returns a string representation of the movie.
    """

    title = models.CharField(max_length=225, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=None)
    videos = models.ManyToManyField('Video', help_text="Eine oder mehrere Videos hochladen - ")
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True, help_text="Vorschaubild für den Film -")
    type = models.CharField(max_length=10, choices=MOVIE_TYPE, help_text="Einzel Film oder Serie(Veranstaltungsreihe)")
    # age_limit = ArrayField(
    #     models.CharField(max_length=20, choices=AGE_CHOICES),
    #     verbose_name="Status",
    #     blank=True,
    #     null=True,
    # )
    age_limit = models.CharField(verbose_name="Status", max_length=20, choices=AGE_CHOICES, blank=True, null=True)
    institut = models.ManyToManyField('Institute', verbose_name="Institute")
    courses = models.ManyToManyField('Course', verbose_name="Kurse")
    categories = models.CharField(verbose_name="Kategorie", max_length=20, choices=MOVIE_CATEGORIES, blank=True, null=True)

    def __str__(self):
        institute_titles = [institute.title for institute in self.institut.all()]
        course_titles = [course.title for course in self.courses.all()]
        return f"{self.title} - Alterslimit: {self.age_limit} - Institute: {', '.join(institute_titles)} - Kurse: {', '.join(course_titles)}" 
    
    
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
        
        
class Institute(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Institute"
