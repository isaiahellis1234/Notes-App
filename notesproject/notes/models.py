from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    sender = models.ForeignKey(User, related_name="sent_notes", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="received_notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient} - {self.title}"
