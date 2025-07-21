# image_tags.py
from django import template

register = template.Library()

@register.filter
def webp_url(image_url):
    return image_url.rsplit('.', 1)[0] + '.webp' if image_url else ''

@register.filter
def avif_url(image_url):
    return image_url.rsplit('.', 1)[0] + '.avif' if image_url else ''
