import json
from django.shortcuts import render, get_object_or_404
from .models import Roadmap, Node

def roadmap_detail(request, slug: str):
    roadmap = get_object_or_404(Roadmap, slug=slug)

    qs = (
        Node.objects
        .filter(roadmap=roadmap)
        .select_related("parent")
        .order_by("order", "id")
    )

    elements = []
    # Nodes
    for n in qs:
        elements.append({
            "data": {"id": str(n.id), "label": n.label, "url": n.url or ""},
            "classes": n.category or ""
        })
    # Edges
    for n in qs:
        if n.parent_id:
            elements.append({"data": {"source": str(n.parent_id), "target": str(n.id)}})

    # Fallback so you see something even if DB is empty
    if not elements:
        elements = [
            {"data": {"id": "A", "label": "DevOps"}},
            {"data": {"id": "B", "label": "Learn a Programming Language"}},
            {"data": {"id": "C", "label": "Python"}},
            {"data": {"source": "A", "target": "B"}},
            {"data": {"source": "B", "target": "C"}},
        ]

    node_count = sum(1 for e in elements if "label" in e.get("data", {}))
    edge_count = sum(1 for e in elements if "source" in e.get("data", {}))

    return render(
        request,
        "roadmap/detail.html",
        {
            "roadmap": roadmap,
            "elements_json": json.dumps(elements),
            "node_count": node_count,
            "edge_count": edge_count,
        },
    )
