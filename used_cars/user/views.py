from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from .models import UserDetails, CarDetails, EnquiryDetails


# Create your views here.
def base(request):
    return render(request, 'user/base.html')


def home(request):
    uid = request.session['id']
    noti_count = EnquiryDetails.objects.count()
    username = request.session['username']
    data = CarDetails.objects.all()
    car_data = CarDetails.objects.filter(user_id=uid)
    enquiry_data = EnquiryDetails.objects.all()

    return render(request, 'user/home.html',
                  {'id': uid, 'username': username,
                   'data': data, 'car_data': car_data,
                   'enquiry_data': enquiry_data,
                   'noti_count':noti_count})


def register_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        email = request.POST.get('email')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass2 == pass1:
            UserDetails(username=name, phone=phone, password=pass1, state=state, email=email, zipcode=zipcode,
                        address=address).save()
            return redirect("/")
        else:
            return redirect("/register")

    else:
        return render(request, 'user/register.html')


def login_request(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        signin = UserDetails.objects.filter(username=username, password=password)
        if signin:
            a = UserDetails.objects.get(username=username, password=password)
            uid = a.user_id
            username = a.username
            request.session['id'] = uid
            request.session['username'] = username
            return redirect("http://127.0.0.1:8000/home")
        else:
            return redirect("/login")
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')


def add_cars(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        series = request.POST.get('series')
        color = request.POST.get('color')
        year = request.POST.get('year')
        kms = request.POST.get('kms')
        fuel = request.POST.get('fuel')
        insurance = request.POST.get('insurance')
        photo = request.FILES.get('image')
        uid = request.session['id']
        price = request.POST.get('prize')
        user = UserDetails.objects.get(user_id=uid)
        print(type(user))

        CarDetails(user_id=user, brand=brand, model=model, series=series, color=color, year=year, kms_driven=kms,
                   fuel_type=fuel, insurance_till=insurance, photo=photo, expected_prize=price).save()
        return redirect("/home")
    else:
        return render(request, 'user/add_cars.html')


def update_cars(request):
    if request.method == 'POST':
        c_id = request.GET.get("id")
        car = CarDetails.objects.get(car_id=int(c_id))

        brand = request.POST.get('brand')
        model = request.POST.get('model')
        series = request.POST.get('series')
        color = request.POST.get('color')
        year = request.POST.get('year')
        kms = request.POST.get('kms')
        fuel = request.POST.get('fuel')
        insurance = request.POST.get('insurance')
       # photo = request.FILES.get('image')
        price = request.POST.get('prize')

        car.brand = brand
        car.model = model
        car.series = series
        car.color = color
        car.year = year
        car.kms = kms
        car.year = year
        car.fuel = fuel
        car.insurance = insurance
      #  car.photo = photo
        car.price = price

        car.save()

        context = {'msg': 'Car Details Updated', 'car': car}
        return redirect('/home', context)

    else:
        c_id = request.GET.get('id')
        car = CarDetails.objects.get(car_id=int(c_id))
        context = {'car': car}
        return render(request, 'user/up_cars.html', context)


def del_cars(request):
    c_id = request.GET.get('id')
    cars = CarDetails.objects.get(car_id=int(c_id))
    cars.delete()
    return redirect('/home')


def message_user(request, car_id):
    print(car_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)

        uid = request.session['id']
        user = UserDetails.objects.get(user_id=uid)
        print(type(user))
        print(uid)

        c_id = request.GET.get('id')
        #user_id = CarDetails.objects.get(user_id=int(c_id))
        car = CarDetails.objects.get(car_id=car_id)

        context = {'car': car, 'user': user}

        EnquiryDetails(car_id=car, interested_user_id=user, message=message).save()
        return redirect('/home', context)
    else:
        return render(request, 'user/mesg.html')
