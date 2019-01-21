from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count
from django.views import generic

from .models import Question, Choice

#
# def index(request):
#     name = 'Sam'
#     surname = 'Zukkerberg'
#     questions = Question.objects.annotate(num_choices=Count('choice')).filter(num_choices__gt=0)
#     return render(request, 'polls/index.html', locals())
#
#
# def details(request, id):
#     question = get_object_or_404(Question, id=id)
#     # question = Question.objects.get(id=id)
#     return render(request, 'polls/details.html', locals())
#
#
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': 'Your didn\'t select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('polls:results', args=(question_id,)))

#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', locals())


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
