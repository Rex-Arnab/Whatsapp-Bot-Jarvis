#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
import time,calendar
from datetime import datetime
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^(?P<helpOrjarvis>help|jarvis|Help|Jarvis)$", self.help),
            ("^(?P<about>About|about)$", self.about),
            ("^(?P<roll>Roll|roll|dice|Dice)$", self.roll),
	    ("^(?P<link>link|Link)$", self.link),
	    ("^(?P<time>Time|time)$", self.time),
	    ("(?P<calcOrcalender>cal|calender|Cal|Calender)$", self.cal),
	    ("^(?P<goodnightOrgdni8>good night|gdni8|ni8|gdnit)", self.gdnit),
	    ("(?P<btcOrbitcoin>btc|bitcoin|Btc|Bitcoin)$", self.btc),
            ("Take (?P<evenOrOdd>even|odd)$", self.even_or_odd),
        ]

    def time(self, message=None, match=None, to=None):
        localtime = time.asctime(time.localtime(time.time()))
        return TextMessageProtocolEntity("Local current time :"+ str(localtime), to=message.getFrom())

    def cal(self, message=None, match=None, to=None):
        now = str(datetime.now())
        cal = calendar.month(2017,6)
        return TextMessageProtocolEntity("Here is the calendar:\n"+now+"\n"+cal, to=message.getFrom())

    def about(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(ABOUT_TEXT, to=message.getFrom())

    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 6), to=message.getFrom())

    def even_or_odd(self, message=None, match=None, to=None):
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 100)
        if (is_odd and num % 2) or (not is_odd and not num % 2):
            return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())

    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())
    def gdnit(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Good Night!! ðŸ™‚", to=message.getFrom())

    def btc(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC_TEXT, to=message.getFrom())

    def link(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(LINK_TEXT, to=message.getFrom())

HELP_TEXT = """ [Commands]

p_help - info about progamming.

download - Download Menu

[NEW] program - Program Menu
btc_help - Bitcoin Menu

fun - Play games have fun.

btc - Information About Bitcoin.

link -  Available shared links.

ask- To ask Jarvis Questions(disable)

help - Show this message.

about - About

Donate me for Supportand
Programming if you like the bot
1GuXnf7XyMnmE1vSFoPDQ7oJbehW4G3KgZ
"""


ABOUT_TEXT = """ Hello i am Arnab the creator of this small bot.
I have a Dream to make my own jarvis.
HOpe i Can Make it. :)
>>> http://exchange.eu5.org <<<

Donate me for Supportand
Programming if you like the bot
1GuXnf7XyMnmE1vSFoPDQ7oJbehW4G3KgZ
"""
BTC_TEXT = """ Bitcoin uses peer-to-peer technology to operate
with no central authority or banks,
managing transactions and the issuing
of bitcoins is carried out collectively
by the network. Bitcoin is open-source.

its design is public, nobody owns or 
controls Bitcoin and everyone can take part.
Through many of its unique properties,

Bitcoin allows exciting uses that could 
not be covered by any previous payment system.

>>œ¨Steps to get started :-<<

0. Advantages - btc0
1. Disadvantages - btc1
2. Bitcoin Wallet - btc2
3. Earn Bitcoin - btc3
4. Bitcoin Exchange - btc4
5. Spend Bitcoin - btc5
6. Important Questions - faq
*Note Read FAQ*

List of All Crypto Currencies
http://coinmarketcap.com"""
LINK_TEXT = """
>>>> *Avalible Links* <<<<

1. *Koch* - http://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html
2. *Python Whatsapp Module* - https://github.com/tgalal/yowsup"""
