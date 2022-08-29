from dataclasses import field
from rest_framework import serializers
from .models import Client,Note
from team.serializers import TeamSerializer

class ClientSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Client
        
        fields = ('id','team','name','contact_person','email','phone','website','created_at','updated_at')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','name','body','created_at','updated_at')