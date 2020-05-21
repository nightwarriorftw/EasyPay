from django.db import models

class UserModel(models.Model):
    full_name = models.CharField(max_length=70)
    balance = models.FloatField(default=0.000)
    PIN = models.IntegerField(default='0700')
    upi_key = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name + self.upi_key

    def get_balance(self):
        return self.balance
