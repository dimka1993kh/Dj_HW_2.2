from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .data import list_station



def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request, page=None):
    # Определение номеров страниц
    prev_page_url = None
    current_page = 1
    if page:
        current_page = page
    if current_page > 1:
        prev_page_url = current_page - 1  
    # Задаем пагинатор
    list_station_paginator = Paginator(list_station, len(list_station))
    list_station_paginator.per_page = 5

    return render(request, 'index.html', context={
        'bus_stations': list_station_paginator.get_page(current_page),
        'current_page': current_page,
        'prev_page_url': current_page - 1,
        'next_page_url': current_page + 1,
    })



