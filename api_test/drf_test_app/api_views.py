from rest_framework import viewsets

from drf_test_app.models import User,Question
from drf_test_app.serializer import UserSerializer,QuestionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
