from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
# Create your models here.


class Task(models.Model):

    author = models.ForeignKey(User, null=True, related_name='author', on_delete=models.PROTECT)

    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)

    executor = models.ForeignKey(User, null=True, related_name='executor', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, unique=True)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name