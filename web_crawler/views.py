from django.http import HttpResponse
from .models import Courses,Articles
import json 


def importer(request):
    i = 0
    f = open("./data/modirsabz_courses.json")
    a = json.load(f)
    f.close()
    for item in a:
        if i == 0:
            i = 1
            continue
        obj = Courses(
           # teacher = item["teacher"],
           # time=item["time"][0],
            price = item["price"][0],
            image = item["image"][0],
            title = item["title"][0],
            category = "مدیریت و بازاریابی",
            Url= item["url"],
        )
        obj.save()
    return HttpResponse("Done!")
# def shower(request):
#     data_list=[]
#     data_str=''
#     data_list=set(data_list)
#     data=Courses.objects.all()
#     for i in data:
#         if i.category not in data_list:
#             data_list.add(i.category+'--------\n')
#     for i in data_list:
#         data_str += str(i)+ "\n\t"
#     print(data_str)
#     return HttpResponse(data_list)
# def deleter(request):
#     query=Courses.objects.filter(category='دوره های رایگان')
#     for i in query:
#         i.delete()
#     return HttpResponse(query)