from django.contrib import admin

# Register your models here.
from .models import Courses,Articles

admin.site.register(Articles)
class CourseAdmin(admin.ModelAdmin):
    fields = ('title', 'category')
    list_filter = ('category','option')
admin.site.register(Courses, CourseAdmin)