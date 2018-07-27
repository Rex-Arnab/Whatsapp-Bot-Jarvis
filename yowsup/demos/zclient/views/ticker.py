#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import requests,json
from bs4 import BeautifulSoup
from yowsup.demos.zclient.views.package import cryptopia,zebpay

class TickerViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^ticker$", self.help),
            ("yobit (?P<currency>[^$]+)$", self.yobit),
            ("polo (?P<currency>[^$]+)$", self.polo),
            ("cryptopia (?P<currency>[^$]+)$", self.cryptopia),
            ("bittrex (?P<currency>[^$]+)$", self.bittrex),
            ("zebpay (?P<currency>[^$]+)$", self.zebpay),
            ("bitcointalk (?P<uid>[^$]+)$", self.btctalk)
        ]

    def cryptopia(self, message=None, match=None, to=None):
        text = match.group("currency")
        result = cryptopia.get(text)
        return TextMessageProtocolEntity(result, to=message.getFrom())
    
    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(ticker_help, to=message.getFrom())
		
    def btctalk(self, message=None, match=None, to=None):
        s = requests.session()
        id = match.group("uid")
        url = "https://bitcointalk.org/index.php?action=profile;u="+id
        data = requests.get(url)
        data = data.text
        soup = BeautifulSoup((data), "lxml")
        for name in soup.find_all("td", class_="windowbg"):
            salary = name.parent.find_all('td')[-1]  # last cell in the row
            return TextMessageProtocolEntity(id+" Details :-\n"+name.get_text(), to=message.getFrom())

    def yobit(self, message=None, match=None, to=None):
        s = requests.session()
        convert = match.group("currency")
        url = "https://yobit.net/api/2/"+convert+"/ticker"
        data = requests.get(url)
        data = data.text
        cur = json.loads(data)
        last = cur["ticker"]["last"]
        high = cur["ticker"]["high"]
        low = cur["ticker"]["low"]
        avg = cur["ticker"]["avg"]
        vol = cur["ticker"]["vol"]
        vol_cur = cur["ticker"]["vol_cur"]
        buy = cur["ticker"]["buy"]
        sell = cur["ticker"]["sell"]
        updated = cur["ticker"]["updated"] 
        return TextMessageProtocolEntity("Price("+convert+")\n\nCurrent Price:"+format(last, '.8f')+"\n\nHigh : "+format(high, '.8f')+"\nLow : "+format(low, '.8f')+"\nAvg : "+format(avg, '.8f')+"\nVol : "+format(vol, '.8f')+"\nCurrent Vol : "+format(vol_cur, '.8f')+"\nBuy : "+format(buy, '.8f')+"\nSell : "+format(sell, '.8f')+"\nupdated : "+str(updated), to=message.getFrom())
    def polo(self, message=None, match=None, to=None):
        s = requests.session()
        convert = match.group("currency").upper()
        url = "https://www.poloniex.com/public?command=returnTicker&currencyPair="+convert.upper()
        data = requests.get(url)
        data = data.text

        cur = json.loads(data)
        rate = cur[convert.upper()]["last"]
        return TextMessageProtocolEntity("Price("+convert+") :"+rate, to=message.getFrom())

    def zebpay(self, message=None, match=None, to=None):
        text = match.group("currency")
        result = zebpay.get(text)
        return TextMessageProtocolEntity(result, to=message.getFrom())
    
    def bittrex(self, message=None, match=None, to=None):
        convert = match.group("currency")
        url = "https://bittrex.com/api/v1.1/public/getmarketsummary?market="+convert
        data = requests.get(url)
        data = data.text
        cur = json.loads(data)
        q = ""
        q += "Market Name : "+str(cur["result"][0]["MarketName"])+"\n"
        q += "Low : "+str(cur["result"][0]["Low"])+"\n"
        q += "High : "+str(cur["result"][0]["High"])+"\n"
        q += "Volume : "+str(cur["result"][0]["Volume"])+"\n"
        q += "Last : "+str(cur["result"][0]["Last"])+"\n"
        q += "BaseVolume : "+str(cur["result"][0]["BaseVolume"])+"\n"
        q += "Bid : "+str(cur["result"][0]["Bid"])+"\n"
        q += "Ask : "+str(cur["result"][0]["Ask"])+"\n"
        q += "OpenSellOrders : "+str(cur["result"][0]["OpenSellOrders"])+"\n"
        q += "OpenBuyOrders : "+str(cur["result"][0]["OpenBuyOrders"])+"\n"
        return TextMessageProtocolEntity(q, to=message.getFrom())



ticker_help = """[ticker menu]

yobit <currency pair> - yobit.net
example - yobit ltc_btc

polo <currency pair> - poloniex.com
example - polo btc_ltc

bittrex<currency pair> - bittrex.com
example - bittrex btc-eth

cryptopia<currency pair> - cryptopia.co.nz
Example - cryptopia btc-eth

Zebpay <currency pair> - Zebpay.com
Example - zebpay btc-inr

bitcointalk <uuid> - bitcointalk.org
example - bitcointalk 555318"""
