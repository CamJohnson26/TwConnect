from bottle import route, run, get, post, request, static_file
from WordCount.wordfrequencies import count_words, compare_freqs, count_words_string, count_words_array
import twitterapi
import WebpageFormatter
import createDiagram
import json
import alchemy_analyze
import datetime
import operator
from random import randint
import TweetObjects

f = open('html/index.html','r');
htmlfile = f.read()

@get('/index') # or @route('/login')
def index():
	return htmlfile;
    # return '''
#         <form action="/userinput" method="post">
#             User1 Twitter Handle: <input name="user1twittername" type="text" />
#             User2 Twitter Handle: <input name="user2twittername" type="text" />
#             <input value="Submit" type="submit" />
#         </form>
#     '''

@post('/userinput')
def index():
	
	user1name = request.forms.get('user1input');
	user2name = request.forms.get('user2input');
	
	try:
		f = open('storedjson/' +user1name[1:len(user1name)] + user2name[1:len(user2name)],'r');
		return f.read();
	except IOError:
		return getJSON(user1name, user2name);
		
def getJSON(user1name, user2name):	
	# Basic information
	user1twitterinfo = twitterapi.getAPIInfo(user1name);
	user2twitterinfo = twitterapi.getAPIInfo(user2name);
		
	# Word frequencies
	numberOfTweets = 200;
	user1statuses = twitterapi.getStatuses(user1name, numberOfTweets);
	user2statuses = twitterapi.getStatuses(user2name, numberOfTweets);
	
	u1statustexts = ""
	u1statusarray = [];
	for i in user1statuses:
		u1statustexts = u1statustexts + i.text.upper();
		u1statusarray.append(i.text.upper());
		
	u2statustexts = ""
	u2statusarray = [];
	for i in user2statuses:
		u2statustexts = u2statustexts + i.text.upper();
		u2statusarray.append(i.text.upper());
		
	hashtags = twitterapi.getHashtags(user1statuses);
	urls = twitterapi.getURLS(user1statuses);
	mentions = twitterapi.getUserMentions(user1statuses);
	media = twitterapi.getMedia(user1statuses);
	
	hashtags2 = twitterapi.getHashtags(user2statuses);
	urls2 = twitterapi.getURLS(user2statuses);
	mentions2 = twitterapi.getUserMentions(user2statuses);
	media2 = twitterapi.getMedia(user2statuses);
	
	
	# wordcount: How often each keyword is used
	u1wordcount = count_words_array(u1statusarray);
	u2wordcount = count_words_array(u2statusarray);
	
	# wordtweets: Maps a keyword to its related tweets
	u1wordtweets = u1wordcount['tweetindices'];
	u2wordtweets = u2wordcount['tweetindices'];
	
	# wordcloud: Combined list of keywords and frequencies
	wordcloud = compare_freqs(u1wordcount['frequencies'], u2wordcount['frequencies']);
	
	# Extract all entities into an array
	entities = {};
	
	user1entities = [];
	user2entities = [];
	
	finaltweetblock1 = u1statustexts;
	finaltweetblock2 = u2statustexts;
	
	while len(finaltweetblock1) > 0:
		currenttweetblock = finaltweetblock1[0:3000];
		finaltweetblock1 = finaltweetblock1[3001:];
		user1entities = user1entities + alchemy_analyze.extract_entities(currenttweetblock.encode("utf8"));

	while len(finaltweetblock2) > 0:
		currenttweetblock = finaltweetblock2[0:3000];
		finaltweetblock2 = finaltweetblock2[3001:];
		user2entities = user2entities + alchemy_analyze.extract_entities(currenttweetblock.encode("utf8"));
	
	print(user1entities);
	print(user2entities);
	for j in user1entities:
		try:
			entities[j['text'].upper()];
		except KeyError:
			entities[j['text'].upper()] = TweetObjects.Entity("", [], j['type'], 0, 0, 0, 0, 0)
		
		text = j['text'].upper();
		type = j['type'];
		frequency = entities[text].frequency + j['count'];
		#u1c = entities[text].user1count + j['count'];
		u1c = entities[text].user1count + 1;
		u2c = entities[text].user2count;
		u1f = u1c;
		u2f = u2c;
				
		entities[text.upper()] = TweetObjects.Entity(text, [], type, frequency, u1c, u2c, u1f, u2f);
	
	for j in user2entities:
		try:
			entities[j['text'].upper()];
		except KeyError:
			entities[j['text'].upper()] = TweetObjects.Entity("", [], j['type'], 0, 0, 0, 0, 0)
		
		text = j['text'].upper();
		type = j['type'];
		frequency = entities[text].frequency + j['count'];
		u1c = entities[text].user1count;
		#u2c = entities[text].user2count + j['count'];
		u2c = entities[text].user2count + 1;
		u1f = u1c;
		u2f = u2c;
		
		entities[text.upper()] = TweetObjects.Entity(text, [], type, frequency, u1c, u2c, u1f, u2f);
	
	for i in user1statuses:
		for j in entities:
			if i.text.upper().find(entities[j].text) != -1:
				entities[j].tweets.append(TweetObjects.Tweet(i.text, i.user.name, i.user.screen_name, i.id, i.created_at));
	
	for i in user2statuses:
		for j in entities:
			if i.text.upper().find(entities[j].text) != -1:
				entities[j].tweets.append(TweetObjects.Tweet(i.text, i.user.name, i.user.screen_name, i.id, i.created_at));
	
	# Catlist: Maps an alchemy category to the tweets associated with a keyword
	counter = 0;
	catkeyworddict = {};
	
	# Loop through all keywords
	for n in wordcloud:
		curtweets = "";
		curtweetobjects = [];
		for j in u1wordtweets[n[0]]:
			curtweets=curtweets + user1statuses[j].text;
			itext = user1statuses[j].text;
			iun = user1statuses[j].user.name;
			isn = user1statuses[j].user.screen_name;
			iid = user1statuses[j].id;
			idate = user1statuses[j].created_at;
			tweetobject = TweetObjects.Tweet(itext, iun, isn, iid, idate);
			curtweetobjects.append(tweetobject);
		for j in u2wordtweets[n[0]]:
			curtweets=curtweets + user2statuses[j].text;
			itext = user2statuses[j].text;
			iun = user2statuses[j].user.name;
			isn = user2statuses[j].user.screen_name;
			iid = user2statuses[j].id;
			idate = user2statuses[j].created_at;
			tweetobject = TweetObjects.Tweet(itext, iun, isn, iid, idate);
			curtweetobjects.append(tweetobject);
		cat = alchemy_analyze.get_category(curtweets.encode("utf8"));
		#cat = "SPORTS";
		if cat == 'arts_entertainment' or cat == 'gaming' or cat == 'recreation':
			cat = "entertainment";
		elif cat == 'sports':
			cat = "sports";
		elif cat == 'computer_internet' or cat == 'health' or cat == 'science_technology':
			cat = "technology";
		elif cat == 'culture_politics' or cat == 'business':
			cat = "politics";
		cat = cat.upper();
		if cat != 'NULL' and cat != 'UNKNOWN':
			tempn = [];
			try:
				tempn = catkeyworddict[cat];
			except KeyError:
				tempn = [];
				
			user1frequency = 0;
			for i in user1statuses:
				if i.text.upper().find(n[0]) != -1:
					user1frequency = user1frequency + 1;
			user2frequency = 0;
			for i in user2statuses:
				if i.text.upper().find(n[0]) != -1:
					user2frequency = user2frequency + 1;
				
			keyword = TweetObjects.Keyword(n[0], curtweetobjects, n[1], n[2], n[3], user1frequency, user2frequency);
			print(n[0]);
			print(user1frequency);
			print(user2frequency);
			tempn.append(keyword);
			catkeyworddict[cat] = tempn;
	
	largest = 0;
	for i in entities:
		if entities[i].frequency > largest:
			largest = entities[i].frequency;
			
	catdict = {};
	for i in entities:
		entities[i].user1count = float(entities[i].user1count) / float(largest);
		entities[i].user2count = float(entities[i].user2count) / float(largest);
		try:
			curcat = catdict[entities[i].type.upper()];
		except KeyError:
			curcat = TweetObjects.Category(entities[i].type.upper());
		curcat.addEntity(entities[i]);
		catdict[entities[i].type.upper()] = curcat;
	
	for key in catkeyworddict:
		try:
			curcat = catdict[key];
		except KeyError:
			curcat = TweetObjects.Category(key);
		for i in catkeyworddict[key]:
			curcat.addKeyword(i);
		catdict[key] = curcat

	# Make sure we have 4 categories
	try:
		catdict['SPORTS'];
	except KeyError:
		catdict['SPORTS'] = TweetObjects.Category('SPORTS');
	try:
		catdict['ENTERTAINMENT'];
	except KeyError:
		catdict['ENTERTAINMENT'] = TweetObjects.Category('ENTERTAINMENT');
	try:
		catdict['POLITICS'];
	except KeyError:
		catdict['POLITICS'] = TweetObjects.Category('POLITICS');
	try:
		catdict['TECHNOLOGY'];
	except KeyError:
		catdict['TECHNOLOGY'] = TweetObjects.Category('TECHNOLOGY');
		
	catlist = [];
	#for key in catdict:
	#	catlist.append(catdict[key]);
	catlist.append(catdict["SPORTS"]);
	catlist.append(catdict["POLITICS"]);
	catlist.append(catdict["TECHNOLOGY"]);
	catlist.append(catdict["ENTERTAINMENT"]);
		
	catlistformats = [];
	for i in catlist:
		catlistformats.append(i.getJSON());
	catlistjson = catlistformats;
	
	for i in catlist:
		#i.sort();
		print i.category
		for j in i.keywords:
			print("\t" + j.keyword);
			for k in j.tweets:
				print("\t\t" + str(k.tweetid));
		for j in i.entities:
			print("\t" + j.text);
			for k in j.tweets:
				print("\t\t" + str(k.tweetid));
	
	for i in entities:
		normfreq = float(entities[i].frequency) / float(largest);
		try:
			wordcloud.append([i, normfreq, entities[i].user1count,entities[i].user2count])
		except ZeroDivisionError:
			entities[i] = 0;
	
	hashtagcloud = compare_freqs(count_words([hashtags])['frequencies'], count_words([hashtags2])['frequencies']);
	if len(hashtagcloud) == 0:
		hashtagcloud.append(["No Common Hashtags", 0.001]);	
	for j in hashtagcloud:
		wordcloud.append(j);
	
	# Followers
	commonFollowers = twitterapi.getCommonFollowers(user1name, user2name);
	commonMentions = twitterapi.getCommonPeople(mentions, mentions2);
	
	vennDiagram = createDiagram.createVenn(user1twitterinfo['friends_count'],user2twitterinfo['friends_count'],len(commonFollowers),user1name,user2name);
	
	user1image = user1twitterinfo['profile_image_url'];
	user2image = user2twitterinfo['profile_image_url'];
	
	u1tweetcount = user1twitterinfo['tweet_count'];
	u2tweetcount = user2twitterinfo['tweet_count'];
	
	u1displayname = user1twitterinfo['user_name']
	u2displayname = user2twitterinfo['user_name']
	
	u1bg = user1twitterinfo['background']
	u2bg = user2twitterinfo['background']

	#return "<table border=\"1\"><tr>" + unicode(user1twitterinfo) + unicode(user2twitterinfo) + "</tr></table>";
	#return vennDiagram + WebpageFormatter.arrayToTable(commonFollowers);
	#return wordcloud + "<span>helloworld</span>";

	jsondata = json.dumps({"categorylist" : catlistjson,"user1background" : u1bg,"user2background" : u2bg,"user1tweetcount" : u1tweetcount,"user2tweetcount": u2tweetcount,"user1displayname" : u1displayname,"user2displayname" : u2displayname, "user1image" : user1image, "user2image" : user2image,"user1description" : user1twitterinfo['description'], "user2description" : user2twitterinfo['description'],"user1location" : user1twitterinfo['location'], "user2location" : user2twitterinfo['location'], "user1followercount" : user1twitterinfo['followers_count'], "user2followercount" : user2twitterinfo['followers_count'], "user1friendcount" : user1twitterinfo['friends_count'], "user2friendcount" : user2twitterinfo['friends_count'], "commonfollowercount" : len(commonFollowers), "user1name" : user1name, "user2name" : user2name, "commonfollowers" : commonFollowers,"commonmentions" : commonMentions , "wordcloud" : wordcloud, "hashtagcloud" : hashtagcloud, "urls" : urls + urls2, "media1" : media, "media2" : media2, "numberOfTweets" : numberOfTweets});

	f = open('storedjson/' +user1name[1:len(user1name)] + user2name[1:len(user2name)],'w');
	f.write(jsondata);
	f.close();
	
	return jsondata;

@get('/html/<filename:path>',name='html')
@route('/html/<filename:path>', name='html')
def html(filename):
    return static_file(filename, root='html')

@get('/<filename:path>',name='html')
@route('/<filename:path>', name='html')
def html(filename):
    return static_file(filename, root='.')
    
run(host='localhost', port=8080, debug=True)