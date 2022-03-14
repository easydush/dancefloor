from rest_framework import generics
from rest_framework.response import Response

from club.models import Dancer, Dance
from dancefloor.serializers import DancerSerializer, DancerWithActionSerializer, DanceSerializer


class DancerList(generics.ListCreateAPIView):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer

    def get(self, request):
        """
        Dancers
        ___
        list:
        omit_parameters:
            - style
        """
        queryset = self.get_queryset()
        serializer = DancerWithActionSerializer(queryset, many=True,
                                                context=request.query_params.get('style', None))
        return Response(serializer.data)


class DancerDetail(generics.RetrieveDestroyAPIView):
    queryset = Dancer.objects.all()
    serializer_class = DancerSerializer


class DanceList(generics.ListCreateAPIView):
    queryset = Dance.objects.all()
    serializer_class = DanceSerializer
