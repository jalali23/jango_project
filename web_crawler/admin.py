from django.contrib import admin

# Register your models here.
from .models import Courses,Articles

admin.site.register(Courses)
admin.site.register(Articles)