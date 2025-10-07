from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from ephios.core.models import UserProfile
from .forms import BirthdateForm

class QualificationsToGroupsListView(LoginRequiredMixin, FormView):
    template_name = "ephios_qualifications_to_user_groups/qualifications_to_groups_list.html"
    """
    form_class = BirthdateForm
    success_url = reverse_lazy("core:settings_personal_data")

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.date_of_birth:
            initial["birthdate"] = self.request.user.date_of_birth
        return initial

    def dispatch(self, request, *args, **kwargs):
        if request.user.date_of_birth:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    """

"""
class BirthdateSettingsView(LoginRequiredMixin, FormView):
    template_name = "ephios_qualifications_to_user_groups/birthdate_form.html"
    form_class = BirthdateForm
    success_url = reverse_lazy("core:settings_personal_data")

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.date_of_birth:
            initial["birthdate"] = self.request.user.date_of_birth
        return initial
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.date_of_birth:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        profile = self.request.user
        profile.date_of_birth = form.cleaned_data["birthdate"]
        profile.save()
        return super().form_valid(form)
"""