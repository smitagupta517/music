from django.db import models


class Menu(models.Model):
    category = models.CharField(max_length=50)
    image = models.FileField()

    def __str__(self):
        return self.category

