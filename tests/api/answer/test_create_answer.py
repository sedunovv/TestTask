import pytest
from hamcrest import *  # noqa
from django.urls import reverse

from interview_main.models import Interview, Question

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def question_data():
    Question.objects.create(
        text='Is it test question?',
        type_question=1,
        text_for_answer=['Да', 'Нет'])


def create_answer(client, question, type_answer, answer, multiple_choice_answer):
    return client.post(
        reverse('create_answer'), data={'user': 123, 'question': question.id, 'type_answer': type_answer,
                                        'answer': answer, 'multiple_choice_answer': multiple_choice_answer},
        format='json')


def test_create_answer(client):
    question = Question.objects.get(text='Is it test question?')
    answer = [question.text_for_answer[0]]
    response = create_answer(client, question, question.type_question, answer, list())
    assert_that(response.status_code, equal_to(201))


def test_create_answer_no_question(client):
    question = Question.objects.get(text='Is it test question?')
    answer = [question.text_for_answer[1]]
    response = create_answer(client, question, 2, answer, list())
    assert_that(response.status_code, equal_to(400))


def test_create_answer_incorrect_answer(client):
    question = Question.objects.get(text='Is it test question?')
    answer = ['String']
    response = create_answer(client, question, question.type_question, answer, list())
    assert_that(response.status_code, equal_to(400))
