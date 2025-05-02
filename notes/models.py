# notes/models.py

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null= True,     # ← यहाँ add करो
    blank=True     # ← यहाँ भी add करो
)


    def __str__(self):
        return self.title
