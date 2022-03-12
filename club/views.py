
from rest_framework import generics

from club.models import Dancer
from dancefloor.serializers import DancerSerializer


class DancerList(generics.ListCreateAPIView):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer


class DancerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer
