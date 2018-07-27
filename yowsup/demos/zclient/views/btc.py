#!/usr/local/bin/python
# coding: latin-1
import requests
from bs4 import BeautifulSoup
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
from forex_python.bitcoin import BtcConverter

class BtcViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
	#self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
	    ("^btc_help$", self.btc_help),
            ("btc (?P<address>[^$]+)$", self.balance),
	    ("txd (?P<txdaddress>[^$]+)$", self.txdid),
	    ("rates (?P<currency>[^$]+)$", self.getprice),
	    ("exchange (?P<amount>[^$]+)$", self.getexchange)
        ]


    def btc_help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(btc_HELP_TEXT, to=message.getFrom())

    def getexchange(self, message=None, match=None, to=None):
        amount = match.group("amount")
        price = BtcConverter()
        return TextMessageProtocolEntity(amount+" INR = "+str(price.convert_to_btc(int(amount),'BTC'))+" INR", to=message.getFrom())

    def getprice(self, message=None, match=None, to=None, currency="INR"):
        currency = match.group("currency").upper()
        if "RUPEES" in currency:
            currency = "INR"
        price = BtcConverter()
        return TextMessageProtocolEntity("1BTC = "+str(price.get_latest_price(currency))+" "+currency, to=message.getFrom())
    
    def balance(self, message=None, match=None, to=None): 
        addr = match.group("address")
        if addr == "arnab":
            addr = "1NcFCtRTGtkhFiGTk7en8yWJK8wjtBuWad"
        elif addr == "arnab_2":
            addr = "1GuXnf7XyMnmE1vSFoPDQ7oJbehW4G3KgZ"
        elif addr == "alpesh":
            addr = "13Q3jM8fwznuV5WGCRJSwTGFzdjVYE8NnN"
        btc = {
            'txd' : '',
            'recived' : '',
            'final' : ''
            }
        total_btc = {
            'txd' : '',
            'recived' : '',
            'final' : ''
            }
        url = "https://blockchain.info/address/"+addr
        data = requests.get(url)
        data = data.text
        soup = BeautifulSoup((data), "lxml")

        btc['txd'] = soup.find("td", {"id": "n_transactions"})
        btc['recived'] = soup.find("td", {"id": "total_received"})
        btc['final'] = soup.find("td", {"id": "final_balance"})
        total_btc['txd'] = btc['txd'].get_text()
        total_btc['recived'] = btc['recived'].get_text()
        total_btc['final'] = btc['final'].get_text()

        url1 = 'blockchain.info/q/addressbalance/'+addr+'?confirmations=0'
        r = requests.get("https://" +url1)
        data1 = r.text
        soup1 = BeautifulSoup(data1, "lxml")
        soup1 = soup1.p.get_text()
        return TextMessageProtocolEntity("["+addr+"]\n\nYou have "+str(float(soup1)*0.00000001)+ " BTC.\n\nNo. Transactions : "+total_btc['txd']+"\nTotal Received : "+total_btc['recived']+"\nFinal Balance : "+total_btc['final'], to=message.getFrom())

    def txdid(self, message=None, match=None, to=None): 
        addr = match.group("txdaddress")
        url = 'blockchain.info/q/txtotalbtcoutput/'+addr
        r = requests.get("https://" +url)
        data = r.text
        soup = BeautifulSoup(data, "lxml")
        soup = soup.p.get_text()
        return TextMessageProtocolEntity("["+url+"]\n\nYou have "+str(float(soup)*0.00000001)+ " BTC.", to=message.getFrom())

btc_HELP_TEXT = """
 *btc_Help* - Show this message.
 *btc <address>* - Get Bitcoin Address Balance
 *txd <txdid>* - Get Transaction Balance
 *rates <currency in caps>* - get price
 *exchange <amount> <currency in caps>* - get price in btc

Donate me for Supportand
Programming if you like the bot
1GuXnf7XyMnmE1vSFoPDQ7oJbehW4G3KgZ"""
