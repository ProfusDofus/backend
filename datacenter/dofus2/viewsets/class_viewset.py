from ..models import CharacterClass
from ..serializers import ClassSerializer, ClassLocalSerializer
from ._dofus_viewset import DofusViewSet


class ClassViewSet(DofusViewSet):
    model_class = CharacterClass
    default_serializer = ClassSerializer
    local_serializer = ClassLocalSerializer
