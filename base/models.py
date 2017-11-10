# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Investment(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    recurring_ammount = models.DecimalField(max_digits=8, decimal_places=4)
    total_investment = models.DecimalField(max_digits=8, decimal_places=4)
    current_value = models.DecimalField(max_digits=8, decimal_places=4)
    profit = models.DecimalField(max_digits=8, decimal_places=4)
    status = models.CharField(max_length=50)
    class Meta:
        db_table ="investments"
