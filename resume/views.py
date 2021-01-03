from django.shortcuts import render
from .models import Resume, Contact
from django.core.mail import send_mail

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
        send_mail(
            'Your Query Received',
            'Thank you for showing interest. I will get in touch with you as soon as possible.',
            'howl31180109@gmail.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'Query received from' + name,
            name + "and" + email,
            'howl31180109@gmail.com',
            ['armakshay31@gmail.com'],
            fail_silently=False,
        )
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
        send_mail(
            'Your Query Received',
            'Thank you for showing interest. I will get in touch with you as soon as possible.',
            'howl31180109@gmail.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'Query received from' + name,
            name + "and" + email,
            'howl31180109@gmail.com',
            ['armakshay31@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'index.html')

