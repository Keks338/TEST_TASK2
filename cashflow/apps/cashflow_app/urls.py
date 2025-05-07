from django.urls import path
from . import views

app_name = "cashflow_app"

urlpatterns = [
    path('', views.cashflow_list_view, name='cashflow_list'),
    path('add/', views.cashflow_create_view, name='cashflow_add'),
    path('edit/<int:pk>/', views.cashflow_update_view, name='cashflow_edit'),
    path('delete/<int:pk>/', views.cashflow_delete_view, name='cashflow_delete'),
    path('directories/', views.directories_manage_view, name='directories_manage'),
]
