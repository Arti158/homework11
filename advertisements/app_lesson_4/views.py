from django.shortcuts import render
from django.http import HttpResponse


def index(reqeust):
    return HttpResponse("Домашняя работа модуля 4")



