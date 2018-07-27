#!/usr/local/bin/python
# coding: latin-1
#from media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import json

class DownloadViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
	#self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
	    ("^download$", self.down),
            ("^show$", self.show),
            ("^write$", self.write),
        ]


    def down(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())

    def show(self, message=None, match=None, to=None):
        a = ""
        with open('new.json') as json_file:  
            data = json.load(json_file)
            for p in data['people']:
                a += 'Name: ' + p['name']+'\n'
                a += 'Website: ' + p['website']+'\n'
                a += 'From: ' + p['from']+'\n'
                a += '\n'
        return TextMessageProtocolEntity(a, to=message.getFrom())

    def write(self, message=None, match=None, to=None):
        data = {}  
        data['people'] = []  
        data['people'].append({  
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        data['people'].append({  
            'name': 'Larry',
            'website': 'google.com',
            'from': 'Michigan'
        })
        data['people'].append({  
            'name': 'Tim',
            'website': 'apple.com',
            'from': 'Alabama'
        })

        with open('new.json', 'w') as outfile:  
            json.dump(data, outfile) 
        return TextMessageProtocolEntity("done", to=message.getFrom())


HELP_TEXT = """ [Download Menu]

* Compilers *
1. Python - https://www.python.org
2. Turbo C - http://turboc.codeplex.com/downloads/get/1609375
3. (a)BlueJ - https://www.bluej.org/versions.html
   (b)JDK   - http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

4. Android Sudio - https://developer.android.com/studio/index.html

* Text Editors *
1. NotePad++ - https://notepad-plus-plus.org/download/v7.3.3.html
2. Sublime text - https://www.sublimetext.com/3
(sublime licance key - https://gist.github.com/rauniaporta/15e0bbd00629b589345ba9f69c547b10)
"""
