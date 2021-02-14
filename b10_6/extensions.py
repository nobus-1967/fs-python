import requests
import json

KEYS = {'рубль': 'RUB',
        'евро': 'USD',
        'доллар': 'EUR',
        'юань': 'CNY',
        'иена': 'JPY',
        'вона': 'KRW',
        'фунт': 'GBP',
        'франк': 'CHF',
        'крона': 'CZK',
        'рупия': 'INR',
        'лира': 'TRY',
        'шекель': 'ILS',
        'рэнд': 'ZAR'}

class APIException(Exception):
    pass

class ExchangeCurrencies:
    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> str:
        try:
            base = KEYS[base]
            quote = KEYS[quote]
            int_amount = int(amount)
            if base == quote:
                raise APIException('Нельзя конвертировать одну и ту же валюту!')
        except APIException as e:
            return f'{e}'
        except KeyError:
            return 'Такая валюта в списке доступных отсутствует!'
        except ValueError:
            return 'Количество первой валюты: цифрами целое число больше 0!'
        else:                
            if base == 'EUR':
                cur_info = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={quote}')
            else:
                cur_info = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}&symbols={quote},{base}')
            cur_rate = json.loads(cur_info.content)['rates']
            sum = cur_rate[quote] * int_amount
        
        return f'{sum: .2f}' 
