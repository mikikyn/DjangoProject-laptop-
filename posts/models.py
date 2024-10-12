from django.db import models


"""
Posts.objects.all() - все объекты из таблицы

Post.objects.filter(title="post") - все объекты по условию

Post.objects.get(id=1) - один объект по условию
"""


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title