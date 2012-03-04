import subprocess
import sys
from jabberbot import *

user = 'whe59ru@jabber.ru'
pws = 'n1k0max1208'


class UptimeBot(JabberBot):
    @botcmd
    def uptime(self, mess, args):
        """Get current uptime information"""
        return 'nyan'



uptime_bot = UptimeBot(user, pws )
uptime_bot.serve_forever()

