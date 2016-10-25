from django.shortcuts import render
from django.http import HttpResponse
import json
import logging

logger = logging.getLogger('webhook')

def index(request):
    if request.POST:
        payload = request.POST.get('payload')
        logger.debug(payload)
        return HttpResponse('ok')
    else:
        return HttpResponse("hello, world!")
