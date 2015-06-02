from rest_framework import viewsets

from .models import Question, Choice
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
