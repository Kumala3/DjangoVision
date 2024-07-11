from django.views import View
from django.shortcuts import render
from django.http import HttpRequest


class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, 'index.html')
