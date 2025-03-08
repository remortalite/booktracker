from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexPageView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, world!</h1>')
