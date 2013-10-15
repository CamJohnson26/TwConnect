import tweepy, urllib2
from bottle import route, run, template

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="mflJ0zhrutRVCk35emOQ"
consumer_secret="MYMT6oxERQcduEf5KZiHNkj66nzrcgO9bLjsHvJmAg"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="152181424-rnFWgXq9QcViENymDfoDwo2AeLfEPGkgSFmWXoJn"
access_token_secret="oVddejjnJfxkV9nMy6m97O3pbf8jQCdnoOsfTXnU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@route('/hello/<name>')
def index(name='index'):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

## If the authentication was successful, you should
## see the name of the account print out
list = api.user_timeline("@mostlyharmlessz");

url = "http://classify.knilab.com/classify/text/linear/";

for i in list:
	values = "input=" + i.text;

	headers = {'Content-Type': 'application/x-www-form-urlencoded' }

	req = urllib2.Request(url, values, headers)
	response = urllib2.urlopen(req)
	the_page = response.read()

	print(the_page[0:30], i.text);
	response.close()
	
# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps