from django.http import HttpResponse

# not using
# from django.shortcuts import render


def index(request):
    return HttpResponse("Hello `shufflesort` index.")
