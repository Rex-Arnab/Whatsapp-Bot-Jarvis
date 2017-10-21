#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import sys
import pymysql
#from weather import Weather
#import wikipedia

#conn = pymysql.connect(host='sql8.freesqldatabase.com',user='sql8175527',password='rgwgSlBExZ',db='sql8175527')
#a = conn.cursor()

class FunViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
	#self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
	    ("^fun$", self.f_help),
	    ("^Ask (?P<question>[^$]+)$", self.ask),
	    ("^ask (?P<question>[^$]+)$", self.ask),
	    #("^weather (?P<place>[^$]+)$", self.weather),
	    #("^wiki (?P<word>[^$]+)$", self.wiki),
	    #("^Wiki (?P<word>[^$]+)$", self.wiki),
        ]

    #def wiki(self, message=None, match=None, to=None):
	#    wikipedia.set_lang("en")
	#    content = wikipedia.summary(match.group("word")).lower()
    #    return TextMessageProtocolEntity(content, to=message.getFrom())

    def f_help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(F_HELP_TEXT, to=message.getFrom())

    #def weather(self, message=None, match=None, to=None):
	#    place = match.group("place").lower()
	#    weather = Weather()
	#    location = weather.lookup_by_location(place)
	#    condition = location.condition()
	#    return TextMessageProtocolEntity("Weather : "+condition['text'], to=message.getFrom())

    def ask(self, message=None, match=None, to=None):
        #file = open('questions.txt','r')
        #d = {}
        #run = "y"
        #for line in file:
        #    x = line.split(":")
        #    a = x[0]
        #    b = x[1]
        #    d[a] = b
        q = match.group("question").lower()
        #if (q in d) == True:
        #    q = d[q]
        #else:	
            #file = open('yowsup/demos/zclient/views/questions.txt','a')
            #file.write("\n"+q+":Pending question")
        #sql = 'INSERT INTO test (msg) value ('+q+');'
        #a.execute(sql)
        #print("Question ("+q+") Added!!")
            #file.close()
        #q = "Question Added!!. Thank You"
        q = "Under Development"
        return TextMessageProtocolEntity(q, to=message.getFrom())

F_HELP_TEXT = """ [FUN]
 *fun* - Show this message.
 Take (even)/(odd)
 ping - pong.
 echo - echo.
 roll - roll a dice."""
