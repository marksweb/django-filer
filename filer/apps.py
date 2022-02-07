from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FilerConfig(AppConfig):
    name = 'filer'
    verbose_name = _("Filer")
    default_auto_field = 'django.db.models.AutoField'
