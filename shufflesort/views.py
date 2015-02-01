from django.shortcuts import get_object_or_404, render

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    context = {'question_list': question_list}
    return render(request, 'shufflesort/index.html', context)


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'shufflesort/question.html', context)


def identify(request):
    return render(request, 'shufflesort/identify.html')
