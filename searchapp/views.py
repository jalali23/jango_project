from django.shortcuts import render
from web_crawler.models import *

def results(request):
    from django.core.paginator import Paginator
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        category = request.GET.get('category')
        page = request.GET.get('page')
        courses = Courses.objects.all()

        if query:
            queryset = Q(title__icontains=query)
            courses = Courses.objects.filter(queryset).distinct()

        elif category:
            categoryQuery = Q(category__icontains=category)
            courses = Courses.objects.filter(categoryQuery).distinct()
        paginator = Paginator(courses, 10)
        courses = paginator.get_page(page)
        context = {
            "courses" : courses ,
            "category" : category,
            "query" : query,
        }
    return render(request,'result.html',context)

def search(request):
    return render(request, 'search.html')
