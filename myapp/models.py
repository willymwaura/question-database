
from django.db import models


# Create your models here.
class Feature (models.Model):
    question=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return '{}'.format(self.question)



