from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Movie, Profile #, Category 
# from uuid import UUID #  fail
from core.models import CustomUser
# from django.urls import reverse
# from django.http import HttpResponseRedirect
from django.db.models import Q

# from django.contrib.auth.forms import AuthenticationForm, UsernameField
# from django import forms

# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#     # @sensitive_post_parameters_m
#     # def dispatch(self, request, *args, **kwargs):
#     #     return super().dispatch(request, *args, **kwargs)

#     def get_initial(self):
#         initial = super().get_initial()
#         email = self.kwargs.get('email')
#         if email:
#             initial['login'] = email
#         return initial

    
#  def dispatch(self, request, *args, **kwargs):
#         email = request.session.get('email', None)
#         if email:
#             # ...
#          / user_exists:
#            #   return redirect(f'/accounts/login?email={email}')
#           else:
#               return redirect(f'/accounts/signup?email={email}')
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
    
# class Home(View):
#     def get(self,request,*args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(to='/profile/')
#         return render(request,'index.html',)

# class Login(View):
#     def get(self, request, email):
#         return render(request, 'login.html', {'email': email})
    
#     def post(self, request, email):
#         # Hier kannst du den Code für die Verarbeitung des Login-Formulars hinzufügen
#         # Zum Beispiel die Überprüfung von Anmeldeinformationen und Weiterleitungen
#         # basierend auf dem Ergebnis
#         return render(request, 'login.html', {'email': email})

# class Signup(View):
#     def get(self, request, email):
#         return render(request, 'signup.html', {'email': email})
    
#     def post(self, request, email):
#         # Hier kannst du den Code für die Verarbeitung des Signup-Formulars hinzufügen
#         # Zum Beispiel das Erstellen eines neuen Benutzers und Weiterleitungen
#         # basierend auf dem Ergebnis
#         return render(request, 'signup.html', {'email': email})

    
# def account_signup(request):
#     email = request.GET.get('email')  # Hier wird der Wert des 'email'-Parameters abgerufen

#     print("Received email:", email)
    
#     context = {'email': email}
#     return render(request, 'signup.html', context)
    
class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/profile/')
        return render(request, 'index.html')

        # Verwende URL-Parameter
    def post(self, request, *args, **kwargs):
        try:
            email = request.POST.get('email')
            user_exists = CustomUser.objects.filter(email=email).exists()

            if user_exists:
                return redirect(f'/accounts/login?email={email}')
            else:
                return redirect(f'/accounts/signup?email={email}')

        except Exception as e:
            print("Error:", str(e))
        return render(request, 'index.html')


@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    
    def get(self,request,*args, **kwargs):

        profiles=request.user.profiles.all()

        print(profiles)


        return render(request,'profileList.html',{
            'profiles':profiles
        })


@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()
        # Erstellen Sie ein neues Profilformular und setzen Sie die Standardwerte
        # form = ProfileForm(initial={
        #     'age': 'Studierende',
        #     'group_institut': 'Willkommen',
        # })

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)

       
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            # if not cleaned_data.get('age'):
            #     cleaned_data['age'] = 'Studierende'
            # if not cleaned_data.get('group_institut'):
            #     cleaned_data['group_institut'] = 'Willkommen'

            
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            print(profile)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch/{profile.uuid}') #uuid

        return render(request,'profileCreate.html',{
            'form':form
        })

@method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            # profile=Profile.objects.get(uuid=profile_id)
            profile=Profile.objects.get(uuid=profile_id)
            age = profile.age
            institut = profile.institut
            courses = profile.courses.values_list('id', flat=True)
            # courses = profile.group_courses
            print(profile)
            
            # movies=Movie.objects.filter(age_limit=profile.age_limit)
            # Filtern Sie Filme nach age_limit, categories und institutes
            movies = Movie.objects.filter(
                Q(age_limit=age) &  # Filme, die dem Alterslimit entsprechen
                Q(institut=institut) &  # Filme, die dem Institut entsprechen
                Q(courses__in=courses) # Filme, die der Kategorie entsprechen
                # Q(group_courses=courses) &  # Filme, die der Kategorie entsprechen
            ).distinct()
            
            print(movies)
            
            # Wenn keine Filme mit den Profilwerten gefunden werden
            # if not movies:
            #     # Holen Sie Filme mit den Standardwerten
            #     default_movies = Movie.objects.filter(
            #         Q(age_limit='Studierende') &
            #         Q(institut='Willkommen') &
            #         Q(courses='Willkommen')
            #     ).distinct()
            
            # Extrahiere die eindeutigen Kategorien aus der movies-Abfrage
            movies_by_category = movies.values_list('categories', flat=True).distinct()
            # Alle verfügbaren Kategorien aus der Movie-Tabelle abrufen
            # movies_by_category = Movie.objects.values_list('categories', flat=True).distinct()
            
        
            # Eine leere Liste für Filme pro Kategorie erstellen
            # movies_by_category = {}
        
            # # Filme nach Kategorien gruppieren
            # for category in categories:
            #     movies_category = Movie.objects.filter(categories=category)
            #     movies_by_category[category] = movies_category
            
            # print(movies_by_category)
            
            """ 
            # profile=Profile.objects.get(uuid=profile_id)
            profile=Profile.objects.get(uuid=profile_id)
            age_limit = profile.age_limit
            categories = profile.categories
            institutes = profile.group_institutes
            print(profile)
            
            # movies=Movie.objects.filter(age_limit=profile.age_limit)
            # Filtern Sie Filme nach age_limit, categories und institutes
            movies = Movie.objects.filter(
                Q(age_limit=age_limit) &  # Filme, die dem Alterslimit entsprechen
                Q(categories=categories) &  # Filme, die der Kategorie entsprechen
                Q(group_institutes=institutes)  # Filme, die dem Institut entsprechen
            ).distinct()
            """
            

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
           
            'show_case':showcase,
            
            # 'movies_by_category': movies_by_category
             'categories': movies_by_category
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')
        
"""
@method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
            'show_case':showcase
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')
"""


@method_decorator(login_required,name='dispatch')
class ShowMovieDetail(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            return render(request,'movieDetail.html',{
                'movie':movie
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

@method_decorator(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            """
            
            # 'movie'-Objekt mit der angegebenen UUID
            movie = Movie.objects.get(uuid=movie_id)
            
            # Extrahieren der URL der Videodatei
            file_url = movie.video_file.url

            # Entfernt '/media/' aus der URL
            cleaned_file_url = file_url.replace('/media', '')

            # Erstellen Sie die movie_data-Liste
            # Wählen Sie die Felder aus, die Sie serialisieren möchten
            movie_data = [{
                'id': str(movie.uuid),
                # 'title': movie.video_title,
                'title': movie.title,
                # 'file': file_url,
                'file': cleaned_file_url,
                # 'file': movie.video_file.url,
                # Fügen Sie weitere Felder hinzu, die Sie benötigen
            }]
            
             # Kontrolle: Ausgabe von movie_data
            print(movie_data)
            
            # Rendern Sie die HTML-Seite und übergeben Sie die movie_data
            return render(request, 'showMovie.html', {
                'movie': movie_data,
            })
            
            """
            # Original 
            
            movie=Movie.objects.get(uuid=movie_id)
            # Erstellen eines QuerySet  
            movie=movie.videos.values()
            # movie=movie.video_file.values()

            print(movie)
            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
            
        except Movie.DoesNotExist:
            return redirect('core:profile_list')
