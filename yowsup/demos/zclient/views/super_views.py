#!/usr/local/bin/python
#from media_sender import UrlPrintSender
import time,calendar
from datetime import datetime
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import requests
import json
import pytz
from yowsup.demos.zclient.views.include import get
class SuperViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^(?P<helpOrjarvis>help|jarvis)$", self.help),
            ("^help1$", self.help1),
            ("^help2$", self.help2),
            ("^about$", self.about),
            #("^(?P<youtube>youtube)$", self.youtube),
            ("^(?P<py1>py1)$", self.py1),
            ("^(?P<py2>py2)$", self.py2),
            ("^(?P<fms>fms)$", self.fms),
            ("^roll$", self.roll),
	    ("^link$", self.link),
	    ("^(?P<time>Time|time)$", self.time),
	    ("(?P<calender>calender)$", self.calender),
	    ("^(?P<goodnightOrgdni8>good night|gdni8|ni8|gdnit)", self.gdnit),
	    ("(?P<btcOrbitcoin>btc|bitcoin)$", self.btc),
            ("take (?P<evenOrOdd>even|odd) (?P<bal>[^$]+)$", self.even_or_odd),

            
        ]

    def time(self, message=None, match=None, to=None):
        #localtime = time.asctime(time.localtime(time.time()))
        localtime = pytz.timezone('Asia/Kolkata')
        return TextMessageProtocolEntity("Local current time :"+ str(localtime.strftime(fmt)), to=message.getFrom())

    def calender(self, message=None, match=None, to=None):
        now = datetime.now()
        cal = str(calendar.month(now.year,now.month))
        return TextMessageProtocolEntity("Here is the calendar:\n"+str(now)+"\n"+cal, to=message.getFrom())

    def about(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("about"), to=message.getFrom())

    def youtube(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("y_menu"), to=message.getFrom())

    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 6), to=message.getFrom())

    def even_or_odd(self, message=None, match=None, to=None):
        me = message.getAuthor()
        url = "http://www.mcetbhb.top/profile__show.php?pro="+me+"&balance=true"
        try:
            try:
                data = requests.get(url)
            except:
                data = requests.get(url)
        except:
            try:
                data = requests.get(url)
            except:
                data = requests.get(url)
        data = data.text
        cur = json.loads(data)
        bal = cur["user"]["balance"]
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 100)
        add = match.group("bal")
        if "-" in add:
            return TextMessageProtocolEntity("You are a Duck", to=message.getFrom())
        elif int(bal) > int(add):
            if (is_odd and num % 2) or (not is_odd and not num % 2):
                url = "http://exchange.eu5.org/bot/profile_add.php?pro="+me+"&addpoint="+str(add)+"&type=add"
                data = requests.get(url)
                return TextMessageProtocolEntity("["+str(num)+"]\nYou win "+str(add)+" Points.", to=message.getFrom())
            else:
                url = "http://exchange.eu5.org/bot/profile_add.php?pro="+me+"&subpoint="+str(add)+"&type=sub"
                data = requests.get(url)
                return TextMessageProtocolEntity("["+str(num)+"]\nYou lose "+str(add)+" Points.", to=message.getFrom())           
        else:
            return TextMessageProtocolEntity("Invalid bet", to=message.getFrom())

    def help(self, message=None, match=None, to=None):
        try:
            return TextMessageProtocolEntity(HOME, to=message.getFrom())
        except:
            return TextMessageProtocolEntity(HOME, to=message.getFrom())
        
    def help1(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("home1"), to=message.getFrom())

    def help2(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("home2"), to=message.getFrom())

    def gdnit(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Good Night!!", to=message.getFrom())

    def btc(self, message=None, match=None, to=None):
        url = "http://exchange.eu5.org/bot/bot/page.php?page=btc"
        try:
            data = requests.get(url)
        except:
            data = requests.get(url)
        data = data.text
        cur = json.loads(data)
        try:
            name = cur['page'][0]['text']
        except:
            name = cur['page']['text']
        return TextMessageProtocolEntity(name, to=message.getFrom())

    def link(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("link"), to=message.getFrom())

    def py1(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("python1"), to=message.getFrom())

    def py2(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("python2"), to=message.getFrom())

    def fms(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("fms"), to=message.getFrom())

HOME = """
1. joke = Get Fresh New Joke
2. pmu <text> = Permutation
3. loop <number> <text> = FOR LOOP
4. /img <name> <img_no> = image downloader
5. <programming_language_name> = Programming Language Doc
6. wiki <search_term> = WikiPedia
7. weather <place_name> = Weather
8. Quiz = Fun Quize
9. fact <no> = factorial
10. echo <text> = echo bot

"""
