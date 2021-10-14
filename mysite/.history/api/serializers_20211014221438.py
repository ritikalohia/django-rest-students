from rest_framework.serializers import ModelSerializer
from .models import Note

class Serializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '_all_'