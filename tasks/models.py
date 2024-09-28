from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')])
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    due_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
