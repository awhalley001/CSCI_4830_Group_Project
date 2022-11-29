from rest_framework import serializers

from yard_capacity.models import Yard,Testyard, File

out_file = "~/CSCI_4830_Group_Project/scripts/out_cars.csv"

def handle_uploaded_file(f):
    with open(out_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testyard
        fields = ["id", "sbdv_name", "trk_sys_nbr", "dist", "car_capacity"]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"