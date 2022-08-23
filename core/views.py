from django.shortcuts import render, HttpResponse

from .models import Bottle

def contacts(request):
    return render(request, 'core/contacts.html')


def about(request):
    return render(request, 'about.html')


def makers_list(request):
    context = {}
    # SELECT * FROM Bottle
    bottles_list = Bottle.objects.all()
    context['bottles_list'] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page

def our_history(request):
    return render(request, 'our_history.html')