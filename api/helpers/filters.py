from django_filters import rest_framework as filters

from interview_main.models import Interview


class InterviewFilter(filters.FilterSet):
    """
    Фильтруем по дата начала и дате окончания опроса
    для получения актуальных опросов
    """
    date_start = filters.DateFilter(
        lookup_expr='gte',
        field_name='date_start',
        label='Дата начала, формат: YYYY-mm-dd'
    )
    date_end = filters.DateFilter(
        lookup_expr='lte',
        field_name='date_end',
        label='Дата окончания, форма: YYYY-mm-dd'
    )

    class Meta:
        model = Interview
        fields = ['date_start', 'date_end']
