# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from user.manager import User ,InvestmentHelper
from django.core.serializers import serialize
from django.http import JsonResponse
from rest_framework.request import Request
from django.shortcuts import render


from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def investment_detail(request, user_id=None):
    error=""
    message =0
    result = User.get_user_investments()

    return render(
        request,
        'index.html',
        context={'title': "Funds Details", 'investment_detail': result},
    )



    #return Response(result)
    #return HttpResponse(result, content_type='application/json')
    #return Response(response)
    #return Response(response)
    # response = serialize('json', result)

@api_view(['PUT'])
def update_units(request,user_id,portfolio_id):
    status =200
    message =""
    data  = request.data
    units = data.get('units')
    currnet_value = data.get('currnet_value')
    try:
        if units != None:
            InvestmentHelper.update_units(folio_id=portfolio_id,units = units)
            status =200
            message ="Successfully updated units ",units
        elif currnet_value !=None:
            InvestmentHelper.update_current_value(folio_id=portfolio_id,current_value=currnet_value)
            print "updated current_value",currnet_value
    except:
        message ="updation failed"
        status =500

    return Response(message,status=status)



