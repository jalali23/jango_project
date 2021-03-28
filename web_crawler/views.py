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
             teacher = item["teacher"],
             time=item["time"],
             price = item["price"],
             image = item["image"],
            title = item["title"][0],
            category = "مدیریت و بازاریابی",
            Url= item["url"],
        )
        obj.save()
    return HttpResponse("Done!")
def shower(request):
    data=Courses.objects.all()
    for course in data:
        if "دروس مدرسه ای" in course.category:
            course.image = course.image[1:-1]
            course.save()
    return HttpResponse("done!")


#
# def deleter(request):
#     query=Articles.objects.all()
#     for i in query:
#         i.delete()
#     return HttpResponse(query)