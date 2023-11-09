from django.contrib import admin
from .models import Menu

class ChildMenuInline(admin.TabularInline):
    model = Menu
    extra = 3

class ParentMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'menu_url', 'time_create', 'time_update')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'menu_url')
    list_filter = ('time_create', 'time_update')
    inlines = [ChildMenuInline]

admin.site.register(Menu, ParentMenuAdmin)