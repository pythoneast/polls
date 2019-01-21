from django.shortcuts import render, get_object_or_404
from polls.models import Question


def main_page_view(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, 'index.html', locals())
