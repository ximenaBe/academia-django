# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.template import RequestContext

from academico.models import *
import json


def index(request):
    
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario, 
        context_instance=RequestContext(request))
