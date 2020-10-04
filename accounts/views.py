from django.shortcuts import render, redirect
from django.contrib import messages, auth
# підключаємо таблицю користувачів з БД
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:  # якщо паролі співпадають
            # перевіряємо чи вже існує такий username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken.")
                return redirect(register)
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already taken")
                    return redirect(register)
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password, first_name=first_name, last_name=last_name)  # створюємо користувача
                    user.save()  # зберігаємо його
                    messages.success(
                        request, "You are registered successfully!")
                    return redirect(login)
        else:
            # генеруємо помилку з _ALERTS.HTML, приймаємо відповідь від сервера
            messages.error(request, "Passwords do not match")
        return redirect('register')
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('dashboard')
        else:
            messages.error(request, "Login or password incorrect!")
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    # знищуємо сесію, перенаправляємось на головну сторінку
    if request.method == "POST":
        auth.logout(request)
    messages.success(request, "See you later!")
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")
