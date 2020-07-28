from django.contrib import admin
from .models import Answer, Interview, Question


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'type_answer', 'answer', 'multiple_choice_answer')
    search_fields = ['user']


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'date_end', 'description')
    search_fields = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type_question', 'text_for_answer')
    search_fields = ['text']
    filter_horizontal = ('interview',)
