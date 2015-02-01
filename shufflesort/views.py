from django.http import HttpResponse
from django.shortcuts import render

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    context = {'question_list': question_list}
    return render(request, 'shufflesort/index.html', context)


def question(request, question_id):
    return HttpResponse("This is question %s." % question_id)
