from django.shortcuts import render
from web_crawler.models import * 

def results(request):
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        courses = []
        if query:
            queryset = Q(title__icontains=query)
            courseQuery = Courses.objects.filter(queryset).distinct()
            for i in courseQuery:
                courses.append({
                    "title" : i.title,
                    "teacher" : i.teacher ,                    
                    "price" : i.price ,
                    "category" : i.category ,
                    "time" : i.time ,
                    "image" : i.image ,
                    "Url" : i.Url ,
                })
        context = {
            "courses" : courses ,
        }
    return render(request,'result.html',context)

def search(request):
    return render(request, 'search.html')
