from django_filters.rest_framework import DjangoFilterBackend
from interview_main.models import Answer, Interview, Question
from rest_framework import generics, viewsets
from .helpers import InterviewFilter

from .serializers import (
    AnswerSerializer,
    AnswerCreateSerializer,
    InterviewListSerializer
)


class InterviewListView(generics.ListAPIView):
    serializer_class = InterviewListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = InterviewFilter

    def get_queryset(self):
        interviews = Interview.objects.all()
        return interviews


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Answer.objects.filter(user=self.kwargs.get('pk', 0))

    def get_serializer_class(self):
        if self.action == 'list':
            return AnswerSerializer


class AnswerCreateViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerCreateSerializer
