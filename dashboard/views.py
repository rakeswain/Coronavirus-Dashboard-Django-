from django.shortcuts import render
from . import web_scrapper

from django.template.loader import render_to_string
# Create your views here.

from django.http import JsonResponse, HttpResponse


def home(request):
    total_data, status = web_scrapper.get_data()
    state_data, status = web_scrapper.get_state_data()

    return render(request, "dashboard/__base__.html", {'total_data': total_data, 'state_data': state_data})


def total_table(request):
    total_data, status = web_scrapper.get_data()

    html = render_to_string('dashboard/home.html', {'total_data': total_data})
    return HttpResponse(html)


def cases_table(request):
    state_data, status = web_scrapper.get_state_data()

    data = render_to_string('dashboard/cases_table.html', {'state_data': state_data})

    return HttpResponse(data)
