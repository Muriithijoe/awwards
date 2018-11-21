from rest_framework import serializers
from .models import AwardsProfiles,AwardsProjects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsProfiles
        fields = ('name', 'bio', 'projects', 'dp')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsProjects
        fields = ('project_name', 'description')
