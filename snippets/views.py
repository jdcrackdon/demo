import urllib
import time

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.utils import simplejson
from django.http import HttpResponse

#@api_view(['GET', 'POST'])
def snippets_response(request, format=None):

    some_data_to_dump = {
        'Time': "Current date & time " + time.strftime("%c"),
    }

    data = simplejson.dumps(some_data_to_dump)

    if request.method == 'GET':

        #Download file, cool!
        if request.GET.get('file'):
            filename = request.GET['file']
            testfile =urllib.URLopener()
            filel = testfile.retrieve(filename,"video.mp4")

        return HttpResponse(data, mimetype='application/json')

    elif request.method == 'POST':

    	if request.POST.get('file'):
            filename = request.POST['file']
            testfile =urllib.URLopener()
            filel = testfile.retrieve(filename,"video.mp4")
        
        return HttpResponse(data, mimetype='application/json')


