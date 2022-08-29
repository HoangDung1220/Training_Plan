from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Lead
from .serializers import LeadSerializer
from django.contrib.auth.models import User
from team.models import Team
from rest_framework.pagination import PageNumberPagination

class LeadPagination(PageNumberPagination):
    page_size = 2

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = LeadPagination
    filter_backends =  (filters.SearchFilter,)
    search_fields = ('company', 'contact_person')

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in = [self.request.user]).first()
        return serializer.save(team=team,created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in = [self.request.user]).first()
        return self.queryset.filter(team=team)

    def perform_update(self, serializer):
        id_member = self.request.data['assigned_to']
        if id_member:
            user = User.objects.get(pk=id_member)
            serializer.save(assigned_to=user)
        else:
            serializer.save()
        return super().perform_update(serializer)
    

    
