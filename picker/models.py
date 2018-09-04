import uuid
from enum import Enum

from django.db import models
from django.db.models.options import Options


#  Abstract Models
class UUIDStandardPrimaryKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: Add PostgreSQL uuid_generate_v1() ext. 

    class Meta:
        abstract = True


class EntryActionTime(models.Model):
    dt_add = models.DateTimeField()
    dt_update = models.DateTimeField(default=None)

    class Meta:
        abstract = True


class EntityEnable(models.Model):
    enable = models.BooleanField(default=True)

    class Meta:
        abstract = True


# Models
class Currency(UUIDStandardPrimaryKey, EntityEnable, EntryActionTime):
    name = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100, unique=True)
    verification = models.BooleanField(default=False)


class CurrencyPair(UUIDStandardPrimaryKey, EntityEnable, EntryActionTime):
    base = models.ForeignKey(Currency, 
                             on_delete=models.CASCADE, 
                             related_name='base_in_pairs',
                             related_query_name='base_in_pair')
    quoted = models.ForeignKey(Currency, 
                               on_delete=models.CASCADE, 
                               related_name='quoted_in_pairs',
                               related_query_name='quoted_in_pair')
    verification = models.BooleanField(default=False)

    class Meta:
        unique_together = ('base', 'quoted')


# Exchanges Model
class Exchange(UUIDStandardPrimaryKey, EntityEnable, EntryActionTime):
    separator = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    fee = models.FloatField()


class MarketStatuses(Enum):
    VN = 'verification' 
    PG = 'pending'
    MN = 'maintenance'
    AC = 'active'


class ExchangeMarket(UUIDStandardPrimaryKey, EntityEnable, EntryActionTime):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    currency_pair = models.ForeignKey(CurrencyPair, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=2,
                              choices=((tag, tag.value) for tag in MarketStatuses),
                              default=MarketStatuses.VN)

    class Meta:
        unique_together = ('exchange', 'currency_pair')
