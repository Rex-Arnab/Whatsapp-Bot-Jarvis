#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import sys
import pymysql
from pyfiglet import figlet_format
from geopy.geocoders import Nominatim
import requests
import json
import forecastio
from yowsup.demos.zclient.utils.media_downloader import ImageSender
from yowsup.demos.zclient.views.include import get
from yowsup.demos.zclient.views.package.bounce import bounce
from yowsup.demos.zclient.views.package.story import story
from yowsup.demos.zclient.views.package.train import find
from yowsup.demos.zclient.views.package.joke import joke
from yowsup.demos.zclient.views.package.knotty import knotty
from yowsup.demos.zclient.views.package.arnab import arnab
from yowsup.demos.zclient.views.package.yt_jawed import yt_jawed
from yowsup.demos.zclient.views.package.wiki import wiki
from yowsup.demos.zclient.views.package.name import NameMagic
from yowsup.demos.zclient.views.package.permu import permu

#conn = pymysql.connect(host='sql8.freesqldatabase.com',user='sql8175527',password='rgwgSlBExZ',db='sql8175527')
#a = conn.cursor()

class FunViews():
    def __init__(self, interface_layer):
        self.image_sender = ImageSender(interface_layer)
        self.interface_layer = interface_layer
	#self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
	    ("^fun$", self.f_help),
            ("^tell story$", self.tell_story),
            ("^knotty$", self.knotty),
            ("^knotty (?P<num>[^$]+)$", self.knotty1),
             ("^yt_jawed$", self.yt_jawed),
            ("^yt_jawed (?P<num>[^$]+)$", self.yt_jawed1),
            ("^youtube$", self.arnab),
            ("^youtube (?P<num>[^$]+)$", self.arnab1),
            ("^story$", self.list_story),
            ("^comic$", self.list_comic),
            ("^joke$", self.joke),
            ("^find (?P<name>[^$]+)$", self.find_name),
            ("ascii (?P<term>[^$]+)$", self.aski),
            ("bounce (?P<height>[^$]+)$", self.bounce),
            ("train (?P<id>[^$]+)$", self.train),
	    #("^ask (?P<question>[^$]+)$", self.ask),
	    ("^weather (?P<place>[^$]+)$", self.weather),
	    ("^wiki (?P<word>[^$]+)$", self.wiki),
            ("^pmu (?P<word>[^$]+)$", self.permu),
        ]

    def wiki(self, message=None, match=None, to=None):
        term = match.group("word")
        content = wiki(term)
        return TextMessageProtocolEntity("WikiPedia\nSEARCH : *"+term+"*\n\n"+content , to=message.getFrom())

    def find_name(self, message=None, match=None, to=None):
        name = match.group("name")
        content = NameMagic(name)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def knotty(self, message=None, match=None, to=None):
        content,img = knotty()
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=img)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def yt_jawed(self, message=None, match=None, to=None):
        content,img = yt_jawed()
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=img)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def arnab(self, message=None, match=None, to=None):
        content,img = arnab()
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=img)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def permu(self, message=None, match=None, to=None):
        term = match.group("word")
        content = permu(term)
        return TextMessageProtocolEntity(content , to=message.getFrom())
    
    def arnab1(self, message=None, match=None, to=None):
        num = match.group("num")
        content = arnab(num)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def yt_jawed1(self, message=None, match=None, to=None):
        num = match.group("num")
        content = yt_jawed(num)
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def knotty1(self, message=None, match=None, to=None):
        num = match.group("num")
        content = knotty(num)
        return TextMessageProtocolEntity(content , to=message.getFrom())
    
    def train(self, message=None, match=None, to=None):
        text = match.group("id")
        train = find(text)
        return TextMessageProtocolEntity(train, to=message.getFrom())

    def tell_story(self, message=None, match=None, to=None):
        rstory = story()
        return TextMessageProtocolEntity(rstory, to=message.getFrom())
    
    def bounce(self, message=None, match=None, to=None):
        text = match.group("height")
        bounce = bounce(text)
        return TextMessageProtocolEntity(bounce, to=message.getFrom())
    
    def aski(self, message=None, match=None, to=None):
        text = match.group("term")
        aski = figlet_format(text)
        return TextMessageProtocolEntity(aski, to=message.getFrom())

    def joke(self, message=None, match=None, to=None):
        joke_text = joke()
        return TextMessageProtocolEntity(joke_text, to=message.getFrom())

    def list_story(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("story"), to=message.getFrom())

    def list_comic(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("comic"), to=message.getFrom())
    
    def f_help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("fun"), to=message.getFrom())

    def weather(self, message=None, match=None, to=None):
        place = match.group("place")
        locator = Nominatim()
        location = locator.geocode(place)
        lat=location.latitude
        lng=location.longitude
        api_key = "7e208df2f156ec0af788e8ec79a30df0"
        forecast = forecastio.load_forecast(api_key, lat, lng)
        byHour = forecast.hourly()
        self.interface_layer.toLower(TextMessageProtocolEntity(place + " Has The Following Weather", to=message.getFrom()))
        for hourlyData in byHour.data[0:3]:
            self.interface_layer.toLower(TextMessageProtocolEntity("temprature - "+str(hourlyData.temperature), to=message.getFrom()))
        return TextMessageProtocolEntity(byHour.summary, to=message.getFrom())

F_HELP_TEXT = """ [FUN]
 *fun* - Show this message.
 take (even)/(odd) [Bet Amount]
 ping - pong.
 echo - echo.
 roll - roll a dice.
 loop <round_number> <text> - For Loop"""
