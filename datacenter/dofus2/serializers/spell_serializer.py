from rest_framework import serializers

from datacenter.dofus2.models import Spell
from datacenter.dofus2.serializers import SpellLevelSerializer

class SpellSerializer(serializers.ModelSerializer):
    # grades = SpellLevelSerializer()
    class Meta:
        model = Spell
        fields = ["id", "grades", "name_fr", "name_en", "name_es", "name_pt", "name_it", "name_de", "description_fr", "description_en", "description_es", "description_pt", "description_it", "description_de", "icon_id"]
        depth = 2

class SpellLocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = [
            "id",
            "icon_id",
            "grades"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = instance.name_fr
        data['description'] = instance.description_fr
        return data
