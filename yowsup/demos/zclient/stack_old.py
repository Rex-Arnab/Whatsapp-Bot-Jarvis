#!/usr/local/bin/python
# coding: latin-1
from yowsup.demos.zclient.utils.config import *
from yowsup.stacks import  YowStackBuilder
from .router import RouteLayer
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.axolotl.props import PROP_IDENTITY_AUTOTRUST
#from yowsup.layers.notifications import NotificationsLayer
from yowsup.demos.zclient.layers.notifications.notification_layer import NotificationsLayer

class YowsupzStack(object):
    def __init__(self, credentials, encryptionEnabled = True):
        stackBuilder = YowStackBuilder()
        self.credentials = credentials

        #Set status message
        #entity = SetStatusIqProtocolEntity(config.status_message)
        #self._sendIq(entity, UpdateStatusMessageSuccess, UpdateStatusMessageError)

        #self.stack.setProp(PROP_IDENTITY_AUTOTRUST, True)
        self.stack = stackBuilder\
            .pushDefaultLayers(encryptionEnabled)\
            .push(NotificationsLayer)\
            .push(RouteLayer)\
            .build()
        self.stack.setCredentials(credentials)

#.push([RouteLayer, NotificationsLayer])\
    def start(self):
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)

    def UpdateStatusMessageSuccess(resultIqEntity, originalIqEntity):
        logging.info("Status updated successfully")

    def UpdateStatusMessageError(errorIqEntity, originalIqEntity):
        logging.error("Error updating status")







