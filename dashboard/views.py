from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from item.models import Category, Item


class DashboardView(LoginRequiredMixin, TemplateView):
    model = Item
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(created_by=self.request.user)
        return context
