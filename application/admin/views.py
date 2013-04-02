# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Main admin view for the Application app
# (c) Twined/Univers 2009-2013. All rights reserved.
# ----------------------------------------------------------------------


from django.views.generic import TemplateView
from ..views import LoginRequiredMixin


class DashboardIndex(LoginRequiredMixin, TemplateView):
    """
    Presents the admin dashboard.
    """
    template_name = 'dashboard/admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardIndex, self).get_context_data(**kwargs)
        return context
