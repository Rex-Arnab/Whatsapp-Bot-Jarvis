#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import requests
import json
from bs4 import BeautifulSoup


class LearnView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("learn (?P<course>[^$]+)$", self.learn1),
            ("^(?P<learn>learn)$", self.learn),

        ]

    def learn1(self, message=None, match=None, to=None):
        c = match.group("course")
        if c == "python":
            txt = "Python Lessons Comming Soon"
        elif c == "html":
            txt = "HTML Lessons Comming Soon"
        elif c == "php":
            txt = "PHP Lessons Comming Soon"
        else:
            txt = c+" Lessons Comming Soon"
        return TextMessageProtocolEntity(txt , to=message.getFrom())

    def learn(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP , to=message.getFrom())




HELP = """
Welcome to Learn Zone.

Python
HTML
CSS
JAVASCRIPT
PHP
MySql
Upcomming...

[learn <course>
"""
