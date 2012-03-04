import oauth, tweepy
from mpd import MPDClient
import time

### loop settings ###

delay = 600

### MPD settings ###

HOST = '10.0.0.1'
PORT = '6600'
PASS = False

### Twitter settings ###

# gives access to app
appKey = 'wgRyY4h641k4u8CPlgUQ'
appSec = 'secret'

# gives access to user
userKey = 'secret'
userSec = 'secret'

# this func post message
def statusUp(msg):
	var = len(msg)
	if var < 140 and var > 0:
		api.update_status(msg)
		return 'ok'
	if var == 0 or var > 140:
		return 'not_ok'

# this func get data from mpd
def getMeta(HOST, PORT):
	# connect
	client = MPDClient()
	client.connect(HOST, PORT)
	# fetch data
	stat = client.status()
	stat = stat['state']
	temp =  client.currentsong()
	# prepare data
	meta = """#nowplaying """ + temp['artist'] + ' - ' + temp['title']
	# closing connection to mpd
	client.close()
	client.disconnect()
	if stat == 'play':
		return meta
	else:
		return ''


# init twitter API, must runs first
def twinit(consKey, consSecret, accKey, accSecret):
	global api
	auth = tweepy.OAuthHandler(consKey, consSecret)
	auth.set_access_token(accKey, accSecret)
	api = tweepy.API(auth)


# init twitter account
twinit (appKey, appSec, userKey, userSec)

while delay > 0:
	print statusUp(getMeta(HOST, PORT))
	time.sleep(delay)
