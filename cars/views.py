from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import CarsList

def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)  #список, що приймає об'єкти з БД, фільтруємо по заданому полю 

    paginator=Paginator(carlist, 6)
    page = request.GET.get("page")
    paged_carlist=paginator.get_page(page)
    #словник з об'єктів, які ми отримуємо з бази
    context = {        
        "carlist":paged_carlist,
        'title':'Cars list',
    }
    return render(request, "carlist/carlist.html", context)

def singlecar(request, carlist_id):
    car = get_object_or_404(CarsList, pk=carlist_id) #Вызывает get() для переданного менеджера модели и возвращает полученный объект. Вызывает исключение Http404 вместо DoesNotExist.
    #pk - первичный ключ
    context = {
        'car':car
    }
    return render(request, "carlist/singlecar.html", context)
