from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name):
    ls = ToDoList.objects.filter(name=name).first()
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1> %s </h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
    # return HttpResponse("<h1>%s</h1>" %ls.name)


