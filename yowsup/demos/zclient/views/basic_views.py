#!/usr/local/bin/python
# coding: latin-1
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import random

class BasicViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [("(?P<hiOrHello>hi|hello|hey|hay|Hi|Hello)", self.hi),
              ("^ping$", self.ping),
              ("^faq$", self.faq),
              ("^e(cho)?\s(?P<echo_message>[^$]+)$", self.echo)]
       
    def echo(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("%s" % match.group("echo_message"), to=message.getFrom())

    def ping(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Pong!", to=message.getFrom())

    def faq(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(faq, to=message.getFrom())

    def hi(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Hello" , to=message.getFrom())



faq = """
Have a Nice Day
This is the Faq Section"""
