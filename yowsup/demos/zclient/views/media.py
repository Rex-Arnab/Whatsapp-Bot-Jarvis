"""
    Media download request views.
    Handles the media url messages with utilities classes for it.
"""
import urllib.parse
from yowsup.demos.zclient.utils.media_downloader import ImageSender, VideoSender, YoutubeSender, UrlPrintSender


class MediaViews():
    def __init__(self, interface_layer):
        """
            Creates the regex routes and callbacks to handle media messages
        """
        self.image_sender = ImageSender(interface_layer)
        self.video_sender = VideoSender(interface_layer)
        self.yt_sender = YoutubeSender(interface_layer)
        self.url_print_sender = UrlPrintSender(interface_layer)
        self.routes = [
            #("https?:\/\/(?:[\w\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:jpe?g|gif|png)($|\?[^\s]+$)", self.send_image),
            ("https?:\/\/(?:[\w\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:jpe?g|png)($|\?[^\s]+$)", self.send_image),
            #("/imgur (?P<pic>[^$]+)$", self.imgur),
            ("https?:\/\/(?:[\w\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:mp4|webm)($|\?[^\s]+$)", self.send_video),
            ("https?:\/\/[^$]+$", self.send_url_print),
            ("http?:\/\/[^$]+$", self.send_url_print),
            ("https?:\/\/(?:www\.)?youtu(?:be.com\/watch\?v=|\.be/)(?P<video_id>[\w-]+)(&\S*)?$", self.send_yt_video),
            ("sendv", self.vdio),
        ]

    def imgur(self, message, match):
        pic = match.group("pic")
        self.image_sender.send_by_url(jid=message.getFrom(), file_url="https://i.imgur.com/"+pic)    

    def vdio(self, message, match):
        self.video_sender.send_by_path(jid=message.getFrom(), path="a.mp4")
        
    def send_video(self, message, match):
        self.video_sender.send_by_url(jid=message.getFrom(), file_url=message.getBody())

    def send_image(self, message, match):
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=message.getBody())

    def send_url_print(self, message, match):
        url = message.getBody()
        url = "http://api.screenshotlayer.com/api/capture?access_key=2ddde16b0e4610147a38b4bba77ba42c&viewport=1440x900&width=250&url="+url
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=url)

    def send_yt_video(self, message, match):
        self.yt_sender.send_by_url(jid=message.getFrom(), file_url=match.group("video_id"))
