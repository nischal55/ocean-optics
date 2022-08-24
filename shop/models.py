from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    image = models.CharField(max_length=122, default='')

    def __str__(self):
        return self.item_name


