"""
This module contains the URL configuration for the Philflix Django project.

It includes the necessary imports for URL routing, serving static and media files,
and configuring the admin site. The urlpatterns list defines the URL patterns
for different views and includes the URLs from the core app and the allauth app.

The module also includes conditional statements to handle static and media file serving
in development mode.

Note: Some parts of the code are commented out and may not be active.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import include, url
# import debug_toolbar


# Admin Site Config
admin.site.site_header = 'Phil II Flix site administration'      # default: "Django Administration"
admin.site.index_title = 'Phil II Flix'     # default: "Site administration"
admin.site.site_title = 'admin'    # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('allauth.urls')), # , views.account_signup, name='account_signup'
    # path('account/signup/', views.account_signup, name='account_signup'), #
    path("i18n/", include("django.conf.urls.i18n")),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
#         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
#     ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
