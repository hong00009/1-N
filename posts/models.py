from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # comment_set 자동생성


class Comment(models.Model):
    # id 는 자동생성
    # 컬럼값 2개 추가
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    # post_id 자동생성
    # 누구랑 연결시킬지
    # 지워지면 어떻게할건지