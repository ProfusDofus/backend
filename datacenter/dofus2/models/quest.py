from django.db import models
from django.db.models import F
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class QuestManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().all()

    def local_only(self, lang):
        return super().get_queryset().only('id')\
            .annotate(name=F(f'name_{lang}'))

class Quest(models.Model):
    id = models.AutoField(primary_key=True)
    name_fr = models.TextField(blank=True)
    name_en = models.TextField(blank=True)
    name_es = models.TextField(blank=True)
    name_pt = models.TextField(blank=True)
    name_it = models.TextField(blank=True)
    name_de = models.TextField(blank=True)
    category = models.ForeignKey(
        'QuestCategory',
        on_delete=models.PROTECT,
        related_name='quests'
    )
    repeat_type = models.IntegerField()
    dungeon = models.BooleanField()
    group = models.BooleanField()
    level_min = models.IntegerField()
    level_max = models.IntegerField()
    start_criterion = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    objects = QuestManager()

    def get_absolute_url(self):
        return reverse('dofus2:quest-detail', args=[str(self.id)])

    def __str__(self):
        return _(self.name_fr)
