from django.db import models
from django.utils.timezone import now

class TableHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(null=False)
    hash = models.TextField (null=True)
    last_modified = models.DateTimeField(default=now)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Histories"

    def __str__(self):
        return self.name
