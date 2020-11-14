from django.http import HttpResponse
from .models import Courses,Articles
import json

def importer(request):
    i = 0
    f = open("./data/articles5.json")
    a = json.load(f)
    f.close()
    for item in a:
        if i == 0:
            i = 1
            continue
        obj = Articles(
            # teacher = item["teacher"],
            # time=item["time"],
            # price = item["price"],
            # image = item["image"],
            title = item["title"][0],
            #category = "دوره های آنلاین",
            Url= item["url"],
        )
        obj.save()
    return HttpResponse("Done!")
def shower(request):
    data_list=[]
    data_str=''
    data_list=set(data_list)
    data=Courses.objects.all()
    for i in data:
        if i.category not in data_list:
            data_list.add(i.category+'----\n')
    for i in data_list:
        data_str += str(i)+ "\n\t"
    print(data_str)
    return HttpResponse(data_list)
#
# def deleter(request):
#     query=Articles.objects.all()
#     for i in query:
#         i.delete()
#     return HttpResponse(query)