from django.shortcuts import render, HttpResponse
from shop.models import Item


def index(request):
    data = Item.objects.all()
    return render(request, 'index.html', {'data': data})


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def search(request):
    query = request.GET['query']
    data = Item.objects.filter(item_name__icontains=query)
    return render(request, 'search.html', {'data': data})


