# WebpageFormatter.py
# Takes as input the results of calling twitterapi.getAPIInfo
# Returns a formatted webpage containing the information

def getFormattedWebpage(input):
	fileHandle = open('html/template.html','r');
	str1 = fileHandle.read();
	fileHandle.close();
	
	index = str1.find("{{{statuses}}}", 0, len(str1));
	
	webpagestart = str1;
	webpageend = "";
	
	if index != -1:
		webpagestart = str1[0:index];
		webpageend = str1[index:len(str1)];
	
	statuses = "";
	for i, v in enumerate(input):
		statuses = statuses + "<p>" + v + "</p>";
	
	webpage = webpagestart + statuses + webpageend;
	return webpage;