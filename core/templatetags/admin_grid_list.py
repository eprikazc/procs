from django import template


register = template.Library()


@register.simple_tag
def url_for_result(cl, item):
    return cl.url_for_result(item)
