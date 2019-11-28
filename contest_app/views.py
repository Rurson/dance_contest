from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView

from contest_app.models import Contest, Vote


class IndexView(ListView):
    template_name = "contest_app/index.html"
    context_object_name = "latest_contest_list"
    model = Contest


class DetailsView(DetailView):
    template_name = "contest_app/details.html"
    context_object_name = "contest"
    model = Contest

    def get_all_jurys_for_contest(self):
        return self.object.membership_set.filter(member_type="J")

    def get_all_contenders_for_contest(self):
        return self.object.membership_set.filter(member_type="C")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"jurys": self.get_all_jurys_for_contest()})
        context.update({"contenders": self.get_all_contenders_for_contest()})
        return context


class VoteView(ListView):
    model = Vote
    context_object_name = 'votes'
    template_name = 'contest_app/vote.html'
