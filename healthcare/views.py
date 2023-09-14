from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from main.settings import EMAIL_HOST_USER
from .models import Hair, Dentist, Plastic, General, Optic


def get_msg_health(request, *args, **kwargs):
    name, email, phone, class_status, person_no, have_child = '', '', '', '', '', ''
    age, disease, date, full, child_no, notes = '', '', '', '', '', ''
    error_msg = ''
    try:
        name = request.POST.get('fullname', 'NO')
        email = request.POST.get('email', 'NO')
        phone = request.POST.get('phone', 'NO')
        age = request.POST.get('age', 'NO')
        disease = request.POST.get('disease', 'NO')
        date = request.POST.get('date', 'NO')
        full = request.POST.get('full', 'NO')
        class_status = request.POST.get('class_status', False)
        person_no = request.POST.get('person_no', 'NO')
        have_child = request.POST.get('have_child', 'Dont Have Children')
        child_no = request.POST.get('child_no', 'NO')
        notes = request.POST.get('note', 'NO')
    except MultiValueDictKeyError as e:
        error_msg = e
    return name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg


# English pages
def hair(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(request)
        choice1 = request.POST.get('choice1', 'NO')
        choice2 = request.POST.get('choice2', 'NO')
        choice3 = request.POST.get('choice3', 'NO')
        choice4 = request.POST.get('choice4', 'NO')
        Hair(fullname=name, email=email, phone=phone).save()
        message = f"""
               Full name:       {name}
               Email:           {email}
               Phone Number:    {phone}
               Age:             {age}
               Has Diseases:    {disease}
               Date:            {date}
               Treatment Area:  {choice1} - {choice2} - {choice3} - {choice4}
               Full Services:   {full}
               Class Status:    {class_status}
               Person Number:   {person_no}
               Have Children:   {have_child}
               Children Number: {child_no}
               Other Notes:     {notes}          
           """
        send_mail('Hair Transplant', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/health/hair.html', context)


def dentist(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1 = request.POST.get('choice1', 'NO')
        choice2 = request.POST.get('choice2', 'NO')
        choice3 = request.POST.get('choice3', 'NO')
        choice4 = request.POST.get('choice4', 'NO')
        Dentist(fullname=name, email=email, phone=phone).save()
        message = f"""
                   Full name:       {name}
                   Email:           {email}
                   Phone Number:    {phone}
                   Age:             {age}
                   Has Diseases:    {disease}
                   Date:            {date}
                   Treatment Type:  {choice1} - {choice2} - {choice3} - {choice4}
                   Full Services:   {full}
                   Class Status:    {class_status}
                   Person Number:   {person_no}
                   Have Children:   {have_child}
                   Children Number: {child_no}
                   Other Notes:     {notes}          
               """
        send_mail('Dentistry', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/health/dentist.html', context)


def optic(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        Optic(fullname=name, email=email, phone=phone).save()
        message = f"""
                      Full name:       {name}
                      Email:           {email}
                      Phone Number:    {phone}
                      Age:             {age}
                      Has Diseases:    {disease}
                      Date:            {date}
                      Full Services:   {full}
                      Class Status:    {class_status}
                      Person Number:   {person_no}
                      Have Children:   {have_child}
                      Children Number: {child_no}
                      Other Notes:     {notes}          
                  """
        send_mail('Ophthalmology', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/health/optic.html', context)


def plastic(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1, choice6 = request.POST.get('option1', 'NO'), request.POST.get('option6', 'NO')
        choice2, choice7 = request.POST.get('option2', 'NO'), request.POST.get('option7', 'NO')
        choice3, choice8 = request.POST.get('option3', 'NO'), request.POST.get('option8', 'NO')
        choice4, choice9 = request.POST.get('option4', 'NO'), request.POST.get('option9', 'NO')
        choice5, choice10 = request.POST.get('option5', 'NO'), request.POST.get('option10', 'NO')
        Plastic(fullname=name, email=email, phone=phone).save()
        message = f"""
                       Full name:       {name}
                       Email:           {email}
                       Phone Number:    {phone}
                       Age:             {age}
                       Has Diseases:    {disease}
                       Date:            {date}
                       Treatment Type:  
                            {choice1} - {choice2} - {choice3} - {choice4} - {choice5}
                            {choice6} - {choice7} - {choice8} - {choice9} - {choice10}
                       Full Services:   {full}
                       Class Status:    {class_status}
                       Person Number:   {person_no}
                       Have Children:   {have_child}
                       Children Number: {child_no}
                       Other Notes:     {notes}          
                   """
        send_mail('Plastic and Reconstructive Surgery', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/health/plastic.html', context)


def general(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1 = request.POST.get('type', 'NO')
        General(fullname=name, email=email, phone=phone).save()
        message = f"""
                       Full name:       {name}
                       Email:           {email}
                       Phone Number:    {phone}
                       Age:             {age}
                       Has Diseases:    {disease}
                       Date:            {date}
                       Treatment Type:  {choice1}
                       Full Services:   {full}
                       Class Status:    {class_status}
                       Person Number:   {person_no}
                       Have Children:   {have_child}
                       Children Number: {child_no}
                       Other Notes:     {notes}          
                   """
        send_mail('General Treatment', message, str(email), (EMAIL_HOST_USER,))
        success_msg = f"Dear {name}, your message has been sent successfully, we'll reply you Shortly"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'en/health/general.html', context)


# Arabic pages
def hair_ar(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(request)
        choice1 = request.POST.get('choice1', 'NO')
        choice2 = request.POST.get('choice2', 'NO')
        choice3 = request.POST.get('choice3', 'NO')
        choice4 = request.POST.get('choice4', 'NO')
        Hair(fullname=name, email=email, phone=phone).save()
        message = f"""
                الاسم الكامل :       {name}
                البريد الالكتروني :           {email}
                رقم الهاتف :    {phone}
                العمر :             {age}
                يوجد أمراض مزمنة :    {disease}
                التاريخ :            {date}
                منطقة العلاج :  {choice1} - {choice2} - {choice3} - {choice4}
                خدمات شاملة :   {full}
                الدرجة :    {class_status}
                عدد الأشخاص:   {person_no}
                يوجد أطفال:   {have_child}
                عدد الأطفال: {child_no}
                ملاحظات أخرى:     {notes}           
           """
        send_mail('زراعة الشعر', message, str(email), (EMAIL_HOST_USER,))
        success_msg = "لقد تم ارسال رسالتك بنجاح , سوف يتم الرد عليكم قريبا!"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/health/hair.html', context)


def dentist_ar(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1 = request.POST.get('choice1', 'NO')
        choice2 = request.POST.get('choice2', 'NO')
        choice3 = request.POST.get('choice3', 'NO')
        choice4 = request.POST.get('choice4', 'NO')
        Dentist(fullname=name, email=email, phone=phone).save()
        message = f"""
                الاسم الكامل :       {name}
                البريد الالكتروني :           {email}
                رقم الهاتف :    {phone}
                العمر :             {age}
                يوجد أمراض مزمنة :    {disease}
                التاريخ :            {date}
                نوع العلاج :  {choice1} - {choice2} - {choice3} - {choice4}
                خدمات شاملة :   {full}
                الدرجة :    {class_status}
                عدد الأشخاص:   {person_no}
                يوجد أطفال:   {have_child}
                عدد الأطفال: {child_no}
                ملاحظات أخرى:     {notes}         
               """
        send_mail('طب الأسنان', message, str(email), (EMAIL_HOST_USER,))
        success_msg = "لقد تم ارسال رسالتك بنجاح , سوف يتم الرد عليكم قريبا!"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/health/dentist.html', context)


def optic_ar(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        Optic(fullname=name, email=email, phone=phone).save()
        message = f"""
                الاسم الكامل :       {name}
                البريد الالكتروني :           {email}
                رقم الهاتف :    {phone}
                العمر :             {age}
                يوجد أمراض مزمنة :    {disease}
                التاريخ :            {date}
                خدمات شاملة :   {full}
                الدرجة :    {class_status}
                عدد الأشخاص:   {person_no}
                يوجد أطفال:   {have_child}
                عدد الأطفال: {child_no}
                ملاحظات أخرى:     {notes}          
                  """
        send_mail('طب العيون', message, str(email), (EMAIL_HOST_USER,))
        success_msg = "لقد تم ارسال رسالتك بنجاح , سوف يتم الرد عليكم قريبا!"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/health/optic.html', context)


def plastic_ar(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1, choice6 = request.POST.get('option1', 'NO'), request.POST.get('option6', 'NO')
        choice2, choice7 = request.POST.get('option2', 'NO'), request.POST.get('option7', 'NO')
        choice3, choice8 = request.POST.get('option3', 'NO'), request.POST.get('option8', 'NO')
        choice4, choice9 = request.POST.get('option4', 'NO'), request.POST.get('option9', 'NO')
        choice5, choice10 = request.POST.get('option5', 'NO'), request.POST.get('option10', 'NO')
        Plastic(fullname=name, email=email, phone=phone).save()
        message = f"""
                الاسم الكامل :       {name}
                البريد الالكتروني :           {email}
                رقم الهاتف :    {phone}
                العمر :             {age}
                يوجد أمراض مزمنة :    {disease}
                التاريخ :            {date}
                نوع العلاج :  
                {choice1} - {choice2} - {choice3} - {choice4} - {choice5}
                {choice6} - {choice7} - {choice8} - {choice9} - {choice10}
                خدمات شاملة :   {full}
                الدرجة :    {class_status}
                عدد الأشخاص:   {person_no}
                يوجد أطفال:   {have_child}
                عدد الأطفال: {child_no}
                ملاحظات أخرى:     {notes}           
                   """
        send_mail('عمليات التجميل ', message, str(email), (EMAIL_HOST_USER,))
        success_msg = "لقد تم ارسال رسالتك بنجاح , سوف يتم الرد عليكم قريبا!"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/health/plastic.html', context)


def general_ar(request):
    success_msg, error_msg = '', ''
    if request.method == 'POST':
        name, email, phone, age, disease, date, full, class_status, person_no, have_child, child_no, notes, error_msg = get_msg_health(
            request)
        choice1 = request.POST.get('type', 'NO')
        General(fullname=name, email=email, phone=phone).save()
        message = f"""
                    الاسم الكامل :       {name}
                    البريد الالكتروني :           {email}
                    رقم الهاتف :    {phone}
                    العمر :             {age}
                    يوجد أمراض مزمنة :    {disease}
                    التاريخ :            {date}
                    نوع العلاج :  {choice1}
                    خدمات شاملة :   {full}
                    الدرجة :    {class_status}
                    عدد الأشخاص:   {person_no}
                    يوجد أطفال:   {have_child}
                    عدد الأطفال: {child_no}
                    ملاحظات أخرى:     {notes}          
                   """
        send_mail('علاجات عامة', message, str(email), (EMAIL_HOST_USER,))
        success_msg = "لقد تم ارسال رسالتك بنجاح , سوف يتم الرد عليكم قريبا!"
    context = {
        'error_msg': error_msg,
        'success_msg': success_msg
    }
    return render(request, 'ar/health/general.html', context)

