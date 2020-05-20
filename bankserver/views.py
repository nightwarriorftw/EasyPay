from django.shortcuts import render
from .models import UserModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def UpdateUserBalance(request):
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        upi_key = request.POST.get('upi_key')
        PIN = request.POST.get('PIN')
        amount = request.POST.get('amount')
        amount = float(amount)
        print(full_name, upi_key, PIN, amount)
        obj = UserModel.objects.filter(
            full_name = full_name,
            upi_key = upi_key,
            PIN = PIN
        )
        obj = obj[0]
        if obj is not None:
             
             if(obj.balance >= amount):
                obj.balance = obj.balance-amount
                obj.save()
                print(obj.balance)
                return JsonResponse({'detail':'success'})
        else:
            return JsonResponse({'detail': 'InvalidCredentials'})
    else:
        return JsonResponse({'details': 'Invalid Request'})
