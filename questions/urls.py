from django.urls import path
from questions.views  import (DeleteAnswer)

urlpatterns = [
     path('answer/<int:pk>/delete/', DeleteAnswer.as_view(), name="delete_answer"),
]
#
