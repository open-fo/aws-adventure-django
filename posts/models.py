from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    class Meta:
        pass

    title = models.CharField(max_length=256)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
