# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from binance.client import Client


client = Client(
    'S9depNrpWL82GH4uUdkhyDCqg3WRNenz7jWtWrBmzkpHCGN7U2QlR1duwR6FTGkJ',
    'LbaYKY6GQXMHkqYiUIW7eZMxihAH3P20Fc8mdHDTxi9DQTh605aiGGnIADKAUVXo'
)


@shared_task
def binance_blc():
    return client.get_asset_balance('BTC')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
