import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Roadmap, Node
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

def roadmap_index(request):
    """List all roadmaps (or redirect if you only have one)."""
    roadmaps = Roadmap.objects.all().order_by("title")
    if roadmaps.count() == 1:
        # optional: auto-jump to the only roadmap
        return redirect("roadmap:detail", slug=roadmaps.first().slug)
    return render(request, "roadmap/index.html", {"roadmaps": roadmaps})

def roadmap_detail(request, slug: str):
    roadmap = get_object_or_404(Roadmap, slug=slug)
    nodes = roadmap.nodes.all().order_by("order")

    # qs = (Node.objects
    #       .filter(roadmap=roadmap)
    #       .select_related("parent")
    #       .order_by("order", "id"))

    elements = []
    for n in nodes:
        elements.append({
            "data": {
                "id": n.key,
                "key": n.key,              # important — used to fetch sidebar HTML later
                "label": n.label,
                "description": n.description,
                "url": n.url,
            },
            "classes": "link" if n.url else ""
        })

        # Add edges (connections) if this node has a parent
        if n.parent_id:
            elements.append({
                "data": {
                    "id": f"{n.parent.key}->{n.key}",
                    "source": n.parent.key,
                    "target": n.key,
                }
            })

    context = {
        "roadmap": roadmap,
        "elements": elements,
        "node_count": nodes.count(),
        "edge_count": len([e for e in elements if "source" in e["data"]]),
    }
    return render(request, "roadmap/detail.html", context)

def node_sidebar(request, key): 
    node = get_object_or_404(Node, key=key)
    specific = f"roadmap/nodes/{node.key}.html"
    try: 
        get_template(specific) 
        html = render_to_string(specific, {"node":node})
    except Exception: 
        html = render_to_string("roadmaps/nodes/sidebar_fallback.html", {"node": node})
    return HttpResponse(html)