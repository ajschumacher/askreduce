from django.http import HttpResponse

# not using
# from django.shortcuts import render

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    output = '\n'.join(['<p>'+q.text+'</p>' for q in question_list])
    return HttpResponse(output)


def question(request, question_id):
    return HttpResponse("This is question %s." % question_id)
