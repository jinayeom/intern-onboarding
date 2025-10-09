import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Roadmap, Node

def roadmap_index(request):
    """List all roadmaps (or redirect if you only have one)."""
    roadmaps = Roadmap.objects.all().order_by("title")
    if roadmaps.count() == 1:
        # optional: auto-jump to the only roadmap
        return redirect("roadmap:detail", slug=roadmaps.first().slug)
    return render(request, "roadmap/index.html", {"roadmaps": roadmaps})

def roadmap_detail(request, slug: str):
    roadmap = get_object_or_404(Roadmap, slug=slug)

    qs = (Node.objects
          .filter(roadmap=roadmap)
          .select_related("parent")
          .order_by("order", "id"))

    elements = []
    for n in qs:
        elements.append({
            "data": {"id": str(n.id), "label": n.label, "url": n.url or ""},
            "classes": n.category or ""
        })
    for n in qs:
        if n.parent_id:
            elements.append({"data": {"source": str(n.parent_id), "target": str(n.id)}})

    empty = (len(elements) == 0)   # <-- flag for template

    node_count = sum(1 for e in elements if "label" in e.get("data", {}))
    edge_count = sum(1 for e in elements if "source" in e.get("data", {}))

    return render(
        request,
        "roadmap/detail.html",
        {
            "roadmap": roadmap,
            "elements": elements,
            "node_count": node_count,
            "edge_count": edge_count,
            "empty": empty,              # <-- pass flag
        },
    )
