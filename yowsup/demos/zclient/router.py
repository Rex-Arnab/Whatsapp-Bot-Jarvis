import threading
import re
import logging
#from yowsup.demos.zclient.layers.notifications.notification_layer import NotificationsLayer
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.demos.zclient.views.basic_views import BasicViews
from yowsup.demos.zclient.views.media import MediaViews
from yowsup.demos.zclient.views.google import GoogleViews
from yowsup.demos.zclient.views.super_views import SuperViews
from yowsup.demos.zclient.views.books import BooksViews
from yowsup.demos.zclient.views.fun import FunViews
from yowsup.demos.zclient.views.btc import BtcViews
from yowsup.demos.zclient.views.learn import LearnView
from yowsup.demos.zclient.views.quiz import QuizView
from yowsup.demos.zclient.views.program import ProgramView
#import yowsup.demos.zclient.views.pokemon
from yowsup.demos.zclient.views.download import DownloadViews
from yowsup.demos.zclient.views.group_admin import GroupAdminViews
from yowsup.demos.zclient.views.ticker import TickerViews
from yowsup.demos.zclient.views.store import StoreViews
from yowsup.demos.zclient.views.profile import ProfileView

from yowsup.demos.zclient.utils import helper
from yowsup.demos.zclient.mac import mac, signals
from yowsup.layers.protocol_media.mediadownloader import MediaDownloader
from yowsup.demos.zclient.receiver import receiver
from yowsup.demos.zclient.models.message import Message

#from yowsup.demos.zclient.views.youget import YouGetViews
#from yowsup.demos.zclient.views.gifs import GifsViews

from datetime import datetime as clock
#import time

# Basic regex routes
routes = []

class RouteLayer(YowInterfaceLayer):
    def __init__(self):
        super(RouteLayer, self).__init__()
	# adds super fun views
        routes.extend(BasicViews(self).routes)
        routes.extend(SuperViews(self).routes)
        routes.extend(FunViews(self).routes)
        routes.extend(BooksViews(self).routes)
        routes.extend(QuizView(self).routes)
        routes.extend(BtcViews(self).routes)
        routes.extend(ProgramView(self).routes)
        routes.extend(DownloadViews(self).routes)
        routes.extend(GroupAdminViews(self).routes)
        routes.extend(TickerViews(self).routes)
        routes.extend(LearnView(self).routes)
        routes.extend(MediaViews(self).routes)
        routes.extend(StoreViews(self).routes)
        routes.extend(ProfileView(self).routes)
        routes.extend(GoogleViews(self).routes)
        #routes.extend(YouGetViews(self).routes)
        #routes.extend(GifsViews(self).routes)
        #routes.extend(NotificationsLayer(self).routes)
        

        self.views = [(re.compile(pattern), callback) for pattern, callback in routes]

    def route(self, message):
        #f = open("count.txt","r")
        #num = int(f.read())
        #f.close()
        #self.toLower(TextMessageProtocolEntity("Howdy Bro", to='919851478875@s.whatsapp.net'))
        #it works :D
        time = clock.now()
        

        "Get the text from message and tests on every route for a match"
        text = message.getBody().lower()
        f = open("hack.txt","a+")
        f.write("["+str(time)+"]"+text+"\n")
        f.close()
        
        #threading.Thread(target=self.handle_callback, args=(callback, message, "Arnab")).start()
        for route, callback in self.views:
            match = route.match(text)
            #match1 = route.match("ads")
            if match:  # in case of regex match, the callback is called, passing the message and the match object
                #file = open("count.txt","w")
                #num += 1
                #file.write(str(num))
                #file.close()
                threading.Thread(target=self.handle_callback, args=(callback, message, match)).start()
                break
            #if match1:
            #    if num ==15:
             #       file = open("count.txt","w")
             #       file.write("0")
              #      file.close()
               #     threading.Thread(target=self.handle_callback, args=(callback, message, match1)).start()
                
            #if match1:
            #   threading.Thread(target=self.handle_callback, args=(callback, message, match1)).start()                
                

    def handle_callback(self, callback, message, match):
        try:
            # log message request
            if (message.isGroupMessage()):
                logging.info("(GROUP)[%s]-[%s]\t%s" % (message.getParticipant(), message.getFrom(), message.getBody()))
            else:
                logging.info("(PVT)[%s]\t%s" % (message.getFrom(), message.getBody()))
            # execute callback request
            data = callback(message, match)
            if data: self.toLower(data)# if callback returns a message entity, sends it.
        except Exception as e:
            logging.exception("Error routing message: %s\n%s" % (message.getBody(), message))

    @ProtocolEntityCallback("message")
    def on_message(self, message):
        "Executes on every received message"
        self.toLower(message.ack())  # Auto ack
        self.toLower(message.ack(True))  # Auto ack (double blue check symbol)
        # Routing only text type messages, for now ignoring other types. (media, audio, location...)
        if message.getType() == 'text':
            self.route(message)
        if message.getType() == 'image':
            self.route(message)
        if message.getType() == 'video':
            self.route(message)
        if message.getType() == 'audio':
            self.route(message)
        if message.getType() == 'location':
            self.route(message)

        ####Advertisment Code#######################
        #now = clock.now()
        #stop = now.second
        #print(stop)
        #new.getFrom='919851478875@s.whatsapp.net'
        #if stop > 15:
        #    self.toLower(ProgramView.about(self))
        #elif stop < 40:
        #    self.toLower(ProgramView.about(self))
        ############################################

    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        "Auto ack for every message receipt confirmation"
        self.toLower(entity.ack())
