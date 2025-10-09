from django.urls import path
from . import views

app_name = "lessons"
urlpatterns = [
    path("<slug:slug>/", views.topic_detail, name="topic_detail"),
]
