from django.shortcuts import render
from demomenu.models import Menu


def recursive_menu(request):
    current_url = request.path
    parent_menu = Menu.objects.filter(parent__isnull=True)
    context = {
        'current_url': current_url,
        'parent_menu': parent_menu,
    }
    return render(request, 'demomenu/base.html', context)