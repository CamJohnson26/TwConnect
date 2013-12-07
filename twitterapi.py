# Ths file takes as input two twitter handles and returns all the needed data from Twitter associated
# with those handles

import tweepy, urllib2, os
import alchemy_analyze

class API:
	consumer_key="mflJ0zhrutRVCk35emOQ"
	consumer_secret="MYMT6oxERQcduEf5KZiHNkj66nzrcgO9bLjsHvJmAg"
	
	access_token="152181424-rnFWgXq9QcViENymDfoDwo2AeLfEPGkgSFmWXoJn"
	access_token_secret="oVddejjnJfxkV9nMy6m97O3pbf8jQCdnoOsfTXnU"
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	api = tweepy.API(auth);

def getAPIInfo(username):
	api = API.api;
	
	user = api.get_user(username);
	userfavorites = api.favorites(username);
	#userfollowers = api.followers(username);
	usertweets = api.home_timeline
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	
	rv = {};
	
	rv['username'] = username;
	rv['tweet_count'] = unicode(user.statuses_count);
	rv['description'] = unicode(user.description);
	rv['favorites'] = unicode(user.favourites_count);
	rv['friends_count'] = unicode(user.friends_count);
	rv['followers_count'] = unicode(user.followers_count);
	rv['language'] = unicode(user.lang);
	rv['location'] = unicode(user.location);
	rv['user_name'] = unicode(user.name);
	rv['screen_name'] = unicode(user.screen_name);
	rv['url'] = unicode(user.url);
	rv['profile_image_url'] = unicode(user.profile_image_url);
	rv['background'] = unicode(user.profile_background_image_url);

	return rv;

def getStatuses(username, numberOfTweets):
	api = API.api;

	usertweets = api.home_timeline
	
	# All from https://dev.twitter.com/docs/platform-objects/users
	
	statuses = [];
	#counter = 0;
	for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(numberOfTweets):
	#for status in tweepy.Cursor(api.user_timeline, screen_name=username).items(100):
		statuses.append(status);
		#counter = counter + 1;
		#if counter == 10:
			#print(alchemy_analyze.extract_entities(statuses.encode("utf8")));
	
	return statuses;

def getHashtags(statuses):
	rv = []
	for i in statuses:
		try:
			curhashtags = i.entities[u'hashtags'];
		except:
			curhashtags = [];
		for j in curhashtags:
				rv.append(u'#' + j[u'text'].upper());
	return rv;

def getMedia(statuses):
	rv = []
	for i in statuses:
		try:
			curmedia = i.entities[u'media'];
		except:
			curmedia = [];
		for j in curmedia:
			rv.append(j[u'media_url']);
	return rv;
	
def getURLS(statuses):
	rv = []
	videos = [];
	instagramphotos = [];
	for i in statuses:
		try:
			cururls = i.entities[u'urls'];
		except:
			cururls = []
		for j in cururls:
			displayurl = j[u'display_url']
			if displayurl.find("instagram.com") != -1:
				input = '''<iframe width="150" height="150" src="http://''' + displayurl + '''embed/" frameborder="0" scrolling="no" allowtransparency="true"></iframe>''';
				instagramphotos.append(input);
			elif displayurl.find("youtu.be") != -1:
				input = '''<iframe width="640" height="390" src="http://www.youtube.com/embed/''' + displayurl[9:len(displayurl)] + '''" frameborder="0"></iframe>''';
				videos.append(input);
	return rv + videos + instagramphotos;
	
def getUserMentions(statuses):
	rv = []
	for i in statuses:
		try:
			curmentions = i.entities[u'user_mentions'];
		except:
			curmentions = [];
		for j in curmentions:
				rv.append(j[u'screen_name']);
	return rv;

def getCommonFollowers(user1name,user2name):
	api = API.api;

	
	user1followers = api.friends_ids(user1name);
	user2followers = api.friends_ids(user2name);
	
	commonfollowers = [];
	
	user1followerd = {};
	for i in user1followers:
		user1followerd[i] = 1;
		
	for i in user2followers:
		try:
			user1followerd[i];
			commonfollowers.append(i);
		except KeyError:
			1+1;
	rv = [];
	for i in commonfollowers:
		user = api.get_user(i)
		screenname = user.screen_name;
		profileimage = user.profile_image_url;
		description = user.description;
		location = user.location;
		friends = user.friends_count;
		followers = user.followers_count;
		username = user.name;
		tweetcount = user.statuses_count;
		bgimage = user.profile_background_image_url;
		rv.append([profileimage,screenname,description,location,friends,followers,username,tweetcount,bgimage]);
	return rv;
	
def getCommonPeople(u1, u2):
	api = API.api;
	
	u1 = list(set(u1));
	u2 = list(set(u2));

	commonfollowers = [];
	
	user1followerd = {};
	for i in u1:
		user1followerd[i] = 1;
		
	for i in u2:
		try:
			user1followerd[i];
			commonfollowers.append(i);
		except KeyError:
			1+1;
	rv = [];
	for i in commonfollowers:
		user = api.get_user(i)
		screenname = user.screen_name;
		profileimage = user.profile_image_url;
		description = user.description;
		location = user.location;
		friends = user.friends_count;
		followers = user.followers_count;
		username = user.name;
		tweetcount = user.statuses_count;
		bgimage = user.profile_background_image_url;
		rv.append([profileimage,screenname,description,location,friends,followers,username,tweetcount,bgimage]);
	return rv;