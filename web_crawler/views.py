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
    counter = 0
    for course in data:
        # print(type(course.price))
        if course.price== "None" or course.price == None or "رایگان" in course.price:
            counter += 1
            # course.price = 0
            # course.save()
            # print(course.price)
    return HttpResponse(counter)



# def adder(request):
#     query=Courses.objects.all()
#     for i in query:
#         if "academyit" in i.Url:
#             i.option = "deliberation"
#             i.save()
#             # print(i.title)
#     return HttpResponse("done!")