# WebpageFormatter.py
# Takes as input the results of calling twitterapi.getAPIInfo
# Returns a formatted webpage containing the information

def getFormattedWebpage(input1, input2):
	return unicode(input1) + unicode(input2);

def arrayToTable(input):
	rv = "<table>";
	for i in input:
		rv = rv + "<tr><td>"+i+"</td></tr>";
	return rv;
	
def getWordCloud(input, tagName):
	## Turn the text into a javascript file
	f = open('html/d3-cloud/examples/simple.html','rw');
	htmlpage = unicode(f.read());
	
	wordlisted = "[";
	countlisted = "";
	for i in input:
		wordlisted = wordlisted + "\"" + i + "\", ";
		countlisted = countlisted + "\"" + '%.5f' % input[i]  + "\", ";
	
	wllist = len(wordlisted);
	if wllist > 2:
		wordlisted = wordlisted[0:wllist - 2];
		countlisted = countlisted[0:len(countlisted) - 2];		
	wordlisted += "]";
	
	## Write to the javascript file
	countstart = htmlpage.find('{{{WORDS}}}');
	tagstart = htmlpage.find('{{{TAG}}}');
	wordstart = htmlpage.find('{{{COUNTS}}}');
	
	htmlpage2 = htmlpage[0:wordstart] + countlisted + htmlpage[wordstart + 12:countstart] + wordlisted + htmlpage[countstart + 11: tagstart] +"\"" +tagName+ "\"" + htmlpage[tagstart + 9:len(htmlpage)];
	f.close();
	
	return htmlpage2;