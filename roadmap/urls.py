from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.roadmap_detail, name="roadmap"),
]
