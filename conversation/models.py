from django.db import models
from django.contrib.auth.models import User

from item.models import Item


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations',
                             on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated_at",)
        
    def __str__(self):
        return self.item.name


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages',
                                     on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_message',
                                   on_delete=models.CASCADE)
    
    def __str__(self):
        return "Send by {} to {}".format(self.created_by.username, self.conversation.item.created_by)