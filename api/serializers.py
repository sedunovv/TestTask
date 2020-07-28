from interview_main.models import Answer, Interview, Question

from rest_framework import serializers


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = ('id', 'name', 'description', 'date_start', 'date_end')


class QuestionDetailSerializer(serializers.ModelSerializer):

    interview = InterviewSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'type_question', 'text_for_answer', 'interview')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text', 'type_question', 'text_for_answer')


class InterviewListSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Interview
        fields = ('id', 'name', 'description', 'date_start', 'date_end', 'questions')


class AnswerSerializer(serializers.ModelSerializer):

    question = QuestionDetailSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
