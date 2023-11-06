from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_page(request):
    return HttpResponse('Hello word!!!!!ol')

