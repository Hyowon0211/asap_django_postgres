from django.db import models

# Create your models here.

# 게시글 모델, post_id, prof_id, title, start_date, end_date, start_time, end_time,
            # created_at, updated_at, content
class Post(models.Model):
    #prof_id = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
