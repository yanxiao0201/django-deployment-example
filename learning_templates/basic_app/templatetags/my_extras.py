from django import template

register = template.Library()

@register.filter(name='cutt')
def cut(value, arg):

    return value.replace(arg, '')


# register.filter('cutt', cut)
