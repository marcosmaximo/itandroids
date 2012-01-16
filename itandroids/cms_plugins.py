from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from models import Category, News, Member, Sponsor, Supporter, Event,\
	TimelineEntry

class CategoryPlugin(CMSPluginBase):
	model = CMSPlugin
	name = _("Category Plugin")
	render_template = "plugins/category_plugin.html"
	module = '[ITAndroids]'
	
	def render(self, context, instance, placeholder):
		context['category_list'] = Category.objects.all()
		return context

class LastestNews(CMSPluginBase):
	model = CMSPlugin
	name = _("Latest News Plugin")
	render_template = "plugins/lastest_news_plugin.html"
	module = '[ITAndroids]'
	
	def render(self, context, instance, placeholder):
		context['news_list'] = News.objects.order_by('-pub_date')[:3]
		return context

class OldNewsPlugin(CMSPluginBase):
	model = CMSPlugin
	name = _("Old News Plugin")
	render_template = "plugins/old_news_plugin.html"
	module = '[ITAndroids]'
	
	def render(self, context, instance, placeholder):
		context['news_list'] = News.objects.order_by('-pub_date')
		return context

class MemberPlugin(CMSPluginBase):
	model = CMSPlugin
	name = _("Member Plugin")
	render_template = "plugins/member_plugin.html"
	module = '[ITAndroids]'
	
	def render(self, context, instance, placeholder):
		KEY_MEMBERS = _("Members")
		KEY_EX_MEMBERS = _("Ex-members")
		
		member_list = Member.objects.filter(leave_date__isnull=True).order_by('name')
		ex_member_list = Member.objects.filter(leave_date__isnull=False).order_by('name')
		context['keys_ordering'] = [ KEY_MEMBERS, KEY_EX_MEMBERS ]
		context['member_dict'] = { KEY_MEMBERS: member_list, KEY_EX_MEMBERS: ex_member_list }
		
		return context

class TimelinePlugin(CMSPluginBase):
	model = CMSPlugin
	name = _("Timeline Plugin")
	render_template = "plugins/timeline_plugin.html"
	module = '[ITAndroids]'
	
	def render(self, context, instance, placeholder):		
		context['timeline'] = TimelineEntry.objects.all().order_by('-year')
		return context
		
plugin_pool.register_plugin(CategoryPlugin)
plugin_pool.register_plugin(LastestNews)
plugin_pool.register_plugin(OldNewsPlugin)
plugin_pool.register_plugin(MemberPlugin)
plugin_pool.register_plugin(TimelinePlugin)