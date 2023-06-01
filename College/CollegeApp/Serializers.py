from rest_framework import serializers
from CollegeApp.models import College

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields ='__all__'