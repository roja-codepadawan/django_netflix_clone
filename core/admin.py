from django.contrib import admin
from .models import CustomUser,Profile,Movie,Video,Course,Institute #,Category
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter

# Register your models here.
# admin.site.register(CustomUser)
# admin.site.register(Profile)
# admin.site.register(Movie)
# admin.site.register(Video)
# admin.site.register(Category)

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
   
   # def queryset(self, request, queryset):
   #      if self.value() == 'studierende':
   #          return queryset.filter(age='Studierende')
   #      if self.value() == 'mitarbeiter':
   #          return queryset.filter(age='Mitarbeiter')
   #      return queryset  # 'all' and default case

   # def queryset(self, request, queryset):
   #    if self.value() == 'all':
   #       return queryset
   #    # Wenn ein bestimmtes Alter ausgewählt wurde, filtern Sie das QuerySet entsprechend
   #    return queryset.filter(age=self.value())

   #  def lookups(self, request, model_admin):
   #      return (
   #          ('all', _('All')),
   #          ('studierende', _('Studierende')),
   #          ('mitarbeiter', _('Mitarbeiter')),
   #      )
   
   # def queryset(self, request, queryset):
   #    if self.value() == 'studierende':
   #       return queryset.filter(age='Studierende')
   #    if self.value() == 'mitarbeiter':
   #       return queryset.filter(age='Mitarbeiter')
   #    return queryset  # 'all' and default case
     
class UserInstitutFilter(SimpleListFilter):
   title = _('Institute')
   parameter_name = 'institut'

   def lookups(self, request, model_admin):
        # Alle eindeutigen Institute aus dem Modell 'CustomUser' abrufen
        institute = CustomUser.objects.values_list('institut', flat=True).distinct()
        # Eine Liste von Tupeln erstellen, wobei der erste Wert das Institut ist
        # und der zweite Wert der Anzeigetext im Filter ist
        institute_choices = [(inst, inst) for inst in institute]
        # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
        return (
            *institute_choices,
        )

   def queryset(self, request, queryset):
        selected_value = self.value()
        if selected_value:
            return queryset.filter(institut=selected_value)
        return queryset

   # def queryset(self, request, queryset):
   #      if self.value() == 'willkommen':
   #          return queryset.filter(group_institut='Willkommen')
   #      if self.value() == 'idp':
   #          return queryset.filter(group_institut='IDP')
   #      if self.value() == 'idm':
   #          return queryset.filter(group_institut='IDM')
   #      return queryset  # 'all' and default case
   
   # def queryset(self, request, queryset):
   #    if self.value() == 'all':
   #       return queryset
   #    # Wenn ein bestimmtes Institut ausgewählt wurde, filtern Sie das QuerySet entsprechend
   #    return queryset.filter(institut=self.value())

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
   
   # def queryset(self, request, queryset):
   #    if self.value() == 'willkommen':
   #       return queryset.filter(courses='Willkommen')
   #    if self.value() == '1':
   #       return queryset.filter(courses='1')
   #    if self.value() == '2':
   #       return queryset.filter(courses='2')
   #    return queryset  # 'all' and default case


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

   #  def lookups(self, request, model_admin):
   #      return (
   #          ('all', _('All')),
   #          ('studierende', _('Studierende')),
   #          ('mitarbeiter', _('Mitarbeiter')),
   #      )

   #  def queryset(self, request, queryset):
   #      if self.value() == 'studierende':
   #          return queryset.filter(age='Studierende')
   #      if self.value() == 'mitarbeiter':
   #          return queryset.filter(age='Mitarbeiter')
   #      return queryset  # 'all' and default case
     
class ProfileInstitutFilter(SimpleListFilter):
   title = _('Institut')
   parameter_name = 'group_institut'
    
   def lookups(self, request, model_admin):
      # Alle eindeutigen Institute aus dem Modell 'CustomUser' abrufen
      institute = Profile.objects.values_list('institut', flat=True).distinct()
      # Eine Liste von Tupeln erstellen, wobei der erste Wert das Institut ist
      # und der zweite Wert der Anzeigetext im Filter ist
      institute_choices = [(inst, inst) for inst in institute]
      # Die Liste der Auswahlmöglichkeiten mit "All" am Anfang zurückgeben
      return (
         *institute_choices,
      )

   def queryset(self, request, queryset):
      selected_value = self.value()
      if selected_value:
         return queryset.filter(institut=selected_value)
      return queryset

   #  def lookups(self, request, model_admin):
   #      return (
   #          ('all', _('All')),
   #          ('willkommen', _('Willkommen')),
   #          ('idp', _('IDP')),
   #          ('idm', _('IDM')),
   #      )

   #  def queryset(self, request, queryset):
   #      if self.value() == 'willkommen':
   #          return queryset.filter(group_institut='Willkommen')
   #      if self.value() == 'idp':
   #          return queryset.filter(group_institut='IDP')
   #      if self.value() == 'idm':
   #          return queryset.filter(group_institut='IDM')
   #      return queryset  # 'all' and default case

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
   
   #  def lookups(self, request, model_admin):
   #      return (
   #          ('all', _('All')),
   #          ('willkommen', _('Willkommen')),
   #          ('1', _('1')),
   #          ('2', _('2')),
   #      )

   #  def queryset(self, request, queryset):
   #      if self.value() == 'willkommen':
   #          return queryset.filter(group_courses='Willkommen')
   #      if self.value() == '1':
   #          return queryset.filter(group_courses='1')
   #      if self.value() == '2':
   #          return queryset.filter(group_courses='2')
   #      return queryset  # 'all' and default case

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


# Admin Register
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
   list_display = ("display_name", "display_age", "display_institut", "display_course")
   # list_filter = ("cours", "age", "institut")
   list_filter = (UserAgeFilter, UserInstitutFilter, UserCoursFilter)


   def display_name(self,obj):
      return obj.username
   
   display_name.short_description = "User"
   
   def display_age(self, obj):
      return obj.age

   display_age.short_description = "Status"
   
   def display_institut(self, obj):
      return obj.institut

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
   list_display = ("display_profil", "display_profile_age", "display_profile_institut", "display_profile_courses")
   list_filter = (ProfileAgeFilter, ProfileInstitutFilter, ProfileCoursFilter)
    
   def display_profil(self, obj):
      return obj.name
    
   display_profil.short_description = "Profil"
    
   def display_profile_age(self, obj):
      return obj.age
    
   display_profile_age.short_description = "Status"
    
   def display_profile_institut(self, obj):
      return obj.institut
    
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
   # def display_movie_courses(self, obj):
   #    return obj.group_courses
   
   # display_movie_courses.short_description = "Kurse"

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