from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# from core import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    path('accounts/', include('allauth.urls')), # , views.account_signup, name='account_signup'
    # path('account/signup/', views.account_signup, name='account_signup'), #
    path("i18n/", include("django.conf.urls.i18n")),
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# if not settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#         url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]
# else:
#     url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),