from django import template
from django.utils import translation

register = template.Library()


@register.filter
def strip_language(value):
    return value.replace('/' + translation.get_language() + '/', '')


@register.filter
def change_type(value):
    return int(value)


@register.filter
def get_zero_or_none(request):
    if request.GET.get('type') == None:
        return 0
