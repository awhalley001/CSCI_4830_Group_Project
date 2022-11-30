from pathlib import Path

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status, parsers,viewsets
from rest_framework.views import APIView

from yard_capacity.models import Yard, Car, Testyard, Posts
from yard_capacity.serializer import YardSerializer, FileSerializer, PostSerializer
from yard_capacity.utils import MultipartJsonParser


@api_view(["GET"])
def list_tracks_api(request):
    yard_tracks = Testyard.objects.all()
    serializer = YardSerializer(yard_tracks, many=True)
    content = serializer.data
    
    print(content)
    return Response(content)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)
      print(file_serializer)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    parser_classes = (MultipartJsonParser, parsers.JSONParser)
    queryset = Posts.objects.all()
    lookup_field = 'id'
