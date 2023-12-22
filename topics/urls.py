from django.urls import path
from topics import views

urlpatterns = [
    path("", views.topic_index, name="topic_index"),
    path("<int:pk>", views.topic_detail, name="topic_detail"),
]