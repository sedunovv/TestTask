from django.urls import path

from . import views


urlpatterns = [
    path('interviews/', views.InterviewListView.as_view()),
    path('interviews/<int:pk>/', views.InterviewDetailView.as_view({'get': 'retrieve'})),
    path('answers/user/<int:pk>', views.AnswerViewSet.as_view({'get': 'list'})),
    path('answers/user/', views.AnswerCreateViewSet.as_view({'post': 'create'})),
]
