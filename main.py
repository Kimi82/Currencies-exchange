import requests

def checkConnection():
    response = requests.get("https://api.exchangeratesapi.io/")
    if response.status_code == 200:
        status = True
    else:
        status = False
    return status

def getCurrencies():
    availableCurrencies="PLN ,CAD, HKD, ISK, PHP, DKK, HUF, CZK, GBP, RON, SEK, IDR, INR, BRL, RUB, HRK,\n JPY, THB, CHF, EUR, MYR, BGN, TRY, CNY, NOK, NZD, USD, MXN, SGD, AUD, ILS, KRW"
    baseCurrencies = input("Available currencies:\n %s.\nChoose your base: " % availableCurrencies)
    baseCurrencies = baseCurrencies.upper()
    currencies = input("Wybierz waluty do pokazania, wpisz je po spcji: ")
    currencies = currencies.upper().split(" ") #list
    newCurrencies = None
    if len(currencies)>1:
        newCurrencies = ','.join(currencies)
    else:
        newCurrencies=''.join(currencies)

    baseCurrenciesResponse = requests.get('https://api.exchangeratesapi.io/latest?base='+baseCurrencies+'&symbols='+newCurrencies)


    data = baseCurrenciesResponse.json()
    print(data)
    date = data['date']
    waluta = []
    dupa = {}
    for i in currencies:
        interation = 0
        waluta.append(data['rates'][i])
        dupa.update({i: waluta[interation]})
        interation +=1
    print(dupa)
    return currencies, baseCurrencies, baseCurrenciesResponse, date

getCurrencies()




