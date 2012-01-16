from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _

class CustomContact(BaseContact):
    custom_label = models.TextField(
        _('Instructions'),
        default=_('To contact us, please use the form below.'))
