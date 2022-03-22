from dataclasses import fields
from rest_framework import serializers
from .models import User,QuestionEntry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail','birth_day','created_at','update_at')
        
class QuestionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionEntry
        fields = ('title','question','created_at','update_at')