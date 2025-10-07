from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from ephios.core.signals import settings_sections
from ephios.core.views.settings import SETTINGS_MANAGEMENT_SECTION_KEY

@receiver(settings_sections)
def add_navigation_item(sender, request, **kwargs):
    return (
        [
            {
                "label": _("Qualifications to Groups"),
                "url": reverse("ephios_qualifications_to_user_groups:qualifications_to_groups_list"),
                "group": SETTINGS_MANAGEMENT_SECTION_KEY,
                "active": False,
            },
        ]
        if request.user.is_staff or request.user.has_perm("core.change_qualification")
        else []
    )
