from django.db import models
# Create your models here.


class Status(models.Model):
    """Status model"""

    name = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
