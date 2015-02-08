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
        answers = question.answer_set.order_by('-date').all()
        answerers = [answer.user for answer in answers]
        answered = request.session['user'] in answerers
        context = {'question': question,
                   'answers': answers,
                   'answered': answered,}
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


class UserView(View):
    @with_identity
    def get(self, request, user_name):
        questions = Question.objects.all()
        # presume questions are ordered by question ID
        questions = [{'question': question,
                      'answers': [],}
                     for question in questions]
        answers = Answer.objects.filter(user=user_name).order_by('-date')
        for answer in answers:
            questions[answer.question_id - 1]['answers'].append(answer)
        context = {'user_name': user_name,
                   'questions': questions,}
        return render(request, 'shufflesort/user.html', context)


class DashboardView(View):
    @with_identity
    def get(self, request):
        questions = Question.objects.all()
        question_ids = [question.id for question in questions]
        answers = Answer.objects.all()
        users = {}
        for answer in answers:
            user = users.setdefault(answer.user, {})
            user[answer.question_id] = answer.text
        user_names = sorted(users.keys())
        users_tups = []
        for user_name in user_names:
            user_row = [None] * len(question_ids)
            for index, question_id in enumerate(question_ids):
                user_row[index] = users[user_name].get(question_id)
            users_tups.append((user_name, user_row))
        context = {'question_ids': question_ids,
                   'users_tups': users_tups,}
        return render(request, 'shufflesort/dashboard.html', context)


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
