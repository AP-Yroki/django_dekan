from django.shortcuts import render
from .models import Items
from django.http import HttpResponseRedirect, HttpResponseNotFound


# получение данных
def index(request):
    items = Items.objects.all()
    return render(request, 'index.html', context={'items': items})


# Сохранение данных
def create(request):
    if request.method == 'POST':
        items = Items()
        items.name = request.POST.get('name')
        items.info = request.POST.get('info')
        items.price = request.POST.get('price')
        items.author = request.POST.get('author')
        items.save()
    return HttpResponseRedirect('/')




def delete(request, id):
    try:
        items = Items.objects.get(id=id)
        items.delete()
        return HttpResponseRedirect('/')
    except Items.DoesNotExist:
        return HttpResponseNotFound('<h2>Item not found</h2>')
