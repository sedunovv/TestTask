from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from interview_main.models import Answer, Interview, Question
from rest_framework import generics, viewsets
from .helpers import InterviewFilter

from .serializers import (
    AnswerSerializer,
    AnswerCreateSerializer,
    InterviewDetailSerializer,
    InterviewListSerializer
)


class InterviewListView(generics.ListAPIView):
    serializer_class = InterviewListSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = InterviewFilter

    def get_queryset(self):
        interviews = Interview.objects.all()
        return interviews


class InterviewDetailView(viewsets.ReadOnlyModelViewSet):
    pagination_class = None

    def get_queryset(self):
        interview = Interview.objects.filter(id=self.kwargs.get('pk', 0))
        interview = interview.annotate(questions_count=models.Count("questions"))
        return interview

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return InterviewDetailSerializer

    def set_answers_count(self, interview):
        answers = interview.annotate(
            answers_count=models.Count('questions__answers')
        ).values_list("questions__answers__user", "answers_count")
        return answers

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        interview = get_object_or_404(queryset, pk=self.kwargs.get('pk', 0))
        serializer = self.get_serializer(interview)
        data = serializer.data
        data.update({'answers_statistics': self.set_answers_count(queryset)})
        return Response(data)


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Answer.objects.filter(user=self.kwargs.get('pk', 0))

    def get_serializer_class(self):
        if self.action == 'list':
            return AnswerSerializer


class AnswerCreateViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer

    def perform_create(self, serializer):
        question = Question.objects.filter(id=self.request.data.get('question', None),
                                           type_question=self.request.data.get('type_answer', None))
        if not question:
            raise ValidationError('There is no such question')
        elif self.request.data.get('type_answer') == 0:
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValidationError('Invalid data in request')
        elif self.request.data.get('type_answer') == 1:
            question = question.filter(text_for_answer__contains=self.request.data.get('answer', None))
            if not question:
                raise ValidationError('There is no such answer on question')
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValidationError('Invalid data in request')
        elif self.request.data.get('type_answer') == 2:
            question = question.filter(text_for_answer__contains=self.request.data.get('multiple_choice_answer', None))
            if not question:
                raise ValidationError('There is no such answer on question')
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValidationError('Invalid data in request')
        else:
            raise ValidationError('There is no such question')
