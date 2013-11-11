# Ths file takes as input two twitter handles and returns all the needed data from Twitter associated
# with those handles

import tweepy, urllib2, os
import alchemy_analyze

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
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	
	rv = "";
	
	rv = rv + unicode("<h1>" + username + "</h1>"+ "\n");
	rv = rv + unicode("Total Tweets: " + unicode(user.statuses_count) + "\n");
	rv = rv + unicode("Profile Creation Date: " + unicode(user.created_at) + "\n");
	rv = rv + unicode("Description: " + unicode(user.description) + "\n");
	rv = rv + unicode("Favorites: " + unicode(user.favourites_count) + "\n");
	rv = rv + unicode("Following? " + unicode(user.following) + "\n");
	rv = rv + unicode("Friends: " + unicode(user.friends_count) + "\n");
	rv = rv + unicode("Geotagging Enabled? " + unicode(user.geo_enabled)+ "\n");
	rv = rv + unicode("Language: " + unicode(user.lang)+ "\n");
	rv = rv + unicode("Listed Count: " + unicode(user.listed_count)+ "\n");
	rv = rv + unicode("Location: " + unicode(user.location)+ "\n");
	rv = rv + unicode(u"User Name: " + unicode(user.name)+ "\n");
	rv = rv + unicode("Profile Background Color: " +  unicode(user.profile_background_color)+ "\n");
	rv = rv + unicode("Profile Background Image URL: " + "<img width=\"100\" src=" + unicode(user.profile_background_image_url) + " />"+ "\n");
	rv = rv + unicode("Profile Image URL: " + "<img width=\"100\" src=" + unicode(user.profile_image_url) + " />"+ "\n");
	rv = rv + unicode("Protected? " + unicode(user.protected)+ "\n");
	rv = rv + unicode("Screen Name: " + unicode(user.screen_name)+ "\n");
	rv = rv + unicode("Status: " + unicode(user.status)+ "\n");
	rv = rv + unicode("Time Zone: " + unicode(user.time_zone)+ "\n");
	rv = rv + unicode("User URL: " + unicode(user.url)+ "\n");
	rv = rv + unicode("UTC Offset: " + unicode(user.utc_offset)+ "\n");
		
	return rv;

def getStatuses(username):
	
	# Authenticate with Twitter. This code is taken from the Tweepy example files
	consumer_key="mflJ0zhrutRVCk35emOQ"
	consumer_secret="MYMT6oxERQcduEf5KZiHNkj66nzrcgO9bLjsHvJmAg"
	
	access_token="152181424-rnFWgXq9QcViENymDfoDwo2AeLfEPGkgSFmWXoJn"
	access_token_secret="oVddejjnJfxkV9nMy6m97O3pbf8jQCdnoOsfTXnU"
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	api = tweepy.API(auth)
	
	usertweets = api.home_timeline
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	
	statuses = "";
	for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(1000):
		statuses = statuses + status.text;

	print(alchemy_analyze.extract_entities(statuses.encode("utf8")));		
	return statuses;