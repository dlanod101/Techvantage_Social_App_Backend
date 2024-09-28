from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

from rest_framework.views import APIView

# Create your views here.
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "pk"


class ProjectList(APIView):
    def get(self, request, format=None):
        #Gets title from the query parameter
        tag = request.query_params.get("tag", "")

        category = request.query_params.get("category", "")

        contributors = request.query_params.get("contributors", "")

        
        if category:
            project = Project.objects.filter(category__icontains=category)

        if tag:
            project = Project.objects.filter(tag__icontains=tag)

        if contributors:
            project = Project.objects.filter(contributors__icontains=contributors)
        
        else:
            project = Project.objects.all()

        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
