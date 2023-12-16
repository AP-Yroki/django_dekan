from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Items
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import Items as ItemsForm

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

def add(request):
    items = Items.objects.all()
    return render(request, 'add.html', context={'items': items})


# Изменение
def edit(request, id):
    try:
        items = Items.objects.get(id=id)

        if request.method == 'POST':
            items.name = request.POST.get('name')
            items.info = request.POST.get('info')
            items.price = request.POST.get('price')
            items.author = request.POST.get('author')
            items.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit_template.html', {'items': items})
    except Items.DoesNotExist:
        return HttpResponseNotFound('<h2>Item not found</h2>')

def delete(request, id):
    try:
        items = Items.objects.get(id=id)
        items.delete()
        return HttpResponseRedirect('/')
    except Items.DoesNotExist:
        return HttpResponseNotFound('<h2>Phone not found</h2>')








def create_test(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Замените 'success' на имя страницы, куда вы хотите перейти после успешного сохранения товара
    else:
        form = ItemsForm()

    return render(request, 'create.html', {'form': form})