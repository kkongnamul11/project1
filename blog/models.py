from django.db import models
from datetime import datetime

# Create your models here.

class blog(models.Model):

    #블로그 기능에 필요한 내용들
    title = models.CharField(max_length = 200)
    cover = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    create_at = models.DateTimeField(default = datetime.now, blank= True)
    
    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name_plural = "blog"


class imageMain(models.Model):
    #메인 랜딩 이미지

    title = models.CharField(max_length = 200)
    banner = models.ImageField(upload_to = 'images/')
    #img_url = models.URLField(max_length = 100)

    def __str__(self):
        return self.title