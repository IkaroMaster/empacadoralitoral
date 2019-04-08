from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
@login_required()
def inicio(request):
    return HttpResponse('hello')
    