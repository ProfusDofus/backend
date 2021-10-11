from rest_framework import serializers

from datacenter.dofus2.models import CharacterClass
from datacenter.dofus2.serializers import ClassSpellSerializer, ClassSpellLocalSerializer


class ClassSerializer(serializers.ModelSerializer):
    spells = ClassSpellSerializer(many=True)
    class Meta:
        model = CharacterClass
        fields = '__all__'

class ClassLocalSerializer(serializers.ModelSerializer):
    spells = ClassSpellLocalSerializer(many=True)
    class Meta:
        model = CharacterClass
        fields = [
            "id",
            "male_look",
            "female_look",
            "spells"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = instance.name
        return data
