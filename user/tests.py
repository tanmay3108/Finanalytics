# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user.models import *
from user.manager import *
from datetime import datetime,timedelta

from django.test import TestCase

# Create your tests here.

class CRUD():
    @staticmethod
    def insert():
        date = datetime.strptime('16/10/20','%y/%m/%d')
        record_dict ={'folio':'91026689363',
                     'name':'Axis Long Term Equitry Fund Growth',
                     'type':'SIP',
                     'recurring_ammount':500,
                     'total_investment':9500,
                     'current_value':0,
                     'profit':0,
                     'status':'Running',
                     'start_date':date,
                     'number_of_units':273.309}
        InvestmentHelper.insert(record_dict)
    @staticmethod
    def update():
        InvestmentHelper.update_units(folio_id='91026689363',units=273.309)






