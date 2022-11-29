from rest_framework import serializers

from yard_capacity.models import Yard,Testyard, File

class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testyard
        fields = ["id", "sbdv_name", "trk_sys_nbr", "dist", "car_capacity"]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"