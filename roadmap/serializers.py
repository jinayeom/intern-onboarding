from rest_framework import serializers
from .models import Roadmap, Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ["id", "key", "label", "description", "url", "category", "parent", "order"]

class RoadmapSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)

    class Meta:
        model = Roadmap
        fields = ["id", "slug", "title", "nodes"]
