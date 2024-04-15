from django.contrib import admin
from .models import CustomUser,Profile,Movie,Video,Course,Institute #,Category
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

###################
#  Search Filter  #
###################
# User Filter
class UserAgeFilter(SimpleListFilter):
   title = _('Status')
   parameter_name = 'age'

   def lookups(self, request, model_admin):
        # Alle eindeutigen Alter aus dem Modell 'CustomUser' abrufen
        ages = CustomUser.objects.values_list('age', flat=True).distinct()
        # Eine Liste von Tupeln erstellen, wobei der erste Wert das Alter ist
        # und der zweite Wert der Anzeigetext im Filter ist
        age_choices = [(age, age) for age in ages]
        # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
        return (
            *age_choices,
        )
   
   def queryset(self, request, queryset):
        selected_value = self.value()
        if selected_value:
            return queryset.filter(age=selected_value)
        return queryset
   
     
class UserInstitutFilter(SimpleListFilter):
   title = _('Institute')
   parameter_name = 'institut'

   def lookups(self, request, model_admin):
      institute = Institute.objects.all()
      institute_choices = [(inst.id, inst.title) for inst in institute]
      return (
          *institute_choices,
      )

   def queryset(self, request, queryset):
        selected_value = self.value()
        if selected_value:
            return queryset.filter(institut=selected_value)
        return queryset

class UserCoursFilter(SimpleListFilter):
   title = _('Kurse')
   parameter_name = 'courses'

   def lookups(self, request, model_admin):
      # Alle Kurse aus der Datenbank abrufen
      courses = Course.objects.all()
      # Eine Liste von Tupeln erstellen, wobei der erste Wert der Kurswert ist
      # und der zweite Wert der Anzeigetext im Filter ist
      course_choices = [(course.id, course.title) for course in courses]
      # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
      return (
         *course_choices,
      )
   
   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(courses=selected_value)
      return queryset


# Profile Filter
class ProfileAgeFilter(SimpleListFilter):
   title = _('Status')
   parameter_name = 'age'
   
   def lookups(self, request, model_admin):
      # Alle eindeutigen Alter aus dem Modell 'CustomUser' abrufen
      ages = Profile.objects.values_list('age', flat=True).distinct()
      # Eine Liste von Tupeln erstellen, wobei der erste Wert das Alter ist
      # und der zweite Wert der Anzeigetext im Filter ist
      age_choices = [(age, age) for age in ages]
      # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
      return (
            *age_choices,
      )
   
   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(age=selected_value)
      return queryset

     
class ProfileInstitutFilter(SimpleListFilter):
   title = _('Institut')
   parameter_name = 'institut'

   def lookups(self, request, model_admin):
      institute = Institute.objects.all()
      institute_choices = [(inst.id, inst.title) for inst in institute]
      return (
          *institute_choices,
      )

   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(institut=selected_value)
      return queryset


class ProfileCoursFilter(SimpleListFilter):
   title = _('Kurse')
   parameter_name = 'group_courses'

   def lookups(self, request, model_admin):
      # Alle Kurse aus der Datenbank abrufen
      courses = Course.objects.all()
      # Eine Liste von Tupeln erstellen, wobei der erste Wert der Kurswert ist
      # und der zweite Wert der Anzeigetext im Filter ist
      course_choices = [(course.id, course.title) for course in courses]
      # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
      return (
         *course_choices,
      )
   
   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(courses=selected_value)
      return queryset


# Movie Filter
class MovieAgeFilter(SimpleListFilter):
   title = _('Status')
   parameter_name = 'age_limit'

   def lookups(self, request, model_admin):
      ages = Movie.objects.values_list('age_limit', flat=True).distinct()
      age_choices = [(age, age) for age in ages]
      return (
         *age_choices,
      )

   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(age_limit=selected_value)
      return queryset

class MovieInstitutFilter(SimpleListFilter):
   title = _('Institut')
   parameter_name = 'institut'

   def lookups(self, request, model_admin):
      institute = Institute.objects.all()
      institute_choices = [(inst.id, inst.title) for inst in institute]
      return (
          *institute_choices,
      )
   
   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(institut=selected_value)
      return queryset

class MovieCoursFilter(SimpleListFilter):
   title = _('Kurse')
   parameter_name = 'courses'

   def lookups(self, request, model_admin):
      courses = Course.objects.all()
      course_choices = [(course.id, course.title) for course in courses]
      return (
         *course_choices,
      )

   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(courses=selected_value)
      return queryset


####################
#  Admin Register  #
####################
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
   """
   Admin class for managing custom user model.

   Attributes:
      list_display (tuple): Tuple of fields to be displayed in the admin list view.
      list_filter (tuple): Tuple of fields to be used for filtering in the admin list view.
      search_fields (list): List of fields to be used for searching in the admin list view.
      fieldsets (tuple): Tuple of fieldsets to be displayed in the admin detail view.

   Methods:
      get_form(self, request, obj=None, **kwargs): Returns the form to be used for the admin view.
      display_name(self, obj): Returns the display name of the user.
      display_age(self, obj): Returns the display age of the user.
      display_institut(self, obj): Returns the display institute(s) of the user.
      display_course(self, obj): Returns the display course(s) of the user.
   """

   list_display = ("display_name", "display_age", "display_institut", "display_course")
   list_filter = (UserAgeFilter, UserInstitutFilter, UserCoursFilter)
   search_fields = ["username"]
   
   def get_fieldsets(self, request, obj=None):
      fieldsets = super().get_fieldsets(request, obj)
      if not request.user.is_superuser or not request.user.is_staff:
         return fieldsets[:-1]  # Exclude the last fieldset ("Permissions")
      return fieldsets

   # def get_readonly_fields(self, request, obj=None):
   #    readonly_fields = super().get_readonly_fields(request, obj)
   #    if not request.user.is_superuser or not request.user.groups.filter(name='Support-Admins').exists() or not request.user.groups.filter(name='admins').exists():
   #       return readonly_fields + ('is_superuser',)
   #    return readonly_fields

   # def has_delete_permission(self, request, obj=None):
   #    if request.user.is_superuser and (request.user.groups.filter(name='Support-Admins').exists() or request.user.groups.filter(name='admins').exists()):
   #       return True
   #    return super().has_delete_permission(request, obj)

   # def has_change_permission(self, request, obj=None):
   #    if request.user.is_superuser and request.user.groups.filter(name='Admins').exists():
   #       return True
   #    return super().has_change_permission(request, obj)
   
   # def get_fieldsets(self, request, obj=None):
   #    if not obj or not (request.user.is_superuser or request.user.is_staff):
   #       fieldsets = super().get_fieldsets(request, obj)
   # # def get_fieldsets(self, request, obj=None):
   # #    fieldsets = super().get_fieldsets(request, obj)
   # #    if not obj or not (request.is_superuser or request.is_staff):
   #    # if not obj or not (obj.is_superuser or obj.is_staff):
   #       return fieldsets[:-1]  # Exclude the last fieldset ("Permissions")
   #    return fieldsets
 
   def get_readonly_fields(self, request, obj=None):
      readonly_fields = super().get_readonly_fields(request, obj)
      if not request.user.is_superuser or not request.user.groups.filter(name='Support-Admins') or request.user.groups.filter(name='Admin').exists():
         return readonly_fields + ('is_superuser',)
      return readonly_fields
   
   """
   def has_delete_permission(self, request, obj=None):
      if request.user.is_superuser:
        return True
      return super().has_delete_permission(request, obj)
    
   def has_change_permission(self, request, obj=None):
      if request.user.is_superuser:
        return True
      return super().has_change_permission(request, obj)
   """
   
   def has_delete_permission(self, request, obj=None):
    if obj is not None and obj.is_superuser:
        return request.user.is_superuser and request.user.groups.filter(name='Support-Admins') or request.user.groups.filter(name='Admin').exists()
    return super().has_delete_permission(request, obj)
 
   def has_change_permission(self, request, obj=None):
    if obj is not None and obj.is_superuser:
        return request.user.is_superuser and request.user.groups.filter(name='Admin').exists()
    return super().has_change_permission(request, obj)

   fieldsets = (
      ("Personal Information", {
         "fields": (
            "username", "age", "email", "date_joined", "last_login",
            )
         }
       ),
      ("Education - Inhalt Zugriffssteuerung basierend auf Instituten und Kursen für den Benutzer (User)", {
         "fields": (
            "institut", "courses"
            ),
         "classes": (
            "expanded",
            ),
      }),
      ("Permissions", {
         "fields": (
            "is_active", "is_staff", "is_superuser", "groups"
         ),
         "classes": (
            "collapse",
         ),
      }),
   )
   

   def get_form(self, request, obj=None, **kwargs):
      """
      Returns the form to be used for the admin view.

      Args:
         request (HttpRequest): The current request.
         obj (object, optional): The object being edited, or None if it's a new object.
         **kwargs: Additional keyword arguments.

      Returns:
         form (Form): The form to be used for the admin view.
      """
      form = super().get_form(request, obj, **kwargs)
      # customize form layout here
      return form

   def display_name(self, obj):
      """
      Returns the display name of the user.

      Args:
         obj (object): The user object.

      Returns:
         str: The display name of the user.
      """
      return obj.username

   display_name.short_description = "User"

   def display_age(self, obj):
      """
      Returns the display age of the user.

      Args:
         obj (object): The user object.

      Returns:
         str: The display age of the user.
      """
      return obj.age

   display_age.short_description = "Status"

   def display_institut(self, obj):
      """
      Returns the display institute(s) of the user.

      Args:
         obj (object): The user object.

      Returns:
         str: The display institute(s) of the user.
      """
      institute = obj.institut.all()
      if institute:
         return ', '.join([institute.title for institute in institute])
      else:
         return "Kein Institut ausgewählt"

   display_institut.short_description = "Institut"

   def display_course(self, obj):
      """
      Returns the display course(s) of the user.

      Args:
         obj (object): The user object.

      Returns:
         str: The display course(s) of the user.
      """
      courses = obj.courses.all()
      if courses:
         return ', '.join([course.title for course in courses])
      else:
         return "Keine Kurse ausgewählt"

   display_course.short_description = "Kurse"
   


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   # list_display
   list_display = ("display_profil", "display_profile_age", "display_profile_institut", "display_profile_courses")
   # list_filter
   list_filter = (ProfileAgeFilter, ProfileInstitutFilter, ProfileCoursFilter)
   # search_fields
   search_fields = ["name"]
   
   def get_fieldsets(self, request, obj=None):
      fieldsets = super().get_fieldsets(request, obj)
      if obj is not None and request.user.is_superuser:
         # if not request.user.is_superuser:
         return fieldsets[:-1]  # Exclude the last fieldset ("Permissions") for non-superusers
      return fieldsets  # Superusers see all fieldsets
   # def get_fieldsets(self, request, obj=None):
   #  fieldsets = super().get_fieldsets(request, obj)
   #  if not obj or not (obj.user.is_superuser or obj.user.is_staff):
   #      return fieldsets[:-1]  # Exclude the last fieldset ("Permissions")
   #  return fieldsets
 
   def get_readonly_fields(self, request, obj=None):
    readonly_fields = super().get_readonly_fields(request, obj)
    if not request.user.is_superuser or not request.user.groups.filter(name='Support-Admins').exists() or not request.user.groups.filter(name='Admin').exists():
        return readonly_fields + ('user__is_superuser',)
    return readonly_fields
 

   def has_delete_permission(self, request, obj=None):
    if obj is not None and request.user.is_superuser:
        return request.user.is_superuser and (request.user.groups.filter(name='Support-Admins').exists() or request.user.groups.filter(name='Admin').exists())
    return super().has_delete_permission(request, obj)
 
   """
   def has_delete_permission(self, request, obj=None):
      if request.user.is_superuser:
        return True
      return super().has_delete_permission(request, obj)
    
   def has_change_permission(self, request, obj=None):
      if request.user.is_superuser:
        return True
      return super().has_change_permission(request, obj)
   """
 
   def has_change_permission(self, request, obj=None):
    if obj is not None and obj.user.is_superuser:
        return request.user.is_superuser and request.user.groups.filter(name='Admin').exists()
    return super().has_change_permission(request, obj)
   
   
   fieldsets = (
      ("Personal Information", {"fields": ("name", "age")}),
      # Institue & Kurse für die Autorisierung des Zugriffs aus die Inhalte
      ("Education - Inhalt Zugriffssteuerung basierend auf Instituten und Kursen den Benutzer (Profil)", {
         "fields": ("institut", "courses"),
         "classes": ("expanded",),
      }),
   )
    
   def display_profil(self, obj):
      return obj.name
    
   display_profil.short_description = "Profil"
    
   def display_profile_age(self, obj):
      return obj.age
    
   display_profile_age.short_description = "Status"
    
   def display_profile_institut(self, obj):
      institute = obj.institut.all()
      if institute:
         return ', '.join([institute.title for institute in institute])
      else:
         return "Kein Institut ausgewählt"
    
   display_profile_institut.short_description = "Institut"
    
   def display_profile_courses(self, obj):
      courses = obj.courses.all()
      if courses:
          return ', '.join([course.title for course in courses])
      else:
          return "Keine Kurse ausgewählt"
    
   display_profile_courses.short_description = "Kurse"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
   """
   Admin class for managing Movie model in the Django admin interface.
   """

   list_display = ("display_title", "display_movie_age", "display_movie_institute", "display_movie_courses")
   list_filter = (MovieAgeFilter ,MovieInstitutFilter, MovieCoursFilter)
   
   fieldsets = (
      ("Movie Information", {
         "fields": ("title", "description")
      }),
      ("Movie file", {"fields": ("videos", "flyer")
      }),
      ("Genre", {
         "fields": ("categories", "type"), 
         "classes": ("expanded",)
      }),
      ("Additional Information - Zugriffsschutz/Autorisierung welche Benutzer auf welche Inhalte zugreifen können.", {
         "fields": ("age_limit", "courses", "institut"),
         "classes": ("expanded",),
      }),
   )
   
   def display_title(self, obj):
      """
      Returns the title of the movie.
      
      Args:
         obj (Movie): The Movie object.
      
      Returns:
         str: The title of the movie.
      """
      return obj.title
   
   display_title.short_description = "Title"
   
   def display_movie_age(self, obj):
      """
      Returns the age limit status of the movie.
      
      Args:
         obj (Movie): The Movie object.
      
      Returns:
         str: The age limit status of the movie.
      """
      return obj.age_limit
   
   display_movie_age.short_description = "Status"
   
   def display_movie_institute(self, obj):
      """
      Returns the institutes associated with the movie.
      
      Args:
         obj (Movie): The Movie object.
      
      Returns:
         str: The institutes associated with the movie.
      """
      institute = obj.institut.all()
      if institute:
         return ', '.join([institute.title for institute in institute])
      else:
         return "Kein Institut ausgewählt"
     
   display_movie_institute.short_description = "Institut"
   
   def display_movie_courses(self, obj):
      """
      Returns the courses associated with the movie.
      
      Args:
         obj (Movie): The Movie object.
      
      Returns:
         str: The courses associated with the movie.
      """
      courses = obj.courses.all()
      if courses:
         return ', '.join([course.title for course in courses])
      else:
         return "Keine Kurse ausgewählt"
   
   display_movie_courses.short_description = "Kurse"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
   pass

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
   pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = ("display_courses",)
   def display_courses(self, obj):
      return obj.title
    
   display_courses.short_description = "Kurse"