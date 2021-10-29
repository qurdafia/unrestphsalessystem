from salesinventory.mainapp.views import order_detail, order_list
from django.urls import path
from mainapp import views

urlpatterns = [
    path('items/', views.item_list),
    path('items/<int:pk>/', views.item_detail),
    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_detail),
    path('expenses/', views.expense_list),
    path('expenses/<int:pk>/', views.expense_detail)
]