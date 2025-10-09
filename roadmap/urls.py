from django.urls import path
from . import views
from .api import RoadmapDetailAPI, NodeDetailAPI

app_name = "roadmap"

urlpatterns = [
    # your normal HTML views
    path("", views.roadmap_index, name="index"),
    path("<slug:slug>/", views.roadmap_detail, name="detail"),

    # new API endpoints
    path("api/roadmaps/<slug:slug>/", RoadmapDetailAPI.as_view(), name="api_roadmap_detail"),
    path("api/nodes/<int:pk>/", NodeDetailAPI.as_view(), name="api_node_detail"),
]
