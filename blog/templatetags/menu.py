from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tutorial_tpl.html')
def menu_tutorials(class_menu):
    categories = Category.objects.all()
    return {"categories": categories, "class_menu": class_menu}