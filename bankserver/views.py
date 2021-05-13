from django.shortcuts import render
from .models import UserModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json, os

from twilio.rest import Client

@csrf_exempt
def UpdateUserBalance(full_name, upi_key, PIN, amount, image=None):
        # full_name = request.POST.get('full_name')
        # upi_key = request.POST.get('upi_key')
        # PIN = request.POST.get('PIN')
        # amount = request.POST.get('amount')
        amount = float(amount)
        obj = UserModel.objects.filter(
            full_name = full_name,
            upi_key = upi_key,
            PIN = PIN
        )
        try:
            obj = obj[0]
        except:
            return {'details': 'Invalid Credentials', 'status': 400}

        if obj is not None:
             
             if(obj.balance >= amount):
                obj.balance = obj.balance-amount
                obj.save()
                print(obj.balance)
                client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
                smsBody = "{name} your account has been debited by Rs {amount} after placing an order from Sbi-EasyPay".format(name=full_name, amount=amount)
                smsPhone = "+{}{}".format(obj.phone_number.country_code,
                                          obj.phone_number.national_number)
                print(smsBody)
                try:
                    smsMessage = client.messages \
                        .create(
                            body=smsBody,
                            from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                            to=smsPhone
                        )
                    print(smsMessage.sid)
                    print('SMS send')

                except:
                    print('SMS send failed')
                return {'detail':'success', 'status': 200}
        else:
            return {'detail': 'InvalidCredentials', 'status': 400}
