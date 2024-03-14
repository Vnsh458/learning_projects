from django.shortcuts import render
from App1.models import Worker


def gritting_mes(request):

    all_workers = Worker.objects.all()
    print(all_workers)

    return render(request, 'Greeting.html')


def about_me(requests):
    return render(requests, 'About.html')