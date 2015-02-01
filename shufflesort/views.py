from django.http import HttpResponse

# not using
# from django.shortcuts import render


def index(request):
    return HttpResponse("Hello `shufflesort` index.")


def question(request, question_id):
    return HttpResponse("This is question %s." % question_id)
