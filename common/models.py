# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MutualFund(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    NAV =  models.DecimalField(max_digits=8, decimal_places=4)
    category = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    dt_update = models.DateField()


    class Meta:
        db_table ="MutualFunds"
        unique_together = ('code', 'name', 'family')


