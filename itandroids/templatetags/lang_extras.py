# -*- coding: utf-8 -*-

# Para facilitar o acesso aos campos internacionalizados dos modelos. 
# Solução baseada em: 
# http://stackoverflow.com/questions/3653999/i18n-django-internationalization-and-database-objects

from django import template

register = template.Library()

@register.tag(name="prop_lang")
def do_prop_lang(parser, token):
	try:
		tag_name, obj, prop, lang = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires exactly three arguments" % tag_name)
	return PropertyLangNode(obj, prop, lang)

class PropertyLangNode(template.Node):
	def __init__(self, obj, prop, lang):
		self.obj = template.Variable(obj)
		self.prop = prop
		self.lang = template.Variable(lang)
	
	def render(self, context):
		try:
			obj = self.obj.resolve(context)
			prop = self.prop
			lang = self.lang.resolve(context)		
			if lang=='pt-br':
				return obj.__getattribute__(prop)
			elif lang=='en':
				return obj.__getattribute__("%s_en" % prop)
			else:
				return ''
		except template.VariableDoesNotExist:
					return ''
