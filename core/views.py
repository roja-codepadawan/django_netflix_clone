from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Movie, Profile, Category 
from uuid import UUID #  fail
from core.models import CustomUser
from django.urls import reverse
from django.http import HttpResponseRedirect



# class Home(View):
#     def get(self,request,*args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(to='/profile/')
#         return render(request,'index.html',)
    
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

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)

       
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
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
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            categories = Category.objects.all() # category=Category.objects.all()

            # context = {'categories': categories}

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
            'categories':categories,
            'show_case':showcase
            }) 	# , context)
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
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            movie=movie.videos.values()
            

            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')
