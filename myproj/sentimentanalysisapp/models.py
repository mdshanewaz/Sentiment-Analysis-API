from django.db import models

# Create your models here.

class Sentimenttb(models.Model):
    text = models.TextField(max_length=100, null=True, blank=True)
    result = models.CharField(max_length= 100, null=True, blank=True)

    # def __str__(self):
    #     return self.id
