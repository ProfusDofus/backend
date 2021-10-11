from rest_framework import serializers

from datacenter.dofus2.models import CharacterClassSpell
from datacenter.dofus2.serializers import SpellSerializer, SpellLocalSerializer


class ClassSpellSerializer(serializers.ModelSerializer):
    spell = SpellSerializer()
    class Meta:
        model = CharacterClassSpell
        fields = ['index', 'spell']

class ClassSpellLocalSerializer(serializers.ModelSerializer):
    spell = SpellLocalSerializer()
    class Meta:
        model = CharacterClassSpell
        fields = ['index', 'spell']
