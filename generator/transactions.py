"""Utilities to model money transactions."""

from random import choices, randint,choice
from string import ascii_letters, digits
import requests
account_chars: str = digits + ascii_letters
import json
import os

def _random_account_id() -> str:
    """Return a random account number made of 12 characters."""
    return ''.join(choices(account_chars, k=12))


def _random_amount() -> float:
    """Return a random amount between 10.00 and 100.00."""
    return int(randint(1000, 10000) / 100)


def create_random_transaction() -> dict:
    """Create a fake, randomised transaction."""
    #myobj = {'somekey': 'somevalue'}
    side = choice(["buy", "sell"])
    pair = choice(["BTC/USD","ETH/USD","XRP/USD"])
    quantity= str(_random_amount())
    price= str(_random_amount())
    #headers = {'Host':'crypto.localhost','Content-Type':'application/json'}
    headers = {'Content-Type':'application/json'}
    
    data_obj={'side':side,'quantity':quantity,'price':price,'pair':pair}
    data=json.dumps(data_obj, separators=(',', ':'))

    #url= 'http://crypto:5000/order/new'
    url=  os.environ.get('ORDER_BOOK_URL')
    #print(data)
    #x = requests.post(url, data = data, headers=headers)
    return data_obj
    """return {
        'source': _random_account_id(),
        'target': _random_account_id(),
        'amount': _random_amount(),
        # Keep it simple: it's all euros
        'currency': 'EUR',
    }"""

