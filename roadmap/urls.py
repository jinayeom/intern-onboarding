from django.urls import path
from . import views
from .api import RoadmapDetailAPI, NodeDetailAPI

app_name = "roadmap"

urlpatterns = [
    path("", views.roadmap_index, name="index"),
    path("<slug:slug>/", views.roadmap_detail, name="detail"),

    path("api/roadmaps/<slug:slug>/", RoadmapDetailAPI.as_view(), name="api_roadmap_detail"),
    path("api/nodes/<int:pk>/", NodeDetailAPI.as_view(), name="api_node_detail"),
    path("node/<slug:key>/sidebar/", views.node_sidebar, name="node_sidebar")
]
