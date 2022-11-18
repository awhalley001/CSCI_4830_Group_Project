from rest_framework import serializers

from yard_capacity.models import Yard

class YardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yard
        fields = ["id", "SBDV_NAME", "TRK_SYS_NBR", "dist", "car_capacity"]