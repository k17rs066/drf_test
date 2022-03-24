from dataclasses import fields
from rest_framework import serializers
from drf_test_app.models import User,Question

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail','birth_day','created_at','update_at')
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title','question','created_at')