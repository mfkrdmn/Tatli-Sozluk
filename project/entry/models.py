from django.db import models
from user.models import *
# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_slug =  models.CharField(max_length=85, blank=True, null=True)
    entry_name =  models.CharField(max_length=85, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entry_name


class EntryComments(models.Model):
    comment_body =  models.CharField(max_length=85, blank=True, null=True)
    commented_entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    likes_to_the_comment = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)