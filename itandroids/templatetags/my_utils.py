# -*- coding: utf-8 -*-

# Classe com templatetags utilitárias genéricas

from django import template
from itandroids.models import MemberCategoryAssociation, Member

register = template.Library()

def get_member_category_associations(value):
    associations = MemberCategoryAssociation.objects.filter(member=value)
    return associations

register.filter('get_member_category_associations', get_member_category_associations)
