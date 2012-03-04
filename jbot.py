import xmpp, time

user = 'whe59ru@jabber.ru'
passwd = 'n1k0max1208'
_SERVER = 'jabber.ru', 5222

jid=xmpp.protocol.JID(user)

server = jid.getDomain()
print server

cli = xmpp.Client(server ,debug=[])
cli.connect(server = _SERVER)

auth = cli.auth(user, passwd, 'con')

cli.send(xmpp.protocol.Message('n1k0n0v@gentoo.ru', 'HI!'))

#auth = xmppClient.auth(jid.getNode(), xmppPassword, 'botty')

cli.disconnect()
