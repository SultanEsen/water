from django.shortcuts import render, HttpResponse
from django.views import View
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


class MyView(View):
    # def some_method_view(self):
    #     return HttpResponse('Hello, world')
    def get(self, request):
        return render(request, "about.html")



