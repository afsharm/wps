from django.db import models

class Province(models.Model):
    class Meta:
       managed = False
       db_table = "province"
    name = models.CharField(max_length=50)