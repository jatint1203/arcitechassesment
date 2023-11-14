from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=10)
    created_at = models.CharField(max_length=10)
    # created_at = models.DateField()
    # created_at = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # ids = models.AutoField(primary_key=True)
    author = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
  

    def __str__(self):
        return self.author
