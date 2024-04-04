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
        
        
        """try:
            # Your code here
        except Exception as e:
        context = {'error': str(e)}
            return render(request, 'error.html', context)"""
    
    
"""
@method_decorator(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            # Your code here
            # Define movie_video here before using it
            # movie = Movie.objects.get(uuid=movie_id)  # Ersetzen Sie ... durch die ID des Films, den Sie anzeigen möchten
            movie_obj = get_object_or_404(Movie, uuid=movie_id)
            # video = movie_obj.videos.first()  # Get the first video related to the movie
            # Get the videos associated with the movie
            video = movie_obj.videos.first()  # Get the first video related to the movie
            if video and video.file:
                video_url = video.file.url
            else:
                raise Http404("Video file not found")
            # Get the URL of the file for each video
            # video_urls = [video.file.url for video in videos]
            # file_url = movie_obj.video_file.url   # Get the URL of the video file
     
            # movie_video = movie.videos.values()
            # logging.info(f'movie_video: {movie_obj}')
            # logging.info(f'movie: {movie}')
            with open('output.txt', 'a') as f:
                now = datetime.datetime.now()  # Get the current date and time
                f.write(f"\n----{now}----\n")  # Write the date and time to the file
                # f.write(str(movie))  # Write movie to the file
                # f.write(f"\n--------") # Add a newline to separate the blocks
                # f.write("\n")  # Add a newline to separate the blocks
                for key, value in movie_obj.__dict__.items():
                    f.write(f'{key}: {value},\n')
                # f.write(str(movie_video.__dict__))  # Write movie_video to the file
                # f.write(str(list(movie_video)))  # Write movie_video to the file
                # f.write(f"\n--------") # Add a newline to separate the blocks
                # f.write(str(video))  # Write movie to the file
                # f.write("\n")  # Add a newline to separate the blocks
                f.write(f"\n--------\n") # Add a newline to separate the blocks
                f.write(str(video_url))  # Write movie to the file
                f.write("\n")  # Add a newline to separate the blocks
                f.write("\n----End of Block----\n")  # Indicate the end of a block
                
            # if movie_obj is None:
            #     logger.exception("Movie with id %s does not exist", movie_obj)
            #     logging.info(f'Movie with id %s does not exist: {movie_obj}')
            #     return HttpResponse("Film nicht gefunden", status=404)
               
            # logger.error("Something went wrong", exc_info=True)
            # logging.info(f'movie_video: {movie_video}')
            return render(request, 'showMovie.html', {'video_url': video_url,})
            # return render(request,'showMovie.html',{
            #     'movie': movie_obj
            # })
            
            # movie = Movie.objects.get(uuid=movie_id)


            # return render(request, 'showMovie.html', {
            # 'movie': list(movie)
            # })
        # except Movie.DoesNotExist:
        #     logger.exception("Movie with id %s does not exist", movie)
        #     raise Http404("Movie does not exist")
        #     # return redirect('core:profile_list')
        except ValueError:
            logger.error("Invalid value", exc_info=True)
            return HttpResponse("Invalid value", status=400)
        except Exception:
            logger.error("Something went wrong", exc_info=True)
            # logging.info(f'movie_video: {movie_video}')
            return HttpResponse("Something went wrong", status=500)
        # # return render(request, 'showMovie.html', {'movie': movie_video})
        # return render(request, 'showMovie.html', {'video_url': video_url})
"""        
        
        # try:
                
        #     movie=Movie.objects.get(uuid=movie_id)

        #     movie_video=movie.video.values()
            
        #     with open('output.txt', 'a') as f:
        #         f.write(str(movie))  # Write movie to the file
        #         f.write(str(list(movie_video)))  # Write movie_video to the file

        #     return render(request,'showMovie.html',{
        #         'movie':list(movie)
        #     })
        # except Movie.DoesNotExist:
        #     return redirect('core:profile_list')


# try:
#         # Your code here
#     except ValueError:
#         return HttpResponse("Invalid value", status=400)
#     except Exception:
#         return HttpResponse("Something went wrong", status=500)


# @method_decorator(login_required,name='dispatch')
# class ShowMovie(View):

    
#     def get(self,request,movie_id,*args, **kwargs):
#         try:
#             movie = get_object_or_404(Movie, uuid=movie_uid)
#             with open('debug_output.txt', 'a') as f:
#                 print(f"URL: {request.path}", file=f)
#                 print(f"Movie: {movie}", file=f)
#             return render(request, 'showMovie.html', {'movie': movie})
#         #     movie = Movie.objects.get(uuid=movie_id)
#         #     video = movie.videos.first()  # Get the first video related to the movie
#         # # if video and video.file:
#         # #     video_url = video.file.url
#         #     # kannst du hier video_url mal dumpen und schauen was drin steht?
#         #     # with open('output.txt', 'a') as f:
#         #     #     print(video_url, file=f)
#         #     response = render(request, 'showMovie.html', {'video_url': video_url})
            
#         #     with open('output.txt', 'a') as f:
#         #         print(str(response.content), file=f)
#         #     return response
#         # else:
#         #     raise Http404("Video file not found")
#         except Movie.DoesNotExist:
#             return redirect('core:profile_list')
#         return render(request, 'showMovie.html', {'video_url': video_url})
    
    # def get(self,request,movie_id,*args, **kwargs):
    #     movie = Movie.objects.get(uuid=movie_id)
    #     video = movie.videos.first()  # Get the first video related to the movie
    #     if video and video.file:
    #         video_url = video.file.url
    #     else:
    #         raise Http404("Video file not found")
    #     return render(request, 'showMovie.html', {'video_url': video_url})
        
        # movie = get_object_or_404(Movie, uuid=movie_id)
        # video = movie.videos.first()  # Get the first video related to the movie
        # if video and video.file:
        #     return FileResponse(video.file)
        # else:
        #     raise Http404("No video file found")
        # try:
        #     movie = Movie.objects.get(uuid=movie_id)
        #     videos = movie.videos.all()
        #     if videos:
        #         video = videos[0]  # Get the first video related to the movie
        #         video_data = {
        #             'id': str(video.uuid),
        #             'file': video.file.url if video.file else '',
        #         }
        #         return render(request, 'showMovie.html', {
        #             'video': video_data,
        #         })
        #     else:
        #         raise Http404("No videos related to this movie")
        # except Movie.DoesNotExist:
        #     return redirect('core:profile_list')
        # try:
        #     movie = Movie.objects.get(uuid=movie_id)
        #     movie_data = {
        #         'id': str(movie.uuid),
        #         'title': movie.title,
        #         # 'files': [video.file.url for video in movie.videos.all()],
        #         'files': [video.file.url for video in movie.videos.all() if video.file],
        #     }
        #     print(movie_data)
        #     return render(request, 'showMovie.html', {
        #         'movie': movie_data,
        #     })
        # except Movie.DoesNotExist:
        #     return redirect('core:profile_list')
    
    # def get(self,request,movie_id,*args, **kwargs):
    #     try:
    #         movie = Movie.objects.get(uuid=movie_id)
    #         file_url = movie.video_file.url
    #         cleaned_file_url = file_url.replace('/media', '')
    #         movie_data = [{
    #             'id': str(movie.uuid),
    #             'title': movie.title,
    #             'file': file_url,
    #         }]
    #         print(movie_data)
    #         return render(request, 'showMovie.html', {
    #             'movie': movie_data,
    #         })
    #     except Movie.DoesNotExist:
    #         return redirect('core:profile_list')
    # def get(self,request,movie_id,*args, **kwargs):
    #     try:
    #         # 'movie'-Objekt mit der angegebenen UUID
    #         movie = Movie.objects.get(uuid=movie_id)
            
    #         # Extrahieren der URL der Videodatei
    #         file_url = movie.video_file.url

    #         # Entfernt '/media/' aus der URL
    #         cleaned_file_url = file_url.replace('/media', '')

    #         # Erstellen Sie die movie_data-Liste
    #         # Wählen Sie die Felder aus, die Sie serialisieren möchten
    #         movie_data = [{
    #             'id': str(movie.uuid),
    #             'title': movie.title,
    #             'file': file_url,
    #             # 'file': cleaned_file_url,
    #             # Fügen Sie weitere Felder hinzu, die Sie benötigen
    #         }]
            
    #         # Kontrolle: Ausgabe von movie_data
    #         print(movie_data)
            
    #         # Rendern Sie die HTML-Seite und übergeben Sie die movie_data
    #         return render(request, 'showMovie.html', {
    #             'movie': movie_data,
    #         })
            
    #     except Movie.DoesNotExist:
    #         return redirect('core:profile_list')
        
        
        

# from django.core.exceptions import ObjectDoesNotExist
# from django.http import Http404

# @method_decorator(login_required,name='dispatch')
# class ShowMovie(View):
#     def get(self,request,movie_id,*args, **kwargs):
#         try:
#             movie = Movie.objects.get(uuid=movie_id)
#             # Rest of your code...

#         except ObjectDoesNotExist:
#             # Handle the case where the movie does not exist
#             return redirect('core:profile_list')

#         except ValueError:
#             # Handle the case where the UUID is not valid
#             raise Http404("Invalid UUID")

#         except Exception as e:
#             # Handle any other exceptions
#             print(e)
#             return HttpResponseServerError("An error occurred")
        
# class ShowMovie(View):
#     def get(self,request,movie_id,*args, **kwargs):
#         try:
#             """
            
#             # 'movie'-Objekt mit der angegebenen UUID
#             movie = Movie.objects.get(uuid=movie_id)
            
#             # Extrahieren der URL der Videodatei
#             file_url = movie.video_file.url

#             # Entfernt '/media/' aus der URL
#             cleaned_file_url = file_url.replace('/media', '')

#             # Erstellen Sie die movie_data-Liste
#             # Wählen Sie die Felder aus, die Sie serialisieren möchten
#             movie_data = [{
#                 'id': str(movie.uuid),
#                 # 'title': movie.video_title,
#                 'title': movie.title,
#                 # 'file': file_url,
#                 'file': cleaned_file_url,
#                 # 'file': movie.video_file.url,
#                 # Fügen Sie weitere Felder hinzu, die Sie benötigen
#             }]
            
#              # Kontrolle: Ausgabe von movie_data
#             print(movie_data)
            
#             # Rendern Sie die HTML-Seite und übergeben Sie die movie_data
#             return render(request, 'showMovie.html', {
#                 'movie': movie_data,
#             })
            
#             """
#             # Original 
            
#             movie=Movie.objects.get(uuid=movie_id)
#             # Erstellen eines QuerySet  
#             movie=movie.videos.values()
#             # movie=movie.video_file.values()

#             print(movie)
#             return render(request,'showMovie.html',{
#                 'movie':list(movie)
#             })
            
#         except Movie.DoesNotExist:
#             return redirect('core:profile_list')


"""    
# def movie_list(request):
#     movies = Movie.objects.all()  # Get all movies
#     return render(request, 'movie_list.html', {'movies': movies})  

# {% for movie in movies %}
#     <div>
#         <h2>{{ movie.title }}</h2>
#         <p>{{ movie.description }}</p>
#         <!-- Display other fields of the movie as needed -->
#     </div>
# {% empty %}
#     <p>No movies available.</p>
# {% endfor %}   
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