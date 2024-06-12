from django.shortcuts import render
from rest_framework import viewsets
from .models import leads
from .serializers import LeadsSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadsSerializer
    queryset = leads.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(created_by = self.request.user)
