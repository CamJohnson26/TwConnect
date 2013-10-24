# WebpageFormatter.py
# Takes as input the results of calling twitterapi.getAPIInfo
# Returns a formatted webpage containing the information

def getFormattedWebpage(input):

	statuses = "";
	for i, v in enumerate(input):
		statuses = statuses + "<p>" + v + "</p>";

	webpage = '''
				<html>
					<head>
						<title>Hi There</title>
					</head>
					<body>
						<div>''' + statuses + '''</div>
					</body>
				</html>
				'''
	return webpage