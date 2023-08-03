from django.db import models


class MyHistore(models.Model):
    email = models.EmailField(max_length=100)
    userName = models.CharField(max_length=100)
    title = models.TextField()
    data_create = models.DateTimeField("date_create", auto_now_add=True)
    quantity_like = models.IntegerField(default=0)
    quantity_dislike = models.IntegerField(default=0)

    def __str__(self):
        return f"Author histore {self.email}"
