from django.urls import include, path
from . import views

urlpatterns = [
    path('results',views.results,name='results') ,
    path('',views.search,name='search') ,
]
