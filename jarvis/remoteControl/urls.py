from django.urls import path
from . import views

urlpatterns = [
    path('<machine>/order', views.order_return, name='order_return'),
    path('test', views.submit_machine_response, name='machine_response')
]
