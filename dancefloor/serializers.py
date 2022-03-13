from rest_framework import serializers

from club.models import Dancer, DanceSkill, Level, Dance


class DanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dance
        fields = '__all__'


class DanceSkillSerializer(serializers.ModelSerializer):
    level = serializers.ChoiceField(Level.choices)

    class Meta:
        model = DanceSkill
        exclude = ['dancer', ]


class DancerSerializer(serializers.ModelSerializer):
    skills = DanceSkillSerializer(many=True)

    class Meta:
        model = Dancer
        fields = '__all__'

    def create(self, validated_data):
        dancer = Dancer.objects.create(name=validated_data['name'], sex=validated_data['sex'])
        for skill_data in validated_data.pop('skills'):
            DanceSkill.objects.create(dancer=dancer, **skill_data)
        return dancer


class DancerWithActionSerializer(serializers.ModelSerializer):
    skills = DanceSkillSerializer(many=True)
    action = serializers.SerializerMethodField()

    class Meta:
        model = Dancer
        fields = '__all__'

    def get_action(self, obj):
        return obj.action(self.context)
