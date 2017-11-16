#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import sys
import pymysql

class FunViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.routes = [
	    ("^fun$", self.f_help),
	    ("^Ask (?P<question>[^$]+)$", self.ask),
	    ("^ask (?P<question>[^$]+)$", self.ask)
            ]

    def f_help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(F_HELP_TEXT, to=message.getFrom())

    def ask(self, message=None, match=None, to=None):
        q = match.group("question").lower()
        q = "Under Development"
        return TextMessageProtocolEntity(q, to=message.getFrom())

F_HELP_TEXT = """ [FUN]
 *fun* - Show this message.
 Take (even)/(odd)
 ping - pong.
 echo - echo.
 roll - roll a dice."""
