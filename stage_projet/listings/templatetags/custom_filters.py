
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Filtre pour accéder aux éléments d'un dictionnaire"""
    return dictionary.get(key)
