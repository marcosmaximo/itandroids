# -*- coding: utf-8 -*-

# Para facilitar a construção das barras laterais (sidebars) da Home.

from django import template
from itandroids.models import Sponsor, Supporter, Event
from datetime import datetime

register = template.Library()

def leftbar():
	sponsor_list = Sponsor.objects.all()
	supporter_list = Supporter.objects.all()
	return {
		'sponsor_list': sponsor_list,
		'supporter_list': supporter_list,
	}
	
def rightbar():
	next_events = Event.objects.filter(end_date__gte=datetime.now())
	return {
		'event_list': next_events,
	}

register.inclusion_tag('leftbar.html')(leftbar)
register.inclusion_tag('rightbar.html')(rightbar)
