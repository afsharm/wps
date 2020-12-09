from django.db import models

class Province(models.Model):
    class Meta:
       managed = False
       db_table = "province"
    name = models.CharField(max_length=50)

class County(models.Model):
    class Meta:
       managed = False
       db_table = "county"
    name = models.CharField(max_length=50)
    province = models.IntegerField()