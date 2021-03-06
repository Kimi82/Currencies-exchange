import requests
from datetime import date
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def checkConnection():
    response = requests.get("https://api.exchangeratesapi.io/")
    if response.status_code == 200:
        status = True
    else:
        status = False
    return status


availableCurrencies = "PLN ,CAD, HKD, ISK, PHP, DKK, HUF, CZK, GBP, RON, SEK, IDR, INR, BRL, RUB, HRK,\n JPY, THB, CHF, EUR, MYR, BGN, TRY, CNY, NOK, NZD, USD, MXN, SGD, AUD, ILS, KRW"
baseCurrencies = input("Available currencies:\n %s.\nChoose your base: " % availableCurrencies)
baseCurrencies = baseCurrencies.upper()
currencies = input("Wybierz waluty do pokazania, wpisz je po spcji: ")
currencies = currencies.upper().split(" ")  # list


def getCurrentCurrencies(baseCurrencies, currencies):
    newCurrencies = None
    if len(currencies) > 1:
        newCurrencies = ','.join(currencies)
    else:
        newCurrencies = ''.join(currencies)

    baseCurrenciesResponse = requests.get(
        'https://api.exchangeratesapi.io/latest?base=' + baseCurrencies + '&symbols=' + newCurrencies)

    data = baseCurrenciesResponse.json()
    # print(data)
    date = data['date']
    currenciesToArray = data['rates']
    keyArray = list(currenciesToArray.keys())
    currenciesArray = list(currenciesToArray.values())
    finalResult = dict(zip(keyArray, currenciesArray))
    finalResult.update(date=date)
    print(finalResult)
    return currencies, baseCurrencies, baseCurrenciesResponse, date, finalResult


def getHistoricalCurrencies(baseCurrencies, currencies):
    begin = input("Enter the start date in USA notation(YYYY-MM-DD): ")
    end = input("Enter end date or don't write anythink to use today date: ")
    if (end or len(end) <= 1):
        end = str(date.today())

    newCurrencies = None
    if len(currencies) > 1:
        newCurrencies = ','.join(currencies)
    else:
        newCurrencies = ''.join(currencies)

    baseCurrenciesResponse = requests.get(
        'https://api.exchangeratesapi.io/history?start_at=' + begin + '&end_at=' + end + '&base=' + baseCurrencies + '&symbols=' + newCurrencies)
    baseCurrenciesResponse = baseCurrenciesResponse.json()

    ordered_dict = dict(OrderedDict(sorted(baseCurrenciesResponse['rates'].items(), key=lambda t: t[0])))
    #print(ordered_dict) # sorted

    datesArray = []

    for dates in ordered_dict.keys():
        datesArray.append(dates)
    #currenciesArray = list(ordered_dict[datesArray[0]].keys())
    #print(datesArray)

    #print(ordered_dict[datesArray[0]].values())  #1/ordered_dict[datesArray[i]][currenciesArray[y]]

    i=0
    while i<len(datesArray):
        ordered_dict[datesArray[i]].update((x, 1 / y) for x, y in ordered_dict[datesArray[i]].items())

        i+=1
    print(ordered_dict)
#getCurrentCurrencies(baseCurrencies, currencies)
getHistoricalCurrencies(baseCurrencies,currencies)

#sns.set(style="whitegrid")


#plt.show()
