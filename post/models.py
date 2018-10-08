from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    field = models.TextField(verbose_name='正文')











