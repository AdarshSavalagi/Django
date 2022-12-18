from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import register
# Create your views here.


def Register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        if phone == "":
            phone = 0000000
        usn = request.POST.get('usn')
        # sem = request.POST.get('sem')
        email = request.POST.get('email')
        branch = request.POST.get('branch')
        laptop = request.POST.get('laptop')
        if laptop == 'on':
            laptop = True
        else:
            laptop = False
        stu = register(Name=name, Phone=phone, Usn=usn,  Email=email,
                       Branch=branch, Laptop=laptop, date=datetime.today())
        stu.save()
        return HttpResponse("submitted bro")
    else:
        return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')
