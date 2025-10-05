from django.contrib import admin
from .models import Roadmap, Node, NodeCompletion

class NodeInline(admin.TabularInline):
    model = Node
    extra = 0

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [NodeInline]

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("label", "roadmap", "category", "parent", "order")
    list_filter = ("roadmap", "category")
    search_fields = ("label", "key")

admin.site.register(NodeCompletion)
