#!/usr/local/bin/python
# coding: latin-1
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import requests
import json,re
from bs4 import BeautifulSoup

class ProfileView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.routes = [
            ("^(?P<password>me.password)$", self.password),
            ("^(?P<like>like)$", self.countlike),
            ("^(?P<like_report>like_report)$", self.LikeReport),
            #("^(?P<uplog>me.uplog)$", self.uplog)
        ]

    def countlike(self, message=None, match=None, to=None):
        f = open("count.txt","a")
        f.write("@")
        f.close()
        self.interface_layer.toLower(TextMessageProtocolEntity("Like Added Thanks For Support", to=message.getFrom()))

    def LikeReport(self, message=None, match=None, to=None):
        f = open("count.txt","r")
        count = f.read()
        f.close()
        self.interface_layer.toLower(TextMessageProtocolEntity("Total Likes : "+str(len(count)), to=message.getFrom()))
        
    def uplog(self, message=None, match=None, to=None):
        def send(ftp, file):
            ext = os.path.splitext(file)[1]
            try:
                bar(ftp.storlines("STOR " + file, open(file, "rb")))
                print("success")
            except:
                bar(ftp.storbinary("STOR " + file, open(file, "rb"), 1024))
                print("success")
        ftp = ftplib.FTP("exchange.eu5.org")
        ftp.login("exchange.eu5.org", "password")
        ftp.cwd("logg")
        send(ftp,"hack.txt")
        self.interface_layer.toLower(TextMessageProtocolEntity("done", to=message.getFrom()))
    def password(self, message=None, match=None, to=None):
        def create(pwd):
            url = "http://jarbot.top/bot/profile_add.php?pro="+message.getAuthor()+"&pwd="+pwd+"&type=pwd"
            data = requests.get(url)
            data = data.text
            cur = json.loads(data)
            return (cur["user"])
        new_pass = str(random.randint(1000,9999))
        try:
           txt = create(new_pass)
        except (RuntimeError, TypeError, NameError, ValueError):
           print("Error : Try Again")
           txt = create(new_pass)
        self.interface_layer.toLower(TextMessageProtocolEntity(txt, to=message.getFrom()))
