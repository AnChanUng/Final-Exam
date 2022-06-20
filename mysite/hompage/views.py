from django.http.response import HttpResponse
from django.shortcuts import render

def 홈페이지(request):
    return render(request, 'folder/introduce.html')
