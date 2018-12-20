from django.http import HttpResponse
from django.views import generic
from .models import Menu


class DetailView(generic.ListView):
    model = Menu
    template_name = 'menu/detail.html'
    context_object_name = 'all_menu'

    def get_queryset(self):
        return Menu.objects.all()


class IndexView(generic.ListView):
    template_name = 'menu/index.html'

    def get_queryset(self):
        return HttpResponse("Welcome Smith")
