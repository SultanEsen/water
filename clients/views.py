from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from .forms import OrderForm, ClientForm

from .models import Client, Order
# from clients.models import Client


# def clients_list(request):
#     context = {}
#     # # SELECT * FROM Bottle
#     # clients_list_ = Client.objects.all()
#     # context['clients_list'] = clients_list_
#     # html_page = render(request, 'client_list.html', context)
#     # return html_page
#     context['clients_list'] = Client.objects.all()
#     return render(request, 'client_list.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

# def client_details(request, id):
#     try:
#         client = Client.objects.get(id=id)
#         context = {
#             "client": Client.objects.get(id=id)
#         }  # SELECT * FROM Client WHERE id=id;
#         return render(request, 'client_info.html', context)
#     except Client.DoesNotExist:
#         return HttpResponse('Not found')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_info.html'


def client_update(request, id):
    context = {}
    client_object = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client_object)
        if form.is_valid():
            client_object = form.save()
        if form.is_valid():
            client_object = form.save()
    context["form"] = ClientForm(instance=client_object)
    return render(request, 'client_update.html', context)


# def create_order(request):
#     if request.method == 'POST':
#         data = request.POST
#         print(data)
#         order = Order()
#         order.name = data['name']
#         order.contacts = data['contacts']
#         order.description = data['description']
#         order.save()
#         return HttpResponse('<h1>Форма обработана</h1>')
#     return render(request, 'core/order_form.html')

# class CreateOrderView(View):
#     def post(self, request):
#         data = request.POST
#         order = Order()
#         order.name = data['name']
#         order.contacts = data['contacts']
#         order.description = data['description']
#         order.save()
#         return HttpResponse('<h1>Форма обработана</h1>')
#
#     def get(self, request):
#         return render(request, 'core/order_form.html')



# def order_djangoform(request):
#     context = {}
#     if request.method == "POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             order_form.save()
#             return HttpResponse("Форма обработана")
#         return HttpResponse("Данные не валидны")
#
#     context["order_form"] = OrderForm()
#     return render(request, 'order_djangoform.html', context)


class CreateOrderDjangoFormView(CreateView):
    model = Order
    template_name = 'order_djangoform.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/orders/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_text'] = "Fill the windows"
        return context


# def orders_list(request):
#     context = {}
    # # SELECT * FROM Bottle
    # clients_list_ = Client.objects.all()
    # context['clients_list'] = clients_list_
    # html_page = render(request, 'client_list.html', context)
    # return html_page
    # context['orders_list'] = Order.objects.all()
    # return render(request, 'order_list.html', {'orders_list': Order.objects.all()})


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


# def order_details(request, id):
#     # context = {
#     #     "order": Order.objects.get(id=id)
#     # }  # SELECT * FROM Client WHERE id=id;
#     try:
#         return render(
#             request,
#             'order_info.html',
#             {'order_object': Order.objects.get(id=id)}
#         )
#     except Order.DoesNotExist:
#         return HttpResponse('Not found')
#

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_info.html'

def order_update(request, id):
    context = {}
    order_object = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order_object)
        if form.is_valid():
            order_object = form.save()
        if form.is_valid():
            order_object = form.save()
    context["form"] = OrderForm(instance=order_object)
    return render(request, 'order_update.html', context)


class ClientOrderList(ListView):
    model = Order
    template_name = 'order_list.html'
