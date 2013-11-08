# Ths file takes as input two twitter handles and returns all the needed data from Twitter associated
# with those handles

import tweepy, urllib2, os
import analyze_category

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
	rv = rv + unicode("Total Tweets: " + str(user.statuses_count) + "\n");
	rv = rv + unicode("Profile Creation Date: " + str(user.created_at) + "\n");
	rv = rv + unicode("Description: " + str(user.description) + "\n");
	rv = rv + unicode("Favorites: " + str(user.favourites_count) + "\n");
	rv = rv + unicode("Following? " + str(user.following) + "\n");
	rv = rv + unicode("Friends: " + str(user.friends_count) + "\n");
	rv = rv + unicode("Geotagging Enabled? " + str(user.geo_enabled)+ "\n");
	rv = rv + unicode("Language: " + str(user.lang)+ "\n");
	rv = rv + unicode("Listed Count: " + str(user.listed_count)+ "\n");
	rv = rv + unicode("Location: " + str(user.location)+ "\n");
	rv = rv + unicode(u"User Name: " + unicode(user.name)+ "\n");
	rv = rv + unicode("Profile Background Color: " +  str(user.profile_background_color)+ "\n");
	rv = rv + unicode("Profile Background Image URL: " + "<img width=\"100\" src=" + str(user.profile_background_image_url) + " />"+ "\n");
	rv = rv + unicode("Profile Image URL: " + "<img width=\"100\" src=" + str(user.profile_image_url) + " />"+ "\n");
	rv = rv + unicode("Protected? " + str(user.protected)+ "\n");
	rv = rv + unicode("Screen Name: " + str(user.screen_name)+ "\n");
	rv = rv + unicode("Status: " + str(user.status)+ "\n");
	rv = rv + unicode("Time Zone: " + str(user.time_zone)+ "\n");
	rv = rv + unicode("User URL: " + str(user.url)+ "\n");
	rv = rv + unicode("UTC Offset: " + str(user.utc_offset)+ "\n");
		
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
		
	return statuses;