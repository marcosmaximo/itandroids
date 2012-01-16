# -*- coding: utf-8 -*-

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from cms.models import Page
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Category(CMSPlugin):
	title = models.CharField(_("Title"), max_length=100, unique=True)
	title_en = models.CharField(_("Title (English)"), max_length=100, unique=True)
	description = models.TextField(_("Description"))
	description_en = models.TextField(_("Description (English)"))
	image = ImageWithThumbsField(_("Image"), upload_to="uploads/images/category", sizes=((640, 480),))
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

class RelationshipWithITA(models.Model):
	title = models.CharField(_("Title"), max_length=100)
	title_en = models.CharField(_("Title (English)"), max_length=100)
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _("Relationship with ITA")
		verbose_name_plural = _("Relationships with ITA")

class SpecialRole(models.Model):
	title = models.CharField(_("Title"), max_length=100)
	title_en = models.CharField(_("Title (English)"), max_length=100)
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = _("Special Role in ITAndroids")
		verbose_name_plural = _("Special Roles in ITAndroids")

class Member(CMSPlugin):
	name = models.CharField(_("Name"), max_length=100, unique=True)
	lattes = models.URLField(blank=True, help_text=_("Optional field (you may leave it blank)."))
	relationship_with_ita = models.ForeignKey(RelationshipWithITA, verbose_name=_("Relationship with ITA"), null=True, blank=True)
	special_roles = models.ManyToManyField(SpecialRole, verbose_name=_("Special Roles in ITAndroids"), null=True, blank=True, help_text=_("Optional field (you may leave it blank)."))
	categories = models.ManyToManyField(Category, verbose_name=_("Categories"), through='MemberCategoryAssociation', null=True, blank=True)
	entry_date = models.DateField(_("Entry Date"), help_text=_("This date field will be displayed as \"mm yyyy\", so only month and year are relevant."))
	leave_date = models.DateField(_("Leave Date"), null=True, blank=True, help_text=_("This date field will be displayed as \"mm yyyy\", so only month and year are relevant. This field is optional (you may leave it blank)."))
	description = models.TextField(_("Description"))
	description_en = models.TextField(_("Description (English)"))
	photo = ImageWithThumbsField(_("Photo"), upload_to="uploads/images/member/", sizes=((100, 100),), help_text=_("Resolution in page will be 100x100 (1:1 aspect ratio). Please, upload an image with resolution as near as possible to 100x100."))

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Member")
		verbose_name_plural = _("Members")

MEMBER = 0
LEADER = 1
ADVISOR = 2
EX_MEMBER = 3
EX_ADVISOR = 4

CATEGORY_ROLE_CHOICES = (
	(MEMBER, _("Member")),
	(LEADER, _("Leader")),
	(ADVISOR, _("Advisor")),
	(EX_MEMBER, _("Ex-member")),
	(EX_ADVISOR, _("Ex-advisor")),
)

# Acochambração
CATEGORY_ROLES_STR = [
	_("Member"),
	_("Leader"),
	_("Advisor"),
	_("Ex-member"),
	_("Ex-advisor")
]

class MemberCategoryAssociation(models.Model):
	role = models.IntegerField(_("Role"), choices=CATEGORY_ROLE_CHOICES)
	member = models.ForeignKey(Member, verbose_name=_("Member"))
	category = models.ForeignKey(Category, verbose_name=_("Category"))
	
	def __unicode__(self):
		return "%s %s %s" % (CATEGORY_ROLES_STR[self.role], _("of category"), self.category.title)

	class Meta:
		verbose_name = _("Member-Category Association")
		verbose_name_plural = _("Member-Category Associations")

class News(CMSPlugin):
	date_created = models.DateTimeField(_("Date Created"), default=(lambda:datetime.now()))
	last_modified = models.DateTimeField(_("Last Modified"), default=(lambda:datetime.now()))
	title = models.CharField(_("Title"), max_length=100)
	title_en = models.CharField(_("Title (English)"), max_length=100)
	page = models.ForeignKey(Page)
	author = models.ForeignKey(User, verbose_name=_("Author"))
	image = ImageWithThumbsField(_("Image"), upload_to="uploads/images/news/", sizes=((320, 240),), help_text=_("Resolution in page will be 320x240 (4:3 aspect ratio). Please, upload an image with resolution as near as possible to 320x240."))

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _("News")
		verbose_name_plural = _("News (plural)")

class Sponsor(CMSPlugin):
	name = models.CharField(_("Name"), max_length=100, unique=True)
	url = models.URLField()
	image = ImageWithThumbsField(_("Image"), upload_to="uploads/images/sponsor/", help_text=_("Image in page will be 200 pixels wide (original aspect ratio will be maintained)."))
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Sponsor")
		verbose_name_plural = _("Sponsors")
		
class Supporter(CMSPlugin):
	name = models.CharField(_("Name"), max_length=100, unique=True)
	url = models.URLField()
	image = ImageWithThumbsField(_("Image"), upload_to="uploads/images/supporter/", help_text=_("Image in page will be 200 pixels wide (original aspect ratio will be maintained)."))
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Supporter")
		verbose_name_plural = _("Supporters")
		
class Event(CMSPlugin):
	name = models.CharField(_("Name"), max_length=100)
	url = models.URLField()
	image = ImageWithThumbsField(_("Image"), upload_to="uploads/images/supporter/", help_text=_("Image in page will be 200 pixels wide (original aspect ratio will be maintained)."))
	start_date = models.DateField(_("Start Date"))
	end_date = models.DateField(_("End Date"))
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _("Event")
		verbose_name_plural = _("Events")
		
class TimelineEntry(CMSPlugin):
	title = models.CharField(_("Title"), max_length=100)
	title_en = models.CharField(_("Title (English)"), max_length=100)
	description = models.TextField(_("Description"), max_length=1000)
	description_en = models.TextField(_("Description (English)"), max_length=1000)
	year = models.IntegerField(_("Year"))
	left_image = ImageWithThumbsField(_("Left Image"), upload_to="uploads/images/timeline_entry/")
	right_image = ImageWithThumbsField(_("Right Image"), upload_to="uploads/images/timeline_entry/")
	
	def __unicode__(self):
		return self.title
	
	class Meta:
		verbose_name = _("Timeline Entry")
		verbose_name_plural = _("Timeline Entries")
