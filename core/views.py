from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Movie, Profile, Video 
from core.models import CustomUser

from django.db.models import Q

import logging
from django.http import HttpResponse, Http404
import datetime

logger = logging.getLogger(__name__)

 
class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/profile/')
        return render(request, 'index.html')


@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    
    def get(self,request,*args, **kwargs):

        profiles = Profile.objects.filter(user=request.user)
        # profiles=request.user.profiles.all()

        print(profiles)

        return render(request,'profileList.html',{
            'profiles':profiles
        })


@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)

        if form.is_valid():
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
            age_profile = profile.age
            institute_profile = profile.institut
            # courses_profile = profile.courses.values_list('id', flat=True)
            courses_profile = list(profile.courses.values_list('id', flat=True))
            courses_profile.append(1)
            # courses = profile.group_courses
            print(profile)
            
            with open('output.txt', 'a') as f:
                now = datetime.datetime.now()  # Get the current date and time
                f.write(f"\n----{now}----\n")  # Write the date and time to the file
                
                # # Write the properties of the Movie object to the file
                # for key, value in movie_obj.__dict__.items():
                #     f.write(f'{key}: {value}\n')
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                # Write the URL of the video to the file
                f.write(f"status liste : {str(age_profile)}\n")
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                # Write the URL of the video to the file
                f.write(f"inst liste : {str(institute_profile)}\n")
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                # Write the URL of the video to the file
                f.write(f"cours liste : {str(courses_profile)}\n")
            
            # Filter movies based on age limit, categories and institutes
            # Filtern Sie Filme nach age_limit, categories und institutes
            movies = Movie.objects.filter(
                Q(age_limit=age_profile) &  # Filme, die dem Alterslimit entsprechen
                Q(institut=institute_profile) &  # Filme, die dem Institut entsprechen
                Q(courses__in=courses_profile) #| # Filme, die der Kategorie entsprechen
                # Q(institut='Willkommen') # | # Filme, die dem Institut "Willkommen" entsprechen
                # Q(courses='Willkommen')  # Filme, die dem Kurs "Willkommen" entsprechen
            ).distinct()
            
            # # Get movies with institut and course "Willkommen"
            # welcome_movies = Movie.objects.filter(
            #     Q(institut='Willkommen') |  # Filme, die dem Institut "Willkommen" entsprechen
            #     Q(courses__title='Willkommen')  # Filme, die dem Kurs "Willkommen" entsprechen
            # ).distinct()

            # # Combine the two QuerySets
            # # final_movies = movies.union(welcome_movies)
            # final_movies = movies | welcome_movies
            
            
            print(movies)
            
            # Extrahiere die eindeutigen Kategorien aus der movies-Abfrage
            movies_by_category = movies.values_list('categories', flat=True).distinct()
            # Alle verfügbaren Kategorien aus der Movie-Tabelle abrufen
            # movies_by_category = Movie.objects.values_list('categories', flat=True).distinct()

            try:
                showcase=movies[0]
            except :
                showcase=None

            if profile != request.user.profiles:
                return redirect(to='core:profile_list')

            # if profile not in request.user.profiles.all():
            #     return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
           
            'show_case':showcase,
            
            'categories': movies_by_category
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')
        

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
    """
    A class-based view that handles the rendering of a movie page.

    Methods:
    - get: Handles the GET request and renders the movie page.
    """

    def get(self,request,movie_id,*args, **kwargs):
        """
        Handles the GET request and renders the movie page.

        Parameters:
        - request: The HTTP request object.
        - movie_id: The ID of the movie to be displayed.

        Returns:
        - If the movie and video exist, renders the 'showMovie.html' template with the full video URL.
        - If the movie or video does not exist, renders the 'error.html' template with the corresponding error message.
        """
        try:
            # Holen des Movie-Objekts anhand der übergebenen movie_id
            movie_obj = get_object_or_404(Movie, uuid=movie_id)
            
            # Holen des ersten Videos, das mit dem Film verknüpft ist
            video = movie_obj.videos.first()
            
            # Überprüfen, ob ein Video vorhanden ist und ob das Video eine Datei hat
            if video and video.file:
                # Wenn ja, hole die URL des Videos
                video_url = video.file.url
            else:
                # Wenn nicht, wirf eine Http404 Ausnahme
                raise Http404("Video file not found")
            
            # Erstellen Sie die vollständige URL des Videos
            full_url = request.build_absolute_uri(video_url)
            
            # Debugging-Informationen in die Konsole schreiben   
            # Öffne die Ausgabedatei im Anhänge-Modus und schreibe die Debugging-Informationen hinein
            with open('output.txt', 'a') as f:
                now = datetime.datetime.now()  # Get the current date and time
                f.write(f"\n----{now}----\n")  # Write the date and time to the file
                
                # Write the properties of the Movie object to the file
                for key, value in movie_obj.__dict__.items():
                    f.write(f'{key}: {value}\n')
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                # Write the URL of the video to the file
                f.write(f"url: {str(video_url)}\n")
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                f.write(f"full_url: {str(full_url)}\n")
                f.write("\n----End of Block----\n")  # Mark the end of the block
            
            
            # Rendere die HTML-Vorlage und übergebe die URL des Videos
            return render(request, 'showMovie.html', {'full_video_url': full_url})
        
            logging.info(f"info log full URL: {full_url}")   
            logging.error(f"error log full URL: {full_url}") 
            # return render(request,'movieList.html',{
            #     'movies':movies,
           
            #     'show_case':showcase,
            
            #     'categories': movies_by_category
            # })
        
        except Exception as e:
            # Protokollieren Sie die Fehlermeldung
            logger.error('Fehler beim Rendern der Vorlage: %s', e)
            # Optional: Geben Sie eine Fehlerseite zurück
            return render(request, 'error.html', {'error': str(e)})
            # # Behandle alle anderen Ausnahmen, die auftreten können
            # return HttpResponse("Ein Fehler ist aufgetreten", status=500)
