from django.urls import path
from .import views


app_name = 'menu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # cafeteria/menu/
    path('menu/', views.DetailView.as_view(), name='detail'),


]
