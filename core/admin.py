from django.contrib import admin
from .models import CustomUser,Profile,Movie,Video,Course,Institute #,Category
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

###################
#  Search Filter  #
###################
#User Filter
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
   # list_display
   list_display = ("display_name", "display_age", "display_institut", "display_course")
   # list_filter
   list_filter = (UserAgeFilter, UserInstitutFilter, UserCoursFilter)
   # search_fields
   search_fields = ["username"]
   
   fieldsets = (
      ("Personal Information", {"fields": ("username", "age")}),
      ("Education", {
         "fields": ("institut", "courses"),
         "classes": ("collapse",),
      }),
   )
   
   def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # customize form layout here
        return form

   def display_name(self,obj):
      return obj.username
   
   display_name.short_description = "User"
   
   def display_age(self, obj):
      return obj.age

   display_age.short_description = "Status"
   
   def display_institut(self, obj):
      institute = obj.institut.all()
      if institute:
         return ', '.join([institute.title for institute in institute])
      else:
         return "Kein Institut ausgewählt"

   display_institut.short_description = "Institut"
   
   def display_course(self, obj):
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
   
   fieldsets = (
      ("Personal Information", {"fields": ("name", "age")}),
      ("Education", {
         "fields": ("institut", "courses"),
         "classes": ("collapse",),
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
      return obj.title
   
   display_title.short_description = "Title"
   
   def display_movie_age(self, obj):
      return obj.age_limit
   
   display_movie_age.short_description = "Status"
   
   def display_movie_institute(self, obj):
      institute = obj.institut.all()
      if institute:
         return ', '.join([institute.title for institute in institute])
      else:
         return "Kein Institut ausgewählt"
      
   display_movie_institute.short_description = "Institut"
   
   def display_movie_courses(self, obj):
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