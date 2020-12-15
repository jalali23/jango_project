from django.urls import include, path
from . import views

urlpatterns = [
    path('articles',views.articles,name='results') ,
]
