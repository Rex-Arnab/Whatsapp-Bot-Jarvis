from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.demos.zclient.utils.media_sender import YouGetSender
import requests, urllib.parse


class YouGetViews():
    def __init__(self, interface_layer):
        self.youget_sender = YouGetSender(interface_layer)
        self.routes = [
            (".*https?:\/\/(?:www\.|m\.)?facebook.com\/", self.send_facebook_video)
        ]

    def send_facebook_video(self, message, match):
        self.youget_sender.handler_facebook(jid=message.getFrom(), full_url=message.getBody())
