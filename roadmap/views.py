# # roadmap/views.py
# from __future__ import annotations

# import json
# from typing import List, Dict, Any

# from django.shortcuts import render, get_object_or_404
# from .models import Roadmap, Node


# def roadmap_detail(request, slug: str):
#     """
#     Render an interactive roadmap graph.

#     Expects a template at: templates/roadmap/detail.html
#     and uses Django's json_script in the template to safely embed JSON.
#     """
#     roadmap = get_object_or_404(Roadmap, slug=slug)

#     # Fetch nodes for this roadmap (ordered for stable layout)
#     nodes = (
#         Node.objects
#         .filter(roadmap=roadmap)
#         .select_related("parent")
#         .order_by("order", "id")
#     )

#     # Build Cytoscape elements: nodes + edges
#     elements: List[Dict[str, Any]] = []

#     # Nodes
#     for n in nodes:
#         elements.append({
#             "data": {
#                 "id": str(n.id),           # IDs must be strings for Cytoscape
#                 "label": n.label,
#                 "url": n.url or "",
#             },
#             "classes": n.category,         # used for styling/filtering (e.g., "optional")
#         })

#     # Edges (parent -> child)
#     for n in nodes:
#         if n.parent_id:
#             elements.append({
#                 "data": {
#                     "source": str(n.parent_id),
#                     "target": str(n.id),
#                 }
#             })

#     context = {
#         "roadmap": roadmap,
#         # IMPORTANT: pre-serialize to JSON string; template will read via json_script
#         "elements_json": json.dumps(elements),
#     }
#     return render(request, "roadmap/detail.html", context)
# roadmap/views.py
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
