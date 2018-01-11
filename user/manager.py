from user.models import *
import json


class InvestmentHelper():
    @staticmethod
    def insert(record_dict):
        record = Investment(
                            folio=record_dict['folio'],
                            name=record_dict['name'],
                            type=record_dict['type'],
                            recurring_ammount=record_dict['recurring_ammount'],
                            total_investment=record_dict['total_investment'],
                            current_value=record_dict['current_value'],
                            profit=record_dict['profit'],
                            status=record_dict['status'],
                            start_date=record_dict['start_date'],
                            number_of_units = record_dict['number_of_units']

                            )
        record.save()

    @staticmethod
    def get(user_id = None):
        if(user_id == None):
            return Investment.objects.all()


    @staticmethod
    def update_units(folio_id, units, user_id=None):
        Investment.objects.filter(folio=folio_id).update(units=units)

    @staticmethod
    def update_current_value(folio_id, current_value, user_id=None):
        Investment.objects.filter(folio=folio_id).update(current_value=current_value)


class User():

    @staticmethod
    def get_user_investments(user_id =None):
        list_dict =[]
        list_query_obj = InvestmentHelper.get()
        for i in range(len(list_query_obj)):
            record ={}
            record['name'] = list_query_obj[i].name
            record['type'] = list_query_obj[i].type
            record['recurring_ammount'] = list_query_obj[i].recurring_ammount
            record['total_investment'] = list_query_obj[i].total_investment
            record['start_date'] = list_query_obj[i].start_date
            record['units'] = list_query_obj[i].units
            list_dict.append(record)
        return list_dict







