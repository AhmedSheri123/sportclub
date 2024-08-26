from django import template
from django.template.defaultfilters import stringfilter
from accounts.models import UserProfile, ClubsModel
from students.models import ProductsImage, ServicesImage
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
@stringfilter
def get_product_imgs(id):
    imgs = ProductsImage.objects.filter(product__id=id)
    return imgs

@register.simple_tag
@stringfilter
def get_Service_imgs(id):
    imgs = ServicesImage.objects.filter(product__id=id)
    return imgs
