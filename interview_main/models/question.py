from django.contrib.postgres.fields import ArrayField
from django.db import models

from .helpers import *


class Question(models.Model):

    class Meta:
        db_table = "questions"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    text = models.CharField(verbose_name="Текст вопроса", max_length=1000)
    interview = models.ManyToManyField('Interview', verbose_name="Опрос", related_name="questions")
    type_question = models.SmallIntegerField(
        verbose_name="Тип ответа",
        choices=((TEXT, "Ответ с текстом"), (CHOICE, "Ответ с выбором одного варианта"),
                 (MULTIPLE_CHOICE, "Ответ с выбором нескольких вариантов")), default=TEXT)
    text_for_answer = ArrayField(
        models.CharField(verbose_name="Ответ с выбором вариантов ответа", max_length=200, blank=True),
        default=list,
        blank=True
    )

    def __str__(self):
        return self.text
