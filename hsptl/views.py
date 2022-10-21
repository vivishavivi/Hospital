from django.shortcuts import render
from.forms import BookingForm
from django.http import HttpResponse
from . models import Doctors, Department
def index(request):
    return render(request,'index.html')
def doctors(request):
    doctors = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',doctors)
def department(request):
    department = {
        'department': Department.objects.all()
    }
    return render(request,'department.html',department)
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    form = BookingForm()
    booking = {
        'form': form
    }
    return render(request,'booking.html',booking)
def about(request):
     return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')