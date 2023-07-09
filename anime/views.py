from django.shortcuts import render
from rest_framework import generics
from .models import Anime
from .serializers import AnimeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class AnimeList(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class= AnimeSerializer
    permission_classes = [IsAuthenticated]

class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsOwnerOrReadOnly]
