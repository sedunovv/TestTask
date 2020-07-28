from django.contrib.postgres.fields import ArrayField
from django.db import models

from .helpers import *


class Answer(models.Model):

    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    user = models.IntegerField(verbose_name="ID пользователя")
    question = models.ForeignKey('Question', verbose_name="Вопрос", related_name="answers",
                                 on_delete=models.CASCADE)
    type_answer = models.SmallIntegerField(
        verbose_name="Тип ответа",
        choices=((TEXT, "Ответ с текстом"), (CHOICE, "Ответ с выбором одного варианта"),
                 (MULTIPLE_CHOICE, "Ответ с выбором нескольких вариантов")), default=TEXT)
    answer = ArrayField(
        models.CharField(verbose_name="Ответ текстом/с выбором одного варианта", max_length=200),
        size=1,
        default=list,
        blank=True
    )
    multiple_choice_answer = ArrayField(
        models.CharField(verbose_name="Ответ с выбором нескольких вариантов", max_length=200),
        default=list,
        blank=True
    )
