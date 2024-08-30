from rest_framework import serializers
from StudentApp.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'  # Corrected the typo here
