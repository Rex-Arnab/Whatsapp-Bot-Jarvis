from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.demos.zclient.utils.media_sender import GifsSender
import requests, urllib.parse


class GifsViews():
    def __init__(self, interface_layer):
        self.gifs_sender = GifsSender(interface_layer)
        self.routes = [
            (".*\.gif$", self.send_gifs_video)
        ]

    def send_gifs_video(self, message, match):
        self.gifs_sender.send_by_url(jid=message.getFrom(), file_url=message.getBody())
