from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
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


class VoteView(DetailView):
    model = Contest
    context_object_name = 'votes'
    template_name = 'contest_app/vote.html'

    def get_all_votes(self):
        return Vote.objects.filter(stage__contest=self.object.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"votes": self.get_all_votes()})
        return context


def vote(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)

    # TODO: Dodać Form i validator
    try:
        points = int(request.POST['points'])
    except KeyError as e:
        messages.add_message(request, messages.ERROR, 'Problem with finding points')
        return HttpResponseRedirect(reverse(f'contest:vote', args=(vote.stage.contest.pk,)))
    except TypeError as e:
        messages.add_message(request, messages.ERROR, 'Point cant be casted to int')
        return HttpResponseRedirect(reverse(f'contest:vote', args=(vote.stage.contest.pk,)))

    if vote.points != 0:
        messages.add_message(request, messages.ERROR, 'Vote already submitted')
        return HttpResponseRedirect(reverse(f'contest:vote', args=(vote.stage.contest.pk,)))
    if points < 0:
        messages.add_message(request, messages.ERROR, 'Vote cant be negative')
        return HttpResponseRedirect(reverse(f'contest:vote', args=(vote.stage.contest.pk,)))

    vote.points = points
    vote.save()
    messages.add_message(request, messages.INFO, 'Vote processed')

    return HttpResponseRedirect(reverse(f'contest:vote', args=(vote.stage.contest.pk,)))
