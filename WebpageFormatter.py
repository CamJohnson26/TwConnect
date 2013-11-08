# WebpageFormatter.py
# Takes as input the results of calling twitterapi.getAPIInfo
# Returns a formatted webpage containing the information

def getFormattedWebpage(input1, input2):
	fileHandle = open('html/template.html','r');
	str1 = fileHandle.read();
	fileHandle.close();
	
	status1index = str1.find("{{{statuses 1}}}", 0, len(str1));
	status2index = str1.find("{{{statuses 2}}}", 0, len(str1));
	
	webpagestart1 = str1;
	webpageend1 = "";
	
	if status1index != -1:
		webpagestart1 = str1[0:status1index];
		webpageend1 = str1[status1index:status2index];
		
	webpageend2 = "";
	
	if status2index != -1:
		webpageend2 = str1[status2index:len(str1)];
	
	webpage = webpagestart1 + input1 + webpageend1 + input2 + webpageend2;
	return webpage;