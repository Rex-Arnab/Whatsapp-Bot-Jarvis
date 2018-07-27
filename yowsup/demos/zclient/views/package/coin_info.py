import requests,json

def market():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=demo"
    data = requests.get(url)
    data = data.text
    data = json.loads(data)
    main = data["Meta Data"]
    for i in main:
        print(i+" : "+main[i])
def crypto():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo"
    data = requests.get(url)
    data = data.text
    data = json.loads(data)
    rate = {}
    main = data["Realtime Currency Exchange Rate"]
    q = ""
    for i in main:
        q += i+" : "+main[i]+"\n"
    print(q)
