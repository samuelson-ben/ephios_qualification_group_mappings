from django.urls import path
from .views import QualificationsToGroupsListView

app_name = "ephios_qualifications_to_user_groups"

urlpatterns = [
    path(
        "settings/qualifications-to-groups/",
        QualificationsToGroupsListView.as_view(),
        name="qualifications_to_groups_list",
    ),
]
