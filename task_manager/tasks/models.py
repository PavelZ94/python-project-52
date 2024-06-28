from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
# Create your models here.


class Task(models.Model):
    """Task model"""

    name = models.CharField(max_length=100,
                            unique=True,)

    #description = models.TextField(blank=True,
    #                               null=True,)

    author = models.ForeignKey(User,
                               null=True,
                               related_name='author',
                               on_delete=models.PROTECT,)

    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True,
                               related_name='status',)

    executor = models.ForeignKey(User,
                                 null=True,
                                 blank=True,
                                 related_name='executor',
                                 on_delete=models.PROTECT,)

    created_at = models.DateTimeField(auto_now_add=True)

    labels = models.ManyToManyField(Label,
                                    blank=True,
                                    through='LabelAndTaskRelation',
                                    related_name='label',)

    def __str__(self):
        return self.name


class LabelAndTaskRelation(models.Model):
    """Model of relations between tasks and labels"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
