from django.shortcuts import render

from cars.models import CarsList
from carmanager.models import CarManager
from .car_info import vendor_list, models_list, engine_list, transmission_list


def index(request):
    # на головній сторінці в каруселі відображаємо лише перші 4 машини з бази
    cars = CarsList.objects.all().filter(is_published=True)[:4]
    query = CarsList.objects.order_by("vendor")
    random_car = CarsList.objects.order_by('?')[0] #вивід рандомної машини на головній сторінці

    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)

    context = {
        'cars': cars,
        "vendor_list": vendor_list,
        "models_list": models_list,
        "engine_list": engine_list,
        "transmission_list": transmission_list,
        "search_cars": query,
        "request_value": request.GET,
        "cars": query,  # в список cars поміщаємо результат запиту query
        "rnd_car":random_car,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all()[:6]
    context = {
        'managers': managers,
        'title': 'About Us',

    }

    return render(request, 'pages/about.html', context)


def services(request):
    data = {
        "title": "Our services"
    }
    return render(request, 'pages/services.html', data)


def contact(request):
    data = {
        "title": "Contact Us"
    }
    return render(request, 'pages/contact.html', data)

# Пошук


def search(request):
    # дістаємо get-параметри(атрибути з адресної строки для пошуку) і будемо робити контекст на основі того що нам передалось
    # запрос в базу, сортуємо по полю vendor
    query = CarsList.objects.order_by("vendor")

    # перевіряємо чи в масиві request.GET є параметри, які ми шукаємо
    if "vendor" in request.GET:
        # покладемо в цю змінну значення (параметр з адресної строки) для подальшого пошуку
        vendor = request.GET["vendor"]
        if vendor:  # якщо не пусто
            # ще раз звертаємось до бази і фільтруємо по полю vendor, iexact - знаходимо точне співпадіння, без урахування регістрів
            query = query.filter(vendor__iexact=vendor)

    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)

    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            query = query.filter(transmission__iexact=transmission)

    context = {
        "title": "Find your car!",
        "vendor_list": vendor_list,
        "models_list": models_list,
        "engine_list": engine_list,
        "transmission_list": transmission_list,
        "cars": query,  # в список cars поміщаємо результат запиту query
        "request_value": request.GET,
    }
    return render(request, 'pages/search.html', context)
