import uuid

from django.shortcuts import render
from django.http import HttpResponse

from heatMap.models import Urunler


def index(request):

    # liste = Urunler.objects.all()
    liste = Urunler.objects.all()
    title = "TEST BAŞLIK"

    context = {'liste': liste, 'title': title}
    return render(request, 'heatMap/index.html', context)

def search(request, some_int):
    liste = some_int
    title = 'SECTINIZ'
    context = {'liste': liste, 'title': title}

    # htmladi = str(uuid.uuid4()) + '.html'
    # templates/heatMap/49194-1419849.html yaz
    return render(request, 'heatMap/index.html', context)
    # return render(request, 'heatMap/49194-1419849.html', context)

# Create your views here.
