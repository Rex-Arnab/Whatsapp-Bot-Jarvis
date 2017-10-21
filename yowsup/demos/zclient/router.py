import threading
import re
import logging

#Working Files
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.demos.zclient.views.basic_views import BasicViews
from yowsup.demos.zclient.views.media import MediaViews
from yowsup.demos.zclient.views.super_views import SuperViews
from yowsup.demos.zclient.views.books import BooksViews
from yowsup.demos.zclient.views.fun import FunViews
from yowsup.demos.zclient.views.quiz import QuizView
from yowsup.demos.zclient.views.download import DownloadViews
from yowsup.demos.zclient.views.group_admin import GroupAdminViews

#Broken Files
from yowsup.demos.zclient.utils import helper
from yowsup.demos.zclient.mac import mac, signals
from yowsup.layers.protocol_media.mediadownloader import MediaDownloader
from yowsup.demos.zclient.receiver import receiver
from yowsup.demos.zclient.models.message import Message

#from datetime import datetime as clock
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
        routes.extend(DownloadViews(self).routes)
        routes.extend(GroupAdminViews(self).routes)
        routes.extend(MediaViews(self).routes)

        self.views = [(re.compile(pattern), callback) for pattern, callback in routes]

    def route(self, message):
        "Get the text from message and tests on every route for a match"
        text = message.getBody()
                
        for route, callback in self.views:
            match = route.match(text)
            if match:  # in case of regex match, the callback is called, passing the message and the match object
                threading.Thread(target=self.handle_callback, args=(callback, message, match)).start()
                break

    def handle_callback(self, callback, message, match):
        try:
            # log message request
            if (message.isGroupMessage()):
                logging.info("(GROUP)[%s]-[%s]\t%s" % (message.getParticipant(), message.getFrom(), message.getBody()))
            else:
                logging.info("(PVT)[%s]\t%s" % (message.getFrom(), message.getBody()))
            # execute callback request
            data = callback(message, match)
            if data: self.toLower(data)  # if callback returns a message entity, sends it.
        except Exception as e:
            logging.exception("Error routing message: %s\n%s" % (message.getBody(), message))

    @ProtocolEntityCallback("message")
    def on_message(self, message):
        "Executes on every received message"
        self.toLower(message.ack())  # Auto ack
        self.toLower(message.ack(True))  # Auto ack (double blue check symbol)
        if message.getType() == 'text':
            self.route(message)
        if message.getType() == 'media':
            self.route(message)
        if message.getType() == 'audio':
            self.route(message)
        if message.getType() == 'location':
            self.route(message)


    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        "Auto ack for every message receipt confirmation"
        self.toLower(entity.ack())
