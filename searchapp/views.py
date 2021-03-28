from django.shortcuts import render

def results(request):
    from web_crawler.models import Courses
    from django.core.paginator import Paginator
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        category = request.GET.get('category')
        page = request.GET.get('page')
        price = request.GET.get('price')
        
        if category:
            title = category
            courses = Courses.objects.filter(Q(category__icontains=category)).distinct()
        elif query:
            title = query
            courses = Courses.objects.filter(Q(title__icontains=query)).distinct() 
        else:
            title = "دوره ها"
            courses = Courses.objects.all()

        if price:
            prices = price.split(',')
            if len(prices) > 1:
                min_price = prices[0]
                max_price = prices[1]
                courses = courses.filter(price__range=(min_price, max_price))
            else:
                courses = courses.filter(price__gt=prices[0])
                
        paginator = Paginator(courses, 10)
        courses = paginator.get_page(page)
        context = {
            "page" : page,
            "courses" : courses ,
            "category" : category,
            "price" : price ,
            "query" : query ,
            "title" : title ,
        }
    return render(request,'result.html',context)

def search(request):
    return render(request, 'search.html')