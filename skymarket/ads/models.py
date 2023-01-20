from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User,related_name='ads',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='django_media/',null=True)


    class Meta:
        verbose_name= "обьявление"
        verbose_name_plural = "обьявления"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length= 500)
    author = models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, related_name='ad',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text

