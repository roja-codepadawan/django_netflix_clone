from django.contrib import admin
from .models import CustomUser,Profile,Movie#,Video#,Category

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
# admin.site.register(Video)
# admin.site.register(Category)
