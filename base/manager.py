from base.models import *


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
                            status=record_dict['status']
                            )
        record.save()
