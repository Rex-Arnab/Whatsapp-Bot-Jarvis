#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random


class BooksViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
	#self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
	    ("^(?P<phelp>p_help)$", self.p_help),
            ("^(?P<python3>python3)$", self.python3),
	    ("^(?P<python>python)$", self.python),
	    ("^(?P<html>html)$", self.html),
	    ("^(?P<css>css)$", self.css),
            ("^(?P<cs>cs)$", self.cs),
            ("^(?P<cpp>c|cpp|c#|dotnet)$", self.cpp),
            ("^(?P<android>android)$", self.android),    
	    ("^(?P<udemy>udemy)$", self.udemy),
	    ("^(?P<java>java)$", self.java),
            ("^(?P<amazon>amazon)$", self.amazon),
            ("^(?P<go>go)$", self.go),
	    ("^(?P<ajax>ajax)$", self.ajax),
            ("^(?P<hacking>hacking)$", self.hacking),
            ("^(?P<linux>linux)$", self.linux),
	    ("^sp100$", self.spl1),
	    ("^(?P<javascript>javascript|js)$", self.javascript)
        ]

    def go(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0ByWO0aO1eI_MdkZwY2VRNzEtbDg", to=message.getFrom())

    def amazon(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0B-naBPVFnJB-SDNNNUdRYTRxeGM", to=message.getFrom())

    def cs(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0ByWO0aO1eI_MV0xmOHVJdEstR2M", to=message.getFrom())

    def linux(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0B-naBPVFnJB-OGxSZzljajUwN28", to=message.getFrom())

    def android(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0B-naBPVFnJB-Q2ZISEFucDctQkk", to=message.getFrom())

    def cpp(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Gdrive : https://drive.google.com/open?id=0B-naBPVFnJB-X0ZHLTNtcEdNbEE", to=message.getFrom())

    def udemy(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(udemy_txt, to=message.getFrom())

    def hacking(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Hacking* \nGdrive : https://drive.google.com/open?id=0B-naBPVFnJB-WGdiMHc5c254d1k", to=message.getFrom())

    def ajax(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Ajax* \nINFO : https://www.w3schools.com/ajax\nINFO(2) : https://www.tutorialspoint.com/ajax\nPDF : https://www.tutorialspoint.com/ajax/ajax_pdf_version.htm", to=message.getFrom())

    def python(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Python* \nINFO : https://www.tutorialspoint.com/python\nPDF : https://www.tutorialspoint.com/python/python_pdf_version.htm", to=message.getFrom())

    def python3(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Python3* \nINFO : https://www.tutorialspoint.com/python3\nPDF : https://www.tutorialspoint.com/python3/python_pdf_version.htm\nGdrive : https://drive.google.com/open?id=0B-naBPVFnJB-TDJ4NFFrQWdpLW8", to=message.getFrom())

    def html(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Html* \nINFO : https://www.w3schools.com/html\nPDF : https://www.tutorialspoint.com/html/html_pdf_version.htm\nGdrive : https://drive.google.com/open?id=0B-naBPVFnJB-QU0wNHY4QnlWNHM", to=message.getFrom())

    def p_help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(P_HELP_TEXT, to=message.getFrom())

    def css(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Css* \nINFO : https://www.w3schools.com/css\nPDF : https://www.tutorialspoint.com/css/css_pdf_version.htm", to=message.getFrom())

    def javascript(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *JavaScript* \nINFO : https://www.w3schools.com/js\nPDF : https://www.tutorialspoint.com/javascript/javascript_pdf_version.htm\nGdrive : https://drive.google.com/open?id=0B-naBPVFnJB-anhQZzN1ZzBDdUk", to=message.getFrom())

    def java(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(" *Java* \nINFO : http://www.tutorialspoint.com/java\nPDF : https://www.tutorialspoint.com/java/java_pdf_version.htm\nGdrive : https://drive.google.com/open?id=0B-naBPVFnJB-anhQZzN1ZzBDdUk", to=message.getFrom())

    def spl1(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(spcl1, to=message.getFrom())

P_HELP_TEXT = """[P_HELP]
 p_Help - Show this message.
 html - Information about HTML
 css - Information about CSS
 Go - Learn Go
 javascript - Informatio about JAVASCRIPT
 python - Informatio about Python 2.x
 python3 - Informatio about Python 3.x
 java - Informatio about JAVA
 ajax - Informatio about Ajax
 c/cpp/c#/dotnet - Informatio about these
 cs - C# Seperatly Guide
 android - Android Study Resourse
 hacking - learn Hacking
 linux - learn Linux
 amazon - learn amazon
 *udemy* - Udemy Gallary
 *sp100* - 100 Free courses
 More Comming Soon..."""

udemy_txt = """

Swift 3 Introduction to the Basics
http://bit.ly/Swift3Intro

Android Programming From Scratch - For Beginners
http://bit.ly/Android_Programming

Promote & Sell Your Apps: From Beginner To Expert
http://bit.ly/PromoteSellApp

C++ Programming - The Complete Course
http://bit.ly/CplusplusProgramming

Xamarin Native Android Puzzle Game with C#
http://bit.ly/XamarinNativeAndroid

Traffic Flood: Your Ads Before Millions of Weekly Readers
http://bit.ly/TrafficFlood

The Complete iOS 10 App Entrepreneur: Build A Tech Start-Up!
http://bit.ly/CompleteIOS10

Xamarin Native iOS Memory Game C#
http://bit.ly/XamarinNativeIOS

Become a Coffee Expert: How to Make the Perfect Cup
http://bit.ly/CoffeeExpertt

Xamarin Android Sliding Puzzle C#
http://bit.ly/XamarinAndroidSlidingPuzzle

(by mesut)
"""
spcl1 = """
Download over 100 Plus Programming courses For Free

Programming Languages in the Drive:
{ C }
CitrixðŸŒ€
²GO²
JAVA 
Android
RUBY
JavaScript
LINUX
˜CLOUD ,DEVOPS,CS
PHP
PYTHON

Many Other Books
TeamTreehouse 
Other Web General Courses.

Google Drive Link: http://bit.ly/2ps8wKD

Donations will be appreciated:
 1GuXnf7XyMnmE1vSFoPDQ7oJbehW4G3KgZ

*Have Fun*"""
