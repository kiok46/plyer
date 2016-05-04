'''
IOS Sms
----------
'''

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

from plyer.facades import Sms
from pyobjus import autoclass, objc_str
from pyobjus.dylib_manager import load_framework

NSURL = autoclass('NSURL')
NSString = autoclass('NSString')
UIApplication = autoclass('UIApplication')
load_framework('/System/Library/Frameworks/MessageUI.framework')


class IOSSms(Sms):

    def _send(self, **kwargs):
        recipient = kwargs.get('recipient')
        message = kwargs.get('message')
        url = "sms:"
        if recipient:
            url += str(recipient)
        if message:
            url += "?" if not "?" in url else "&"
            url += "body="
            url += quote(str(message))
        nsurl = NSURL.alloc().initWithString_(objc_str(url))
        UIApplication.sharedApplication().openURL_(nsurl)


def instance():
    return IOSSms()
