from rest_framework import serializers

from .models import leads

class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = leads
        fields = '__all__'   #take all the fields in the model
