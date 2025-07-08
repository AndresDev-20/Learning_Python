from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=100, null= False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
