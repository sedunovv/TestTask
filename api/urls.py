from django.urls import path

from . import views


urlpatterns = [
    path('interviews/', views.InterviewListView.as_view(), name='interviews'),
    path('interviews/<int:pk>/', views.InterviewDetailView.as_view({'get': 'retrieve'}), name='interview_details'),
    path('answers/user/<int:pk>', views.AnswerViewSet.as_view({'get': 'list'}), name='user_answers'),
    path('answers/user/', views.AnswerCreateViewSet.as_view({'post': 'create'}), name='create_answer'),
]
