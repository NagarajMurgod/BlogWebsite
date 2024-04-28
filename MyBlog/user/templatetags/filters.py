from django import template
from django.template import Template, Context
from django.utils.html import strip_tags


register = template.Library()

# @register.filter
# def lowercase(value):
#     # template = Template(value)

#     # rendered_html = template.render(Context())

#     # text = strip_tags(rendered_html)
#     # print(text)
#     # return text