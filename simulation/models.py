
import uuid
from django.db import models

class Simulation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    size = models.IntegerField()
    p, f = models.FloatField(), models.FloatField()
    steps_count = models.IntegerField(default=0)
    grid_data = models.JSONField()
    fire_histogram = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
