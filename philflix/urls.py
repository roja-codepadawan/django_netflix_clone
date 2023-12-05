from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls.static import static
from django.conf import settings
# from core import views
from django.views.static import serve
# from django.conf.urls import url

# Admin Site Config
admin.site.site_header = 'Phil II Flix site adminsitration'      # default: "Django Administration"
admin.site.index_title = 'Phil II Flix'     # default: "Site administration"
admin.site.site_title = 'admin'    # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls',namespace='core')),
    path('accounts/', include('allauth.urls')), # , views.account_signup, name='account_signup'
    # path('account/signup/', views.account_signup, name='account_signup'), #
    path("i18n/", include("django.conf.urls.i18n")),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
else:
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

# if not settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#         url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]
# else:
#     url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    