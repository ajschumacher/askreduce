import functools
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from shufflesort.models import Question, Answer


def with_identity(func):
    @functools.wraps(func)
    def newfunc(self, request, **kwargs):
        request.session['target'] = request.path
        if 'user' in request.session:
            return func(self, request, **kwargs)
        else:
            return HttpResponseRedirect(reverse('shufflesort:identity'))
    return newfunc


class IndexView(View):
    @with_identity
    def get(self, request):
        question_list = Question.objects.order_by('date')
        context = {'question_list': question_list}
        return render(request, 'shufflesort/index.html', context)


class QuestionView(View):
    @with_identity
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        context = {'question': question}
        return render(request, 'shufflesort/question.html', context)

    @with_identity
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        if 'text' in request.POST:
            answer = Answer(question=question,
                            text=request.POST['text'],
                            user=request.session['user'],
                            date=timezone.now())
            answer.save()
        return HttpResponseRedirect(reverse('shufflesort:question',
                                            args=(question_id,)))


class IdentityView(View):
    def get(self, request):
        return render(request, 'shufflesort/identity.html')

    def post(self, request):
        if 'user' in request.POST:
            request.session['user'] = request.POST['user']
        if 'deidentify' in request.POST and 'user' in request.session:
            del request.session['user']
        if 'target' in request.session:
            target = request.session['target']
            del request.session['target']
            return HttpResponseRedirect(target)
        return HttpResponseRedirect(reverse('shufflesort:identity'))
