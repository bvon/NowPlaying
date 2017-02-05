from objc_util import *
import twitter
import dialogs

# Music Controller

MPController = ObjCClass('MPMusicPlayerController')
player = MPController.systemMusicPlayer()
nowPlaying = player.nowPlayingItem()

# Twitter setup

tAccts = twitter.get_all_accounts()
if len(tAccts) >= 1:
	acct = tAccts[0]
else:
	None

# Return artist/song, post

if nowPlaying:
	artist = nowPlaying.valueForProperty_('artist')
	title = nowPlaying.valueForProperty_('title')

	NP = '#NowPlaying: %s - "%s"' % (artist, title)
	
	checkPost = dialogs.alert('#NowPlaying', 'Currently playing: %s - "%s"' % (artist, title) + '. Tweet it?', 'Nope', 'Tweet', hide_cancel_button=True)
	
	if checkPost == 2:
		twitter.post_tweet(acct, NP)
		dialogs.alert('#NowPlaying', 'Posted', 'Okay', hide_cancel_button=True)
	elif checkPost == 1:
		dialogs.alert('#NowPlaying', 'Canceled', 'Okay', hide_cancel_button=True)
