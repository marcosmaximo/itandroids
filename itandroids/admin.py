# -*- coding: utf-8 -*-
from models import Category, Member, News, Sponsor, Supporter, Event, SpecialRole, RelationshipWithITA, TimelineEntry
from models import MEMBER, LEADER, ADVISOR, EX_MEMBER, EX_ADVISOR
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class CategoryAdmin(admin.ModelAdmin):
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

class CategoryRoleInline(admin.TabularInline):
	model = Member.categories.through
	extra = 1

class MemberAdmin(admin.ModelAdmin):
	inlines = [
			CategoryRoleInline
	]
	
	def save_model(self, request, obj, form, change):
		# Para manter coerência, se um membro se torna ex-membro
		# (i.e., recebe uma data de saída), ele passa
		# automaticamente a ser "ex" em todas as categorias.
		if obj.leave_date is not None:
			for category_role in obj.categories.all():
				if category_role.role == MEMBER or category_role.role == LEADER:
					category_role.role = EX_MEMBER
				elif category_role.role == ADVISOR:
					category_role.role = EX_ADVISOR
		obj.save()
		
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

class NewsAdmin(admin.ModelAdmin):
	fieldsets = [
				(None, {'fields': ['title', 'title_en', 'page', 'image']}),
				(_("Date Information"), {'fields': ['date_created', 'last_modified'], 'classes': ['collapse']})
	]
	
	def save_model(self, request, obj, form, change):
		if obj.created_by is None:
			obj.created_by = request.user
		obj.modified_by.add(request.user)
		obj.save()

	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
		
class TimelineEntryAdmin(admin.ModelAdmin):
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Sponsor)
admin.site.register(Supporter)
admin.site.register(Event)
admin.site.register(RelationshipWithITA)
admin.site.register(SpecialRole)
admin.site.register(TimelineEntry, TimelineEntryAdmin)