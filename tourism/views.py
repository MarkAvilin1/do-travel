from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from main.settings import EMAIL_HOST_USER
from .models import Ticket, Booking, Trip, Visa, Education


# Create your views here.

def get_msg_tour(request, *args, **kwargs):
    name, email, phone, class_status, person_no, have_child, child_no, notes = '', '', '', '', '', '', '', ''
    error_msg = ''
    try:
        name = request.POST.get('fullname', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        class_status = request.POST.get('class_status', False)
        person_no = request.POST.get('person_no', 'NO')
        have_child = request.POST.get('have_child', 'Dont Have Children')
        child_no = request.POST.get('child_no', 'NO')
        notes = request.POST.get('note', 'NO')
    except MultiValueDictKeyError as e:
        error_msg = e
    return name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg


# English pages
def tickets(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        distance_from = request.POST.get('country_from', 'NO')
        distance_to = request.POST.get('country_to', 'NO')
        one_two = request.POST.get('select', False)
        date_dep = request.POST.get('date_dep', 'NO')
        date_re = request.POST.get('date_re', 'NO')
        if date_dep > date_re != '':
            date_error = f"The date doesn't exist, please be sure that you choose right date!"
        else:
            if name != 'NO' and email != 'NO':
                Ticket(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'Pleas input your fullname and email address'
            message = f"""
                Full name:      {name}
                Email:          {email}
                Phone Number:   {phone}
                From:           {distance_from}
                To:             {distance_to}
                Travel Status:  {one_two}
                Departure Date: {date_dep}
                Return Date:    {date_re}
                Class Status:   {class_status}
                Person Number:  {person_no}
                Have Children:  {have_child}
                Children Number:{child_no}
                Other Notes:    {notes}          
            """
            send_mail('Book Tickets', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/tourism/tickets.html', context)


def booking(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        country = request.POST.get('country', 'NO')
        city = request.POST.get('city', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = "The date doesn't exist, please be sure that you choose right date!"
        else:
            if name != 'NO' and email != 'NO':
                Booking(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'Pleas input your fullname and email address'
            message = f"""
                    Full name:      {name}
                    Email:          {email}
                    Phone Number:   {phone}
                    Country:        {country}
                    City:           {city}
                    Date From:      {date_from}
                    Date To:        {date_to}
                    Class Status:   {class_status}
                    Person Number:  {person_no}
                    Have Children:  {have_child}
                    Children Number:{child_no}
                    Other Notes:    {notes}          
                """
            send_mail('Hotel Booking', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"Dear {name}, your message has been sent successfully, " \
                          f"we'll reply you ASAP" if name != 'NO' else ""
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/tourism/booking.html', context)


def trips(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        cities = request.POST.get('cities', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = "The date doesn't exist, please be sure that you choose right date!"
        else:
            if name != 'NO' and email != 'NO':
                Trip(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'Pleas input your fullname and email address'
            message = f"""
                        Full name:      {name}
                        Email:          {email}
                        Phone Number:   {phone}
                        Cities:         {cities}
                        Date From:      {date_from}
                        Date To:        {date_to}
                        Class Status:   {class_status}
                        Person Number:  {person_no}
                        Have Children:  {have_child}
                        Children Number:{child_no}
                        Other Notes:    {notes}
                    """
            send_mail('Plan own trip', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"Dear {name}, your message has been sent successfully, " \
                          f"we'll reply you shortly" if name != 'NO' else ""
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/tourism/trips.html', context)


def visas(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        nationality = request.POST.get('nationality', 'NO')
        visa = request.POST.get('visa', 'NO')
        visa_type = request.POST.get('visa_type', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = "The date doesn't exist, please be sure that you choose right date!"
        else:
            if name != 'NO' and email != 'NO':
                Visa(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'Pleas input your fullname and email address'
            message = f"""
                        Full name:      {name}
                        Email:          {email}
                        Phone Number:   {phone}
                        Nationality:    {nationality}
                        Visa To:        {visa}
                        Start Date:     {date_from}
                        Until :         {date_to}
                        Visa Type:      {visa_type}
                        Person Number:  {person_no}
                        Have Children:  {have_child}
                        Children Number:{child_no}
                        Other Notes:    {notes}
                    """
            send_mail('Apply for visa', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you shortly"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/tourism/visas.html', context)


def education(request):
    success_msg, errors = '', ''
    if request.method == 'POST':
        name = request.POST.get('fullname', 'NO')
        nationality = request.POST.get('nationality', 'NO')
        gender = request.POST.get('gender', 'NO')
        age = request.POST.get('age', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        finish = request.POST.get('finish', 'NO')
        want = request.POST.get('want', 'NO')
        city = request.POST.get('city', 'NO')
        notes = request.POST.get('note', 'NO')
        Education(fullname=name, email=email, phone=phone).save()
        message = f"""
                        Full name:      {name}
                        Email:          {email}
                        Phone Number:   {phone}
                        Nationality:    {nationality}
                        Gender :        {gender}
                        Age:            {age}
                        Start Date:     {date_from}
                        Has finished:   {finish}                            
                        Wants:          {want}
                        City wants:     {city}
                        Other Notes:    {notes}
                    """
        send_mail('Admission to study', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you shortly"
    context = {
        'errors': errors,
        'success_msg': success_msg
    }
    return render(request, 'en/education.html', context)


# Arabic pages
def tickets_ar(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        distance_from = request.POST.get('country_from', 'NO')
        distance_to = request.POST.get('country_to', 'NO')
        one_two = request.POST.get('select', False)
        date_dep = request.POST.get('date_dep', 'NO')
        date_re = request.POST.get('date_re', 'NO')
        if date_dep > date_re != '':
            date_error = f"التاريخ غير صحيح يرجى التأكد من صحة الإدخال!"
        else:
            if name != 'NO' and email != 'NO':
                Ticket(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'يرجى كتابة الاسم الكامل و البريد الالكتروني'
            message = f"""
                        الاسم الكامل :      {name}
                        البريد الالكتروني :          {email}
                        رقم الهاتف:   {phone}
                        من :           {distance_from}
                        الى :             {distance_to}
                        نوع التذكرة :  {one_two}
                        تاريخ المغادرة : {date_dep}
                        تاريخ العودة :    {date_re}
                        الدرجة :   {class_status}
                        عدد الأشخاص :  {person_no}
                        يوجد أطفال :  {have_child}
                        عدد الأطفال :{child_no}
                        ملاحظات أحرى :    {notes}       
            """
            send_mail('تذاكر السفر', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"|لقد تم ارسال رسالتك بنجاح , سوف نقوم بالرد قريبا!"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/tourism/tickets.html', context)


def booking_ar(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        country = request.POST.get('country', 'NO')
        city = request.POST.get('city', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = f"التاريخ غير صحيح يرجى التأكد من صحة الإدخال!"
        else:
            if name != 'NO' and email != 'NO':
                Booking(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'يرجى كتابة الاسم الكامل و البريد الالكتروني'
            message = f"""
                    الاسم الكامل :      {name}
                    البريد الالكتروني :          {email}
                    رقم الهاتف:   {phone}
                    البلد :        {country}
                    المدينة :           {city}
                    التاريخ من :      {date_from}
                    التاريخ الى :        {date_to}
                    الدرجة :   {class_status}
                    عدد الأشخاص :  {person_no}
                    يوجد أطفال :  {have_child}
                    عدد الأطفال :{child_no}
                    ملاحظات أحرى :    {notes}       
                """
            send_mail('حجز فندق', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"|لقد تم ارسال رسالتك بنجاح , سوف نقوم بالرد قريبا!"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/tourism/booking.html', context)


def trips_ar(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        cities = request.POST.get('cities', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = f"التاريخ غير صحيح يرجى التأكد من صحة الإدخال!"
        else:
            if name != 'NO' and email != 'NO':
                Trip(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'يرجى كتابة الاسم الكامل و البريد الالكتروني'
            message = f"""
                        الاسم الكامل :      {name}
                        البريد الالكتروني :          {email}
                        رقم الهاتف:   {phone}
                        المدن :         {cities}
                        التاريخ من :      {date_from}
                        التاريخ الى :        {date_to}
                        الدرجة :   {class_status}
                        عدد الأشخاص :  {person_no}
                        يوجد أطفال :  {have_child}
                        عدد الأطفال :{child_no}
                        ملاحظات أحرى :    {notes}
                    """
            send_mail('طلب رحلة خاصة', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"|لقد تم ارسال رسالتك بنجاح , سوف نقوم بالرد قريبا!"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/tourism/trips.html', context)


def visas_ar(request):
    success_msg, error_msg, date_error, errors = '', '', '', ''
    if request.method == 'POST':
        name, email, phone, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_tour(request)
        nationality = request.POST.get('nationality', 'NO')
        visa = request.POST.get('visa', 'NO')
        visa_type = request.POST.get('visa_type', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        date_to = request.POST.get('date_to', 'NO')
        if date_from > date_to != '':
            date_error = f"التاريخ غير صحيح يرجى التأكد من صحة الإدخال!"
        else:
            if name != 'NO' and email != 'NO':
                Visa(fullname=name, email=email, phone=phone).save()
            else:
                errors = 'يرجى كتابة الاسم الكامل و البريد الالكتروني'
            message = f"""
                        الاسم الكامل :      {name}
                        البريد الالكتروني :          {email}
                        رقم الهاتف :   {phone}
                        الجنسية :    {nationality}
                        فيزا الى :        {visa}
                        التاريخ :     {date_from}
                        حتى :         {date_to}
                        نوع الفيزا :      {visa_type}
                        عدد الأشخاص :  {person_no}
                        يوجد أطفال :  {have_child}
                        عدد الأطفال :{child_no}
                        ملاحظات أحرى :    {notes}
                    """
            send_mail('التقديم للحصول على الفيزا', message, str(email), (EMAIL_HOST_USER,))
            success_msg = f"|لقد تم ارسال رسالتك بنجاح , سوف نقوم بالرد قريبا!"
    context = {
        'date_error': date_error,
        'errors': errors,
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/tourism/visas.html', context)


def education_ar(request):
    success_msg, errors = '', ''
    if request.method == 'POST':
        name = request.POST.get('fullname', 'NO')
        nationality = request.POST.get('nationality', 'NO')
        gender = request.POST.get('gender', 'NO')
        age = request.POST.get('age', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        date_from = request.POST.get('date_from', 'NO')
        finish = request.POST.get('finish', 'NO')
        want = request.POST.get('want', 'NO')
        city = request.POST.get('city', 'NO')
        notes = request.POST.get('note', 'NO')
        Education(fullname=name, email=email, phone=phone).save()
        message = f"""
                        الاسم الكامل :  {name}         
                        البريد الالكتروني :      {email}:        
                        رقم الهاتف : {phone}        
                        الجنسية : {nationality}    
                        الجنس : {gender}       
                        العمر : {age}          
                        تاريخ ألبدء : {date_from}    
                        انهى دراسة : {finish}          
                        يريد دراسة : {want}         
                        المدينة او الجامعة :  {city}          
                        الملاحظات : {notes}        
                    """
        send_mail('القبول الجامعي', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"|لقد تم ارسال رسالتك بنجاح , سوف نقوم بالرد قريبا!"
    context = {
        'errors': errors,
        'success_msg': success_msg
    }
    return render(request, 'ar/education.html', context)
