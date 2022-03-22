import django_filters
from rest_framework import viewsets, filters

from .models import User,QuestionEntry
from .serializer import UserSerializer,QuestionEntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class QuestionEntryViewSet(viewsets.ModelViewSet):
    queryset = QuestionEntry.objects.all()
    serializer_class = QuestionEntrySerializer
