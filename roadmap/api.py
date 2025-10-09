from rest_framework import generics
from .models import Roadmap, Node
from .serializers import RoadmapSerializer, NodeSerializer

class RoadmapDetailAPI(generics.RetrieveAPIView):
    queryset = Roadmap.objects.all()
    lookup_field = "slug"
    serializer_class = RoadmapSerializer

class NodeDetailAPI(generics.RetrieveAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
