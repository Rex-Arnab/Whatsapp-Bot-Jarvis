import sys, logging
from yowsup.demos.zclient.utils.config import *

from yowsup.layers.auth import AuthError
from yowsup.layers.axolotl.props import PROP_IDENTITY_AUTOTRUST
from yowsup.stacks import YowStackBuilder
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer

from .router import RouteLayer

# Uncomment to log
#logging.basicConfig(level=logging.DEBUG)

# Config

class MacStack(object):
    def __init__(self, credentials, encryption = True):
        builder = YowStackBuilder()

        self.stack = builder\
            .pushDefaultLayers(encryption)\
            .push(RouteLayer)\
            .build()

        self.stack.setCredentials(credentials)
        self.stack.setProp(MacLayer.PROP_CONTACTS,  list(config.contacts.keys()))
        self.stack.setProp(PROP_IDENTITY_AUTOTRUST, True)

    def start(self):
        print("[Whatsapp] Mac started\n")

        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

        try:
            self.stack.loop(timeout=0.5, discrete=0.5)
        except AuthError as e:
            print("Auth Error, reason %s" % e)
        except KeyboardInterrupt:
            print("\nBye")
            sys.exit(0)
            
def run_infinite():
    while True:
        try:
            c = MacStack()
            c.start()
        except:
            pass
        else:
            break

if __name__ == "__main__":
    c = MacStack()
    c.start()
