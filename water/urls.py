"""water URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from core.views import *
from clients.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('about/', about),
    path('', makers_list),
    path('clients/', ClientListView.as_view(), name="client-list"),
    path('our_history', our_history),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client-details"),
    path('client/<int:id>/order-list/', ClientOrderList.as_view(), name='client-order-list'),
    path('client/update/<int:id>/', client_update, name="client-update"),
    # path('order/create/', CreateOrderView.as_view(), name='create-order'),
    path('order/djangoform/', CreateOrderDjangoFormView.as_view(), name='order-django-form'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order-details"),
    path('order/update/<int:id>/', order_update, name="order-update"),
    path('test/', MyView.as_view()),
    path('singin/', LoginView.as_view(), name='sign-in')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)