#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
import time,calendar
from datetime import datetime
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
import requests
import json,re
from bs4 import BeautifulSoup
from .utils.session import SessionDB
from .utils.config import *
#from translate import Translator as tr
import goslate
from yowsup.demos.zclient.views.include import get

class ProgramView():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.session_db = SessionDB("/tmp/sessions.db", "quiz")
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^(?P<program>Program|program)$", self.help),
            ("^(?P<fan>fan)$", self.fan),
            ("^(?P<tv>tv)$", self.tv),
            ("^(?P<profile>profile)$", self.profile),
            ("^(?P<about_bigart>about_bigart|info_bigart)$", self.about),
            ("fact (?P<number>[^$]+)$", self.fact),
            ("rps (?P<term>[^$]+)$", self.rps),
            ("break (?P<term>[^$]+)$", self.breaker),
            ("@(?P<term>[^$]+)$", self.ask),
            ("job (?P<name1>[^$]+)$", self.job),
            ("set (?P<profile>[^$]+) (?P<name>[^$]+)$", self.setpro),
            ("cout (?P<msg>[^$]+)$", self.echo),
            ("printf (?P<msg>[^$]+)$", self.echo),
            ("(loop(?P<num>[^$]+) (?P<msg>[^$]+)$)", self.loop),
            ("calc (?P<num>[^$]+)$", self.calculator),
            ("input (?P<num>[^$]+)$", self.have),
            ("translate (?P<msg>[^$]+)$", self.translate),
        ]

    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP , to=message.getFrom())

    def tv(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(get("tv") , to=message.getFrom())
    
    def ask(self, message=None, match=None, to=None):
        def question(n):
            url = "http://jarbot.top/bot/profile_add.php?q="+n
            data = requests.get(url)
            data = data.text
            cur = json.loads(data)
            return cur
        try:
           txt = question(match.group("term"))
        except (RuntimeError, TypeError, NameError, ValueError):
           print("Error : Try Again")
           txt = question(match.group("term")) 
        return TextMessageProtocolEntity(txt , to=message.getFrom())
    
    def profile(self, message=None, match=None, to=None):
        def question(n):
            url = "http://jarbot.top/bot/profile__show.php?q="+n
            data = requests.get(url)
            data = data.text
            cur = json.loads(data)
            name = cur['user'][0]['name']
            city = cur['user'][0]['city']
            return (name,city)
        try:
           txt = question(message.getAuthor())
        except (RuntimeError, TypeError, NameError, ValueError):
           print("Error : Try Again")
           txt = question(message.getAuthor())
        content = "Name : "+str(txt[0])+"\nCity : "+str(txt[1])
        return TextMessageProtocolEntity(content , to=message.getFrom())

    def setpro(self, message=None, match=None, to=None):
        def create(n,ty):
            if "phone" == ty:
                url = "http://jarbot.top/bot/profile_add.php?profile="+n
            elif "name" == ty:
                url = "http://jarbot.top/bot/profile_add.php?pro="+message.getAuthor()+"&name="+n+"&type=name"
            elif "city" == ty:
                url = "http://jarbot.top/bot/profile_add.php?pro="+message.getAuthor()+"&name="+n+"&type=city"
            data = requests.get(url)
            data = data.text
            cur = json.loads(data)
            return cur
        try:
            if match.group("profile") == "phone":
                txt = create(message.getAuthor(),"phone")
            elif match.group("profile") == "name":
                txt = create(match.group("name"),"name")
            elif match.group("profile") == "city":
                txt = create(match.group("name"),"city")
        except (RuntimeError, TypeError, NameError, ValueError):
            print("Error : Try Again")
            if match.group("profile") == "phone":
                txt = create(message.getFrom(),"phone")
            elif match.group("profile") == "name":
                txt = create(match.group("name"),"name")
            elif match.group("profile") == "city":
                txt = create(match.group("name"),"city")
        return TextMessageProtocolEntity(txt , to=message.getFrom())
    
    def have(self, message=None, match=None, to=None):
        url = "http://jarbot.top/bot/test13.txt"
        data = requests.get(url)
        data = data.text
        return TextMessageProtocolEntity( a, to=message.getFrom())


    def job(self, message=None, match=None, to=None):
        def search(name):
            job = ""
            if "skill" in name:
                match = re.search('skill (?P<name>.*) (?P<number>.*)', name)
            elif "city" in name:
                match = re.search('city (?P<name>.*) (?P<number>.*)', name)
            c = match.group('name')
            num = int(match.group('number'))
            if "skill" in name:
                url = "http://www.naukri.com/"+c+"-jobs"
            elif "city" in name:
                url = "https://www.naukri.com/jobs-in-"+c
            data = requests.get(url)
            data = data.text
            soup = BeautifulSoup((data), "lxml")
            content = mydivs = soup.findAll("a", { "class" : "content" })
            job += "*Total Results : "+str(len(content))+"*\n\n"
            for search in range(num):
                site = content[search]
                take = site.text[1:].split(",")
                for one in take:
                    job += one+"\n"
                job += "===============================\n"
            return job
        job = match.group("name1")
        try:
            result = search(job)
        except:
            result = search(job)
        return TextMessageProtocolEntity(result, to=message.getFrom())

    def translate(self, message=None, match=None, to=None):
        def trns(word,lang="en"):
            gs = goslate.Goslate()
            a = gs.translate(word, lang)
            return a
        reg = match.group("msg")
        reg = reg.split(" ")
        lang=reg[0]
        if lang == "hindi":
            lang = "hi"
        elif lang == "english":
            lang = "en"
        word=" ".join(reg[1:])
        try:
            text = trns(word,lang)
        except (RuntimeError, TypeError, NameError):
            text = "Jarvis Crashed"
        return TextMessageProtocolEntity(word + " <=> " + text , to=message.getFrom())

    def calculator(self, message=None, match=None, to=None):
        num = match.group("num")
        total = eval(num)
        return TextMessageProtocolEntity("Result = "+str(total), to=message.getFrom())

    def about(self, message=None, match=None, to='abc'):
        def run():
            query = ""
            url = "http://jarbot.top/bot/show.php?view=true"
            data = requests.get(url)
            data = data.text
            url1 = "http://jarbot.top/bot/show.php?total=true"
            data1 = requests.get(url1)
            total = int(data1.text)

            cur = json.loads(data)
            query += "[The BigArt Group Serving Help For You]\n\n"
            for loop in range(total):
                query += str(cur['list'][loop]['id'])
                query += " Name = " + str(cur['list'][loop]['name'])
                query += "\nNumber = +" + str(cur['list'][loop]['num'])
                query += "\nSkill = " + str(cur['list'][loop]['skill'])
                query += "\nLocation = " + str(cur['list'][loop]['location'])
                query += "\n\n"
            query += "Hi i am a BigArt Bot and you are going to add in the list."
            return(query)  
        try:
           txt = run()
        except (RuntimeError, TypeError, NameError, ValueError):
           print("Error : Try Again")
           txt = run()
        if to == 'abc':
            self.interface_layer.toLower(TextMessageProtocolEntity(txt, to='919851478875@s.whatsapp.net'))
        else:
            return TextMessageProtocolEntity(txt , to=message.getFrom())

    def echo(self, message=None, match=None, to=None):
        msg = match.group("msg")
        return TextMessageProtocolEntity(msg , to=message.getFrom())

    def loop(self, message=None, match=None, to=None):
        num = int(match.group("num"))
        txt = match.group("msg")
        text = ""
        if num > 500:
            num = 1
        for i in range(num):
            text += txt+"\n"
        return TextMessageProtocolEntity(text , to=message.getFrom())

    def breaker(self, message=None, match=None, to=None):
        term = match.group("term")
        s = ""
        a = []
        for x in str(term):
            s = s+x
            a.append(s)
        self.interface_layer.toLower(TextMessageProtocolEntity("\n".join(a), to=message.getFrom()))

    def rps(self, message=None, match=None, to=None):
        def say(word):
            self.interface_layer.toLower(TextMessageProtocolEntity(word, to=message.getFrom()))
        player = match.group("term").lower()
        computerInt = random.randint(0,2);
        if (computerInt == 0):
            computer = "rock"
        elif (computerInt == 1):
            computer = "paper"
        elif (computerInt == 2):
            computer = "scissors"
        else:
            computer = "Huh? Error..."

        if (player == computer):
            say("Draw!")
        elif (player == "rock"):
            if (computer == "paper"):
                say("Computer wins!")
            else:
                say("You win!")
        elif (player == "paper"):
            if (computer == "rock"):
                say("You win!")
            else:
                say("Computer wins!")
        elif (player == "scissors"):
            if (computer == "rock"):
                say("Computer wins!")
            else:
                say("You win!")

        say("Your choice: " + player + "\nComputer choice: " + computer + "\nThank you for playing!")
        
    def fact(self, message=None, match=None, to=None):
        num = int(match.group("number"))
        fact = 1
        if num < 0:
           text = "Sorry, factorial does not exist for negative numbers"
        elif num == 0:
           text = "The factorial of 0 is 1"
        else:
            if num < 1000:
                for i in range(1,num + 1):
                    fact = fact * i
                text = "The factorial of "+str(num)+" is "+str(fact)
            else:
                text = str(num) + " is very huge number. Try Smalller Number"
        return TextMessageProtocolEntity(text , to=message.getFrom())

    def fan(self, message=None, match=None, to=None):
        def ru():
            query = ""
            url = "http://jarbot.top/bot/show.php?fan=true"
            data = requests.get(url)
            data = data.text
            url1 = "http://jarbot.top/bot/show.php?fan_total=true"
            data1 = requests.get(url1)
            total = int(data1.text)
    
            cur = json.loads(data)
            query += "[FAN PAGE]\n\n"
            for loop in range(total):
                query += str(cur['list'][loop]['id'])
                query += ". " + str(cur['list'][loop]['name'])
                query += "\n\n"
            query += "Become a Fan By Submitting Your Name\n\nhttp://mcetbhb.top/fan.php"
            return(query)  
        try:
           txt = ru()
        except (RuntimeError, TypeError, NameError, ValueError):
           print("Error : Try Again")
           txt = ru()    
        return TextMessageProtocolEntity(txt , to=message.getFrom())

HELP ="""[PROGRAM MENU]
1. Factorial - fact <number>
"""
