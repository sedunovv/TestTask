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


class InterviewDetailSerializer(serializers.ModelSerializer):

    questions_count = serializers.IntegerField()

    class Meta:
        model = Interview
        fields = ('id', 'name', 'description', 'date_start', 'date_end', 'questions_count')


class AnswerSerializer(serializers.ModelSerializer):

    question = QuestionDetailSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        answer, _ = Answer.objects.update_or_create(
            user=validated_data.get('user', None),
            type_answer=validated_data.get('type_answer', None),
            question=validated_data.get('question', None),
            defaults={'answer': validated_data.get('answer', None),
                      'multiple_choice_answer': validated_data.get('multiple_choice_answer', None)},
        )
        return answer
