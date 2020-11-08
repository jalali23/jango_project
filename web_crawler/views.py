from django.http import HttpResponse
from .models import Courses,Articles
import json 


def importer(request):
    i = 0
    f = open("./data/zaban.json")
    a = json.load(f)
    f.close()
    for item in a:
        if i == 0:
            i = 1
            continue
        obj = Courses(
            teacher = item["teacher"],
            time = item["time"][0],
            price = item["price"][0],
            image = item["image"][0],
            title = item["title"][0],
            category = "مهارت های زبان",
            Url= item["url"],
        )
        obj.save()
    return HttpResponse("Done!")