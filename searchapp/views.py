from django.shortcuts import render
from web_crawler.models import Courses

def results(request):
    from django.core.paginator import Paginator
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        category = request.GET.get('category')
        page = request.GET.get('page')
        courses = Courses.objects.all()
        price = None
        
        if category:
            courses = Courses.objects.filter(Q(category__icontains=category)).distinct()
        elif query:
            courses = Courses.objects.filter(Q(title__icontains=query)).distinct() 
        else:
            courses = Courses.objects.all()

        if price:
            courses = courses.filter(price__range=(min_price, max_price))
        
        paginator = Paginator(courses, 10)
        courses = paginator.get_page(page)
        context = {
            "courses" : courses ,
            "category" : category,
            "price" : price
        }
    return render(request,'result.html',context)

def search(request):
    return render(request, 'search.html')
