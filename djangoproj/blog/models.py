from django.db import models
import datetime
from tinymce import models as tinymce_models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body= tinymce_models.HTMLField()
    blog_date = models.CharField(max_length=200)
    image = models.CharField(max_length=800)
    BlogId = models.CharField(max_length=200)
    discription = models.TextField()
    def __str__(self):
        return f"post : {self.title}"
class Projects(models.Model):
    Name = models.CharField(max_length= 1000)
    description = models.TextField()
    Project_image = models.CharField(max_length=400)
    project_article = models.CharField(max_length= 200)
