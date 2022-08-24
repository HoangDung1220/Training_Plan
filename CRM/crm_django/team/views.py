from django.shortcuts import render
from .serializers import TeamSerializer
from .models import Team
from rest_framework import viewsets

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def perform_create(self, serializer):
        obj = serializer.save(created_by = self.request.user)
        obj.members.add(self.request.user)
        obj.save()

        