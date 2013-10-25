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
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	
	rv = [];
	
	rv.append("<h1>" + username + "</h1>");
	rv.append("Total Tweets: " + str(user.statuses_count));
	rv.append("Profile Creation Date: " + str(user.created_at));
	rv.append("Description: " + str(user.description));
	rv.append("Favorites: " + str(user.favourites_count));
	rv.append("Following? " + str(user.following));
	rv.append("Friends: " + str(user.friends_count));
	rv.append("Geotagging Enabled? " + str(user.geo_enabled));
	rv.append("Language: " + str(user.lang));
	rv.append("Listed Count: " + str(user.listed_count));
	rv.append("Location: " + str(user.location));
	rv.append("User Name: " + str(user.name));
	rv.append("Profile Background Color: " +  str(user.profile_background_color));
	rv.append("Profile Background Image URL: " + "<img width=\"100\" src=" + str(user.profile_background_image_url) + " />");
	rv.append("Profile Image URL: " + "<img width=\"100\" src=" + str(user.profile_image_url) + " />");
	rv.append("Protected? " + str(user.protected));
	rv.append("Screen Name: " + str(user.screen_name));
	rv.append("Status: " + str(user.status));
	rv.append("Time Zone: " + str(user.time_zone));
	rv.append("User URL: " + str(user.url));
	rv.append("UTC Offset: " + str(user.utc_offset));
		
	for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(100):
		rv.append(status.text);
		
	return rv;