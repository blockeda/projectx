from django.db import models
from django.template.defaultfilters import title


class Vacansy(models.Model):
    title= models.CharField(unique=True,max_length=200,verbose_name='название')
    salary= models.CharField()
    area=models.TextField()
    published=models.DateTimeField()


    def __str__(self):
        return self.title


