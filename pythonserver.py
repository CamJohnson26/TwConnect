from bottle import route, run, get, post, request
import twitterapi
import WebpageFormatter

@get('/index') # or @route('/login')
def index():
    return '''
        <form action="/userinput" method="post">
            Twitter Handle: <input name="twittername" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/userinput')
def index():
	twitterinfo = twitterapi.getAPIInfo(request.forms.get('twittername'));
	return WebpageFormatter.getFormattedWebpage(twitterinfo);

run(host='localhost', port=8080, debug=True)