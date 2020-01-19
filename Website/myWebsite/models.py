from django.db import models

# Create your models here.

class Post(models.Model):
    Post_title = models.CharField(max_length = 200)
    Post_content = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Post_title
