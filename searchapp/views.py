from django.shortcuts import render
from web_crawler.models import * 

def results(request):
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        courses = Courses.objects.all()
        if query:
            queryset = Q(title__icontains=query)
            courses = Courses.objects.filter(queryset).distinct()
        context = {
            "courses" : courses ,
        }
    return render(request,'result.html',context)

def search(request):
    return render(request, 'search.html')
