from django import template
from newapp.models import Medecin  # or Medecin if different

register = template.Library()

@register.simple_tag
def total_medecin():
    return Medecin.objects.count()

@register.simple_tag
def total_medecins_dep():
    return Medecin.objects.filter(department="Dentiste").count()