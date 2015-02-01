from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
import functools
from django.views.generic import View

from shufflesort.models import Question


def with_identity(func):
    @functools.wraps(func)
    def newfunc(request, **kwargs):
        if 'user' in request.session:
            return func(request, **kwargs)
        else:
            request.session['target'] = request.path
            return HttpResponseRedirect(reverse('shufflesort:identity'))
    return newfunc


@with_identity
def index(request):
    question_list = Question.objects.order_by('date')
    context = {'question_list': question_list}
    return render(request, 'shufflesort/index.html', context)


@with_identity
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
        if 'target' in request.session:
            target = request.session['target']
            del request.session['target']
            return HttpResponseRedirect(target)
        return HttpResponseRedirect(reverse('shufflesort:identity'))
