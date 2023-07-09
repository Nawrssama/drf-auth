from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        # fields='__all__'
        fields = ('id','owner','name','desc','created_at','updated_at')