from django.shortcuts import render, HttpResponse

from .models import Client
# from clients.models import Client


def clients_list(request):
    context = {}
    # SELECT * FROM Bottle
    clients_list_ = Client.objects.all()
    context['clients_list'] = clients_list_
    html_page = render(request, 'clients.html', context)
    return html_page

# def clients_list(request):
#     response = HttpResponse('<h1>test text</h1>')
#     return response
