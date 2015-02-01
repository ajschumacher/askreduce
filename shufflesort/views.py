from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from shufflesort.models import Question


def index(request):
    question_list = Question.objects.order_by('date')
    context = {'question_list': question_list}
    return render(request, 'shufflesort/index.html', context)


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'shufflesort/question.html', context)


class IdentityView(View):
    def get(self, request):
        print(request.session.get('user', 'nada'))
        return render(request, 'shufflesort/identity.html')

    def post(self, request):
        if 'user' in request.POST:
            print(request.POST['user'])
            request.session['user'] = request.POST['user']
        if 'deidentify' in request.POST:
            request.session.flush()
        return HttpResponseRedirect(reverse('shufflesort:identity'))
