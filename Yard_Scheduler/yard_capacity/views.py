from pathlib import Path

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from yard_capacity.models import Yard, Car
from yard_capacity.serializer import YardSerializer


@api_view(["GET"])
def list_tracks_api(request):
    yard_tracks = Yard.objects.all()
    serializer = YardSerializer(yard_tracks, many=True)
    content = {
        "tracks": serializer.data,
    }

    return Response(content)
