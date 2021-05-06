
# Create your models here.
from django.db import models

class Company(models.Model):
    # 企业名称
    name = models.CharField(max_length=200)

    # 企业经营范围
    scope = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    #企业类型
    kind = models.CharField(max_length=200)