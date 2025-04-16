from django.db import models
from django.contrib.auth.models import User

# Task model to store user tasks
class Task(models.Model):
    # Links the task to a user; if the user is deleted, their tasks are also deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    # Title of the task
    title = models.CharField(max_length=200)
    # Description of the task, optional
    description = models.TextField(null=True, blank=True)
    # Indicates whether the task is complete
    complete = models.BooleanField(default=False)
    # Timestamp when the task was created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # Tasks are ordered by their completion status (incomplete tasks come first)
        ordering = ['complete']
