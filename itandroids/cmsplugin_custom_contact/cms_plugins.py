from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from cmsplugin_contact.cms_plugins import ContactPlugin
from models import CustomContact
from forms import CustomContactForm

class CustomContactPlugin(ContactPlugin):
    name = _("Custom Contact Form")
    
    model = CustomContact
    contact_form = CustomContactForm
    
    # We're using the original cmsplugin_contact templates here which
    # works fine but requires that the original plugin is in INSTALLED_APPS.
    render_template = "cmsplugin_contact/contact.html"
    email_template = "cmsplugin_contact/email.txt"
    
    fieldsets = (
        (None, {
                'fields': ('site_email', 'email_label', 'custom_label',
                           'subject_label', 'content_label', 'thanks',
                           'submit'),
        }),
        (_('Spam Protection'), {
                'fields': ('spam_protection_method', 'akismet_api_key',
                           'recaptcha_public_key', 'recaptcha_private_key',
                           'recaptcha_theme')
        })
    )

plugin_pool.register_plugin(CustomContactPlugin)
