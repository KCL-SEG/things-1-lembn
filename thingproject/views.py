from django import http
from django.shortcuts import render


def home(req: http.HttpRequest) -> http.HttpResponse:
    return render(req, "thing.html")
