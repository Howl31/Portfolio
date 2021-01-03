from django.shortcuts import render
from .models import Resume, Contact

# Create your views here.


def home(request):
    data = Resume.objects.all()
    resume = data[0].pic
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        query = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        query.save()
    return render(request, 'index.html', {'resume': resume.url})


def portfolio(request):
    data = Resume.objects.all()
    resume = data[0].pic
    return render(request, 'index.html', {'resume': resume.url})


def about(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        query = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        query.save()
    return render(request, 'index.html')

