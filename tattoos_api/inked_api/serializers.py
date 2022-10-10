from rest_framework import serializers
from .models import Tattoo
from .models import Admin   

class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tattoo
        fields = ('id', 'image', 'artist', 'description',)
        