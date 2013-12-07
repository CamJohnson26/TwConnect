import json
import operator

class Category:

	# Allowed: entertainment, sports, technology, politics
	category = "unknown";
	keywords = [];
	entities = [];
	def __init__(self, cat):
		self.category = cat;
		self.keywords = [];
		self.entities = [];
	
	def addKeyword(self, keyword):
		self.keywords.append(keyword);
	
	def addEntity(self, entity):
		self.entities.append(entity);
	
	def getJSON(self):
		jsonkeywordlist = [];
		jsonentitylist = [];
		for i in self.keywords:
			jsonkeywordlist.append(i.getJSON());
		for i in self.entities:
			jsonentitylist.append(i.getJSON());
		return {'category' : self.category, 'keywords' : jsonkeywordlist, 'entities' : jsonentitylist};
# 	def sort(self):
# 		self.keywords = sorted(self.keywords, key=operator.attrgetter('frequency'));
# 		self.entities = sorted(self.keywords, key=operator.attrgetter('frequency'));

class Entity:
	text = "";
	type = "";
	frequency = 0;
	user1count = 0;
	user2count = 0;
	tweets = [];
	user1frequency = 0;
	user2frequency = 0;
	
	def __init__(self, itext, itweets, itype, ifrequency, iu1c, iu2c, iu1f, iu2f):
		self.text = itext;
		self.tweets = itweets;
		self.type = itype;
		self.frequency = ifrequency;
		self.user1count = iu1c;
		self.user2count = iu2c;
		self.user1frequency = iu1f;
		self.user2frequency = iu2f;
	
	def getJSON(self):
		jsontweetlist = [];
		for i in self.tweets:
			jsontweetlist.append(i.getJSON());
		return {'text' : self.text, 'type' : self.type, 'frequency' : unicode(self.frequency), 'tweets' : jsontweetlist, 'user1count' : unicode(self.user1count), 'user2count' : unicode(self.user2count), 'user1frequency' : unicode(self.user1frequency), 'user2frequency' : unicode(self.user2frequency),};
	

class Keyword:
	keyword = "unknown";
	frequency = 0;
	user1count = 0;
	user2count = 0;
	tweets = [];
	user1frequency = 0;
	user2frequency = 0;
	
	def __init__(self, ikeyword, itweets, ifrequency, iu1c, iu2c, iu1f, iu2f):
		self.keyword = ikeyword;
		self.tweets = itweets;
		self.frequency = ifrequency;
		self.user1count = iu1c;
		self.user2count = iu2c;
		self.user1frequency = iu1f;
		self.user2frequency = iu2f;
	
	def getJSON(self):
		jsontweetlist = [];
		for i in self.tweets:
			jsontweetlist.append(i.getJSON());
		return {'keyword' : self.keyword, 'frequency' : unicode(self.frequency), 'tweets' : jsontweetlist, 'user1count' : unicode(self.user1count), 'user2count' : unicode(self.user2count), 'user1frequency' : unicode(self.user1frequency), 'user2frequency' : unicode(self.user2frequency)};

class Tweet:
	text = "";
	user_name = "";
	screen_name = "";
	tweetid = 0;
	date = "";
	
	def __init__(self, itext, iun, isn, iid, idate):
		self.text = itext;
		self.user_name = iun;
		self.screen_name = isn;
		self.tweetid = iid;
		self.date = idate;
	
	def getJSON(self):
		return {'text' : self.text, 'user_name' : self.user_name, 'screen_name' : self.screen_name, 'tweetid' : unicode(self.tweetid), 'date' : unicode(self.date)};