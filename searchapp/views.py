from django.shortcuts import render

def results(request):
    return render(request,'result.html')

def search(request):
    return render(request, 'search.html')
