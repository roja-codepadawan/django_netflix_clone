from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    path('accounts/', include('allauth.urls')), # , views.account_signup, name='account_signup'
    #path('account/signup/', views.account_signup, name='account_signup'), #
    path("i18n/", include("django.conf.urls.i18n")),
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
