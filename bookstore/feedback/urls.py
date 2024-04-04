from django.urls import path

from feedback.views import feedback, feedback_sent

urlpatterns = [
    path('', feedback, name='feedback'),
    path('sent/', feedback_sent, name='feedback_sent'),
]
