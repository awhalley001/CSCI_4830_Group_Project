from rest_framework import serializers

from yard_capacity.models import Yard, Testyard, File, Posts


#  serialize yard data
class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testyard
        fields = ["id", "sbdv_name", "trk_sys_nbr", "dist", "car_capacity"]


#  serialze car data from file
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "EQUIPMENT_INITIAL", "EQUIPMENT_NUMBER",
                  "CURRENT_YARD_CIRC7", "CURRENT_TRAIN_DATE", "DEST_TRACK"]


# post serialized data
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["id", "EQUIPMENT_INITIAL", "EQUIPMENT_NUMBER",
                  "CURRENT_YARD_CIRC7", "CURRENT_TRAIN_DATE", "DEST_TRACK"]
