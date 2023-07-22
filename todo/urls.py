from django.urls import path
from .views import (ListCreateToDoApiView,RUDApiView,StatusUpdateView)

urlpatterns = [
    path('', ListCreateToDoApiView.as_view()),
    path('<pk>/', RUDApiView.as_view()),
    path('status/<int:task_id>/', StatusUpdateView.as_view())
]