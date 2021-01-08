from django.shortcuts import render
from web_crawler.models import Articles
# Create your views here.
def articles(request):
    from django.db.models import Q
    if request.method == "GET":
        query = request.GET.get('q')
        articles = Articles.objects.all()
        if query:
            queryset = Q(title__icontains=query)
            articles = Articles.objects.filter(queryset).distinct()
        context = {
            "articles" : articles ,
        }
    return render(request,'articles.html',context)