from django.urls import include, path
from . import views

urlpatterns = [
    path('result',views.result,name='result') ,
]
