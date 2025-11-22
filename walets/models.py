from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class expenss(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    amount=models.FloatField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, cost: {self.amount} $, in:  {self.date}'