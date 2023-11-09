from django import template
from demomenu.models import Menu

register = template.Library()


@register.inclusion_tag('demomenu/menu_tree.html', takes_context=True)
def draw_menu(context, menu_id=None):
    parent_menu = Menu.objects.filter(parent__isnull=True)
    local_context = {
        'parent_menu': parent_menu,
        'menu_id': menu_id,
        'current_url': context.get('current_url', '')
    }
    return local_context


@register.inclusion_tag('demomenu/menu_item.html')
def draw_menu_item_children(menu_item, current_url):
    children_menus = menu_item.children.all()
    is_parent_selected = current_url.startswith(menu_item.menu_url)
    local_context = {
        'children_menus': children_menus,
        'menu_item': menu_item,
        'current_url': current_url,
        'is_parent_selected': is_parent_selected,
    }
    return local_context
