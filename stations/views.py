import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))
    paginator = Paginator(data, 10)
    page = request.GET.get('page', 1)
    data = paginator.get_page(page)


    context = {
        'bus_stations': data,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
