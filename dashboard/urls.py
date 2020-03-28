from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cases-table/', views.cases_table, name='cases-table'),
    path('total-table/', views.total_table, name='total-table'),
]
