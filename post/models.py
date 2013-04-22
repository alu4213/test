from django.db import models

class Post(models.Model):
    message = models.CharField(max_length=175)
    pub_date = models.DateTimeField('date published')

class Response(models.Model):
    post= models.ForeignKey(Post)
    message = models.CharField(max_length=200)
