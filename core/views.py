from rest_framework import viewsets
from .models import Ride
from .serializers import RideSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


class Rideviewset(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class =RideSerializers

    def perform_create(self, serializer):
        user = User.objects.first()
        serializer.save(rider=user,status='requested')

    @action(methods=['POST'],detail=True)
    def accept_driver(self,request,pk=None):
        ride=self.get_object()
        driver= User.objects.last()
        ride.driver =driver
        ride.status= "accepted"
        ride.save()

        return Response({
            "message":"Ride accepted","rider_id":ride.id,"status":ride.status},status=200)
    

    @action (methods=["PATCH"],detail=True)
    def change_status(self,request,pk=None):
        ride= self.get_object()
        status=request.data.get('status')

        if status not in dict(Ride.STATUS_CHOICES):
            return Response({"error":"invalid status"},status=400)
        
        ride.status =status
        ride.save()
        return Response({"status":ride.status},status=200)
        



