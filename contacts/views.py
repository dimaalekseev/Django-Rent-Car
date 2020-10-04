from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contacts


def contact(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        car_manager = request.POST['car_manager']
        car_name = request.POST['car_name']
        car_id = request.POST['car_id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['text']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(
                car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "Car has already rented!")
                return redirect("/carlist/"+car_id)
        contact = Contacts(car=car_name, car_id=car_id, name=name,
                           email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'New Car order!', #тема листа
            'Rent order' + " " + name + " " + car_name + " " + phone + " " + email + " " + message, #вміст листа
            'thedimaalekseev@gmail.com', #від кого посилаємо
            ['aleksieiev_ak16@nuwm.edu.ua'], #кому посилаємо, в даному випадку менеджеру
            fail_silently=False,
        )
        messages.success(request, "Your request submitted")
        return redirect("/carlist/"+car_id)
