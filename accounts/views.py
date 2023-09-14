from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from administration.models import OffersEN, OfferAr
from main.settings import EMAIL_HOST_USER
from .forms import LoginForm, RegisterForm, get_username


# English pages

def home(request):
    context = {
        'offers': OffersEN.objects.all()
    }
    return render(request, 'en/index.html', context)


def offer_details(request, pk):
    offer = OffersEN.objects.get(id=pk)
    context = {
        'offer': offer,
    }
    return render(request, 'en/offer_details.html', context)


def delete_offer(request, pk):
    offer = OffersEN.objects.get(id=pk)
    offer.delete()
    return redirect('home')
    context = {
        'offer': offer,
    }
    return render(request, 'en/index.html', context)


def about(request):
    return render(request, 'en/about.html')


def contacts(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', 'NO')
        phone = request.POST.get('phone', 'NO')
        message = request.POST.get('message', 'NO')
        email = request.POST.get('email', 'NO')
        msg = f"""
                Full Name:      {name}
                Phone Number:   {phone}
                Email:          {email}
                Message:        {message}
        """
        send_mail('General Contact', msg, email, (EMAIL_HOST_USER,))
        success_msg = "Your message hes been sent successfully, we'll reply you shortly!"
    return render(request, 'en/contacts.html', {'success_msg': success_msg})


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = get_username(email)
        password = request.POST['password']
        user = User(first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=make_password(password))
        user.save()
        messages.success(request, user.username + ' Created Successfully !')
        auth.login(request, user)
        return redirect('home')

    context = {'form': RegisterForm()}
    return render(request, 'en/auth/register.html', context)


def login_user(request):
    form = LoginForm()
    error = ''
    if request.method == 'POST':
        username = get_username(request.POST['username'])
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            form = LoginForm(request.POST)
            error = f"The username or password is wrong!"
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'en/auth/login.html', context)


@login_required(login_url='login')
def logout_user(request):
    auth.logout(request)
    return redirect('home')


# Arabic pages

def home_ar(request):
    context = {
        'offers': OfferAr.objects.all()
    }
    return render(request, 'ar/index.html', context)


def offer_details_ar(request, pk):
    offer = OfferAr.objects.get(id=pk)
    context = {
        'offer': offer,
    }
    return render(request, 'ar/offer_details.html', context)


def delete_offer_ar(request, pk):
    offer = OfferAr.objects.get(id=pk)
    offer.delete()
    return redirect('home_ar')
    context = {
        'offer': offer,
    }
    return render(request, 'ar/index.html', context)


def about_ar(request):
    return render(request, 'ar/about.html')


def contacts_ar(request):
    success_msg = ''
    if request.method == 'POST':
        name = request.POST.get('name', 'NO')
        phone = request.POST.get('phone', 'NO')
        message = request.POST.get('message', 'NO')
        email = request.POST.get('email', 'NO')
        msg = f"""
                الاسم الكامل:      {name}
                رقم الهاتف:   {phone}
                البريد الالكتروني:          {email}
                الرسالة:        {message}
        """
        send_mail('من تواصل معنا', msg, email, (EMAIL_HOST_USER,))
        success_msg = 'تم ارسال رسالتك بنجاح و سيتم الرد عليك قريبا'
    return render(request, 'ar/contacts.html', {'success_msg': success_msg})


def register_ar(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = get_username(email)
        password = request.POST['password']
        user = User(first_name=firstname,
                    last_name=lastname,
                    email=email,
                    username=username,
                    password=make_password(password))
        user.save()
        messages.success(request, user.username + ' تم التسجيل بنجاح !')
        auth.login(request, user)
        return redirect('home_ar')

    context = {'form': RegisterForm()}
    return render(request, 'ar/auth/register.html', context)


def login_user_ar(request):
    form = LoginForm()
    error = ''
    if request.method == 'POST':
        username = get_username(request.POST['username'])
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home_ar')
        else:
            form = LoginForm(request.POST)
            error = f"يوجد خطأ في اسم المستخدم او كلمة المرور!"
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'ar/auth/login.html', context)


@login_required(login_url='login_ar')
def logout_user_ar(request):
    auth.logout(request)
    return redirect('home_ar')
