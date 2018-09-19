from django.urls import path
from . import views

urlpatterns = [
    path('<machine>/order', views.order_return, name='order_return'),
]
