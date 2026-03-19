from rest_framework import serializers
from .models import Ride

class RideSerializers(serializers.ModelSerializer):
    class Meta:
        model =Ride
        fields='__all__'
        read_only= ['rider','driver','status']
        