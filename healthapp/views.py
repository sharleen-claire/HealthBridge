from django.shortcuts import render,redirect,get_object_or_404

from healthapp.models import *

# Create your views here.
def home(request):
    return render(request,  'index.html')

def starter(request):
    return render(request,  'starter-page.html')


def about(request):
    return render(request,  'about.html')

def appointment(request):
    if request.method == 'POST':
        all = Myappointment()
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        datetime = request.POST['date']
        department = request.POST['department']
        doctor = request.POST['doctor']

        all.save()

        return render(request, 'appointment.html')
    else:
        return render(request, 'appointment.html')


def show(request):
    allappointment =Myappointment.objects.all()
    return render(request, 'show.html', {'allappointment':allappointment})


def delete(request, id):
    deleteappointment = Myappointment.objects.filter(id=id)
    deleteappointment.delete()
    return redirect('/show')

def edit(request, id):
    editappointment =get_object_or_404(Myappointment,id=id)
    if request.method =='POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.department = request.POST.get('date')
        editappointment.doctor = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.doctor = request.POST.get('message')

        editappointment.save()
        return redirect('/show')

    else:
        return render(request, 'edit.html', {'editappointment':editappointment})



    
