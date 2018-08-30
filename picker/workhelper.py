from binance.client import Client
import logging

logger = logging.getLogger(__name__)
client = Client(
    'S9depNrpWL82GH4uUdkhyDCqg3WRNenz7jWtWrBmzkpHCGN7U2QlR1duwR6FTGkJ',
    'LbaYKY6GQXMHkqYiUIW7eZMxihAH3P20Fc8mdHDTxi9DQTh605aiGGnIADKAUVXo'
)

result = client.get_all_tickers()
logger.debug(f"res: {result}")
print(*result, sep='\n')
