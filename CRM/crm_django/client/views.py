from unicodedata import name
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404
from .serializer import ClientSerializer, NoteSerializer,TeamSerializer
from .models import Client,Note
from team.models import Team
from lead.models import Lead
from rest_framework.decorators import api_view

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in =[self.request.user]).first()
        return serializer.save(team=team,created_by = self.request.user)
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in =[self.request.user]).first()
        id_client = self.request.data['id_client']
        client = Client.objects.get(pk=id_client)
        return serializer.save(team =team,client=client,created_by = self.request.user)

@api_view(['POST'])
def convert_lead_to_client(request):
    print(request.data)
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']
    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        Http404
    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person, email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)
    return Response()