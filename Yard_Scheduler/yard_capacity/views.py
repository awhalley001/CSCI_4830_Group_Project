import sys
import os

from pathlib import Path

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status, parsers, viewsets
from rest_framework.views import APIView

from yard_capacity.forms import DocumentForm

from yard_capacity.models import Yard, Car, Testyard, Posts
from yard_capacity.serializer import YardSerializer, FileSerializer, \
    PostSerializer
from yard_capacity.utils import MultipartJsonParser, DbClass, \
    handle_uploaded_file

from subprocess import run


# db = DbClass()

#  index view
def index(response, id):
    db = DbClass()
    ls = db.providetrackstable()
    db.close()
    return render(response, "yard.html", {"ls": ls})


#  home view
def home(response):
    if response.method == 'POST':
        form = DocumentForm(response.POST, response.FILES)
        if form.is_valid():
            handle_uploaded_file(response.FILES['file'])
            #  path to scripts
            script_dir = '/home/ubuntu/CSCI_4830_Group_Project/scripts'
            out = run([sys.executable,
                       script_dir + '/hump_operation_backup_again.py'])
            return HttpResponseRedirect('/yard_capacity/create/')
    else:
        form = DocumentForm()
    return render(response, 'home.html', {'form': form})


# car table html
def create(response):
    db = DbClass()
    ls = db.providecarstable()
    db.close()
    return render(response, "create.html", {"ls": ls})


#  yard table html
def yard(response):
    db = DbClass()
    ls = db.providetrackstable()
    db.close()
    return render(response, "yard.html", {"ls": ls})

# render api
def yard_tracks(request):
    data = {'yard': Testyard.objects.all()}
    print(data)
    return render(request, 'yard_tracks.html', data)

# post API data
@api_view(["GET"])
def list_tracks_api(request):
    yard_tracks = Testyard.objects.all()
    serializer = YardSerializer(yard_tracks, many=True)
    content = serializer.data

    return Response(content)

#  upload file view angular
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

#  Post api view angular
class PostsViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    parser_classes = (MultipartJsonParser, parsers.JSONParser)
    queryset = Posts.objects.all()
    lookup_field = 'id'
