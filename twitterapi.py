# Ths file takes as input two twitter handles and returns all the needed data from Twitter associated
# with those handles

import tweepy, urllib2

def getAPIInfo(username):
	
	# Authenticate with Twitter. This code is taken from the Tweepy example files
	consumer_key="mflJ0zhrutRVCk35emOQ"
	consumer_secret="MYMT6oxERQcduEf5KZiHNkj66nzrcgO9bLjsHvJmAg"
	
	access_token="152181424-rnFWgXq9QcViENymDfoDwo2AeLfEPGkgSFmWXoJn"
	access_token_secret="oVddejjnJfxkV9nMy6m97O3pbf8jQCdnoOsfTXnU"
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	api = tweepy.API(auth)
	
	user = api.get_user(username);
	userfavorites = api.favorites(username);
	#userfollowers = api.followers(username);
	usertweets = api.home_timeline
	
	print("\n\nTweets:::::::");
	for i in userlist:
		print(i.text);
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	print("\n\nUser Data:::::::");
	print(user.statuses_count);
	print(user.created_at);
	print(user.description);
	print(user.favourites_count);
	print(user.following);
	print(user.friends_count);
	print(user.geo_enabled);
	print(user.lang);
	print(user.listed_count);
	print(user.location);
	print(user.name);
	print(user.profile_background_color);
	print(user.profile_background_image_url);
	print(user.profile_image_url);
	print(user.protected);
	print(user.screen_name);
	print(user.status);
	print(user.time_zone);
	print(user.url);
	print(user.utc_offset);
	
	# Download all statuses
	tweepy.Cursor(api.user_timeline, id=username);
	
	for status in tweepy.Cursor(api.user_timeline).limit(200):
		process_status(status)
	
	return userlist;