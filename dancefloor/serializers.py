from rest_framework import serializers

from club.models import Dancer


class DancerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dancer
        fields = ['name', 'sex']