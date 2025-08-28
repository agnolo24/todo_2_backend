from django.db import models

# Create your models here.

class Todo(models.Model):
    CHOICE = [
        ('d', 'done'),
        ('p', 'pending'),
        ('t', 'terminated')
    ]
    title = models.CharField(max_length=20)
    status = models.CharField(max_length=1, default='p', choices=CHOICE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title