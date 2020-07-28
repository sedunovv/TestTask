from django.db import models


class Interview(models.Model):

    class Meta:
        db_table = "interviews"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    name = models.CharField(verbose_name="Название опроса", max_length=200)
    date_start = models.DateField(verbose_name="Дата начала опроса", auto_now_add=True)
    date_end = models.DateField(verbose_name="Дата окончания опроса", null=True)
    description = models.CharField(verbose_name="Описание опроса", max_length=1500)

    def __str__(self):
        return self.name
