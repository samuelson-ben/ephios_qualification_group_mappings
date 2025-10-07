from ephios.core.plugins import PluginConfig
from django.utils.translation import gettext_lazy as _

class PluginApp(PluginConfig):
    name = "ephios_qualification_group_mappings"

    class EphiosPluginMeta:
        name = _("Qualififcation Group Mappings")
        author = "Ben Samuelson <ben.samuelson@fiteka.de>"
        description = _("Maps Qualifications to User Groups.")

    def ready(self):
        from . import signals  # NOQA
