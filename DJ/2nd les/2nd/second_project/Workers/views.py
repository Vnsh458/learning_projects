from django.shortcuts import render
from models import Worker


def index_page(requests):
    all_workers = Worker.object.all()
    print(all_workers)
    return render(requests, 'GR.html')
