from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(views.recursive_menu), name='all_menu'),
]