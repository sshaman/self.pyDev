from mpd import MPDClient

# settings

HOST = '10.0.0.1'
PORT = '6600'
PASS = False

client = MPDClient()
client.connect(HOST, PORT)

# currentsong

temp =  client.currentsong()
meta = temp['artist'] + ' - ' + temp['title']

print "result is: ", meta

client.close()
client.disconnect()

