from django.http import HttpResponse
from django.template import RequestContext, loader

# not using
# from django.shortcuts import render

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    template = loader.get_template('shufflesort/index.html')
    context = RequestContext(request, {
        'question_list': question_list,
    })
    return HttpResponse(template.render(context))


def question(request, question_id):
    return HttpResponse("This is question %s." % question_id)
