from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.TaskList.as_view()),
    path('<int:pk>', views.TaskDetail.as_view()),
    path('create/', views.TaskCreate.as_view()),
]
