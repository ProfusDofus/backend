from rest_framework import serializers

from datacenter.dofus2.models import SpellLevel

class SpellLevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpellLevel
        fields = '__all__'

class SpellLevelLocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpellLevel
        fields = [
            "id",
            "grade",
            "ap_cost",
            "min_range",
            "range",
            "range_alterable",
            "cast_in_line",
            "cast_in_diagonal",
            "critical_chance",
            "max_stack",
            "cast_per_turn",
            "cast_per_target",
            "cast_interval",
            "start_cooldown",
            "global_cooldown",
            "min_level"
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
