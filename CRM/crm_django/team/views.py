from email.policy import HTTP
from django.shortcuts import render
from .serializers import TeamSerializer,UserSerializer
from .models import Team,Plan
from rest_framework import viewsets,status,views
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members_in=[self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by = self.request.user)
        obj.members.add(self.request.user)
        obj.save()

class UserDetailView(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    


@api_view(['GET'])
def get_my_team(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    return Response(serializer.data)    

@api_view(['POST'])
def add_member(request):
    user = User.objects.get(username=request.data['email'])
    team = Team.objects.filter(members__in=[request.user]).first()
    print(team.name)
    team.members.add(user)
    team.save()
    return Response()

@api_view(['POST'])
def upgrade_plan(request):
    team = Team.objects.filter(members__in = [request.user]).first()
    print("hello")
    print(team)
    name_plan = request.data['name_plan']
    print(name_plan)
    if name_plan == 'free':
        plan = Plan.objects.get(name='Free')
    if name_plan == 'smallteam':
        plan = Plan.objects.get(name="Small Team")
    elif name_plan == 'bigteam':
        plan = Plan.objects.get(name='Big Team')

    team.plan = plan
    team.save()
    serializer = TeamSerializer(team)
    return Response(serializer.data)
