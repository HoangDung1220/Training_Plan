from django.shortcuts import render
from rest_framework import viewsets
from .models import Lead
from .serializers import LeadSerializer
from django.contrib.auth.models import User

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def perform_create(self, serializer):
        print(self.request.user)
        return serializer.save(created_by=self.request.user)

    
