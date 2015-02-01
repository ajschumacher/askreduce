from django.http import Http404
from django.shortcuts import render

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    context = {'question_list': question_list}
    return render(request, 'shufflesort/index.html', context)


def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {'question': question}
    return render(request, 'shufflesort/question.html', context)
