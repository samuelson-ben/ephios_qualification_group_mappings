from django.db import models
from django.contrib.auth.models import Group
from ephios.core.models import Qualification
from django.utils.translation import gettext_lazy as _

class QualificationGroupMapping(models.Model):
    qualification = models.ForeignKey(
        Qualification,
        on_delete=models.CASCADE,
        related_name="qualification_group_mappings",
        verbose_name=_("Qualification"),
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="qualification_group_mappings",
        verbose_name=_("User Group"),
    )

    def __str__(self):
        return f"{self.qualification.title} -> {self.group.name}"
