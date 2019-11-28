from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import ListView

from contest_app.models import Contest


class IndexView(ListView):
    template_name = 'contest_app/index.html'
    context_object_name = 'latest_contest_list'

    def get_queryset(self):
        return Contest.objects.filter(start_date__lte=timezone.now()).order_by('-start_date')