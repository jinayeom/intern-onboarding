from django.conf import settings
from django.db import models

class Roadmap(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

CATEGORY_CHOICES = [
    ("core", "Core"),
    ("optional", "Optional"),
    ("tool", "Tool"),
]

class Node(models.Model):
    roadmap = models.ForeignKey(Roadmap, related_name="nodes", on_delete=models.CASCADE)
    key = models.SlugField()                        # stable identifier like "learn-programming"
    label = models.CharField(max_length=200)        # text shown in the box
    description = models.TextField(blank=True)      # optional sidebar text
    url = models.URLField(blank=True)               # click to open link
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="core")
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children",
                               on_delete=models.CASCADE)  # parent→child edge
    order = models.PositiveIntegerField(default=0)  # sibling ordering

    class Meta:
        unique_together = ("roadmap", "key")
        ordering = ["order", "id"]

    def __str__(self):
        return self.label

class NodeCompletion(models.Model):
    """Per-user check marks (optional)."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "node")
