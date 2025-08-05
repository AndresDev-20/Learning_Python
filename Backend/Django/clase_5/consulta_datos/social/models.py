from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return f"Comment by {self.user.name}"