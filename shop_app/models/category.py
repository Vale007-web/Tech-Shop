from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    @staticmethod
    @staticmethod
    def get_all_categories():
        return Category.objects.all().order_by('name')