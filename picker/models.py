from django.db import models

# Create your models here.
class Exchange(models.Model):
    name = models.CharField(max_length=100)
    separator = models.CharField(max_length=1)


class CurrencyPair(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    base = models.CharField(max_length=10)
    quoted = models.CharField(max_length=10)


class FinancialQuote(models.Model):
    pair = models.ForeignKey(CurrencyPair)
