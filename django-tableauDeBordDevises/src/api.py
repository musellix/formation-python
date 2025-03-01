from datetime import date, timedelta
from pprint import pprint

import requests

def get_rates(currencies: list[str], days: int=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ",".join(currencies)
    exchange_rate_api = f'https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}'
    r = requests.get(exchange_rate_api)
    if not r and not r.json():
        return False, False     # cette methode retourne deux valeurs

    api_rates = r.json().get("rates")

    # rate = taux
    all_rates = {currency: [] for currency in currencies}   # {'CAD': [], 'USD': []}
    all_days = sorted(api_rates.keys())        # ex : ['2025-01-24', ...]
    pprint(all_days)

    for each_days in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_days].items() ]
    pprint(all_rates)

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"] )