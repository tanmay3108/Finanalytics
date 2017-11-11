# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from base.models import *
from base.manager import *

from django.test import TestCase

# Create your tests here.

class CRUD():
    @staticmethod
    def insert():
        record_dict ={'folio':'91026689363',
                     'name':'Axis Long Term Equitry Fund Growth',
                     'type':'SIP',
                     'recurring_ammount':500,
                     'total_investment':0,
                     'current_value':0,
                     'profit':0,
                     'status':'Running'}
        InvestmentHelper.insert(record_dict)





