from common.models import *




class MutualFundHelper():
    @staticmethod
    def insert(record_dict):
        record = MutualFund(
        code=record_dict['Scheme Code'],
        name = record_dict['Scheme Name'],
        NAV = record_dict['Net Asset Value'],
        category = record_dict['Scheme Category'],
        family = record_dict['Fund Family'],
        dt_update = record_dict['Date']

        )
        record.save()