from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.views.generic import ListView
from .models import Bet
from itertools import chain
from operator import attrgetter
from django.db.models import Sum


def index(request):
    latest_team_list = Bet.objects.order_by('-pub_date')[:6]
    context = {'latest_team_list': latest_team_list}
    return render(request, 'picks/index.html', context)


class IndexView(ListView):
    model = Bet
    template_name = 'picks/index.html'
    context_object_name = 'latest_team_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sum_result'] = Bet.objects.all().aggregate(sum_all=Sum('result')).get('sum_all')
        return context

    def get_context_data1(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['count_picks'] = Bet.objects.all().aggregate(count_all=Sum('line_text')).get('count_all')
        return context
