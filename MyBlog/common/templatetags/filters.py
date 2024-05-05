from django import template
from django.template import Template, Context
from django.utils.html import strip_tags


register = template.Library()

@register.filter(name = 'addclass')
def addclass(value,token):
    value.field.widget.attrs['class'] = token
    return value


@register.filter(name = 'placeholder')
def placeholder(value,token):
    value.field.widget.attrs['placeholder'] = token
    return value
