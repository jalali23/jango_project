from django.shortcuts import render
from web_crawler.models import Articles

def articles(request):
    from django.core.paginator import Paginator
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        page = request.GET.get('page')
        articles = Articles.objects.all()

        if query:
            queryset = Q(title__icontains=query)
            articles = Articles.objects.filter(queryset).distinct()
        
        paginator = Paginator(articles, 10)
        articles = paginator.get_page(page)

        context = {
            "articles" : articles ,
            "query":query,
        }
    return render(request,'articles.html',context)