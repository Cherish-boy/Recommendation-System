from django.urls import path

from tuijian import views

urlpatterns = [
    path('orders/', views.listorders),
    path('company/', views.listcompany),
]