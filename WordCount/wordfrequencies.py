from collections import Counter
import nltk, string
from nltk.tokenize import word_tokenize
import datetime

## Read the input text and break it into words
def count_words(n):
	remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
	words = [n.translate(remove_punctuation_map)]
	
	words = word_tokenize(n)
	freq = Counter(words)
	
	length = float(len(freq));
	for key in freq:
		freq[key] = '%.10f' % float(freq[key] / length);
	
	##print(freq);
	
	## Figure out the global frequencies
	f = open('wordlist','r');
	worldwords = f.read().split("\n")
	worldworddict = {};
	
	for i in worldwords:
		i = i.split("\t")
		worldworddict[i[0]] = i[1];
	
	## Filter out common words
	listything = [];
	for key in freq:
		try:
			freq[key] = '%.10f' % (float(freq[key]) - float(worldworddict[key]));
		except KeyError:
			listything.append(key);
	
	## Apply the Blacklist
	f = open('blacklist','r')
	blacklista = f.read().split("\n")
	blacklist = {};
	for i in blacklista:
		blacklist[i] = "YES";
	
	for key in blacklist:
		if key in freq:
			del freq[key]
		
	
	## Sort our results by frequency
	sortedd = {};
	for w in sorted(freq, key=freq.get, reverse=True):
		sortedd[w] = freq[w];
	
	return sortedd;
	
def compare_freqs(m,n):
	
	differences = [];
	freqs = [];
	
	finallist = {};
	for key in m:
		if key in n:
			truncm = float(m[key]);
			truncn = float(n[key]);
						
			diff = abs(truncm - truncn);
			freq = (truncm + truncn);
			
			differences.append({ '%.5f' % diff : key });
			freqs.append({'%.5f' % freq : key });
			
			try:
				finallist[key] = (freq - diff);
			except ZeroDivisionError:
				finallist[key] = float(0);
	
	differences = sorted(differences);
	freqs = sorted(freqs);
	#print(differences);
	#print(freqs);
	
	sortedd = [];
	for w in sorted(finallist, key=finallist.get, reverse=True):
		sortedd.append({w : finallist[w]});
	for i in sortedd:
		print(i)
	
	## Turn the text into a javascript file
	f = open('d3-cloud/examples/simple.html','rw');
	htmlpage = f.read();
	
	wordlisted = "[";
	countlisted = "";
	for i in finallist:
		wordlisted = wordlisted + "\"" + i + "\", ";
		countlisted = countlisted + "\"" + '%.5f' % finallist[i]  + "\", ";
	
	wllist = len(wordlisted);
	if wllist > 2:
		wordlisted = wordlisted[0:wllist - 2];
		countlisted = countlisted[0:len(countlisted) - 2];		
	wordlisted += "]";
	
	## Write to the javascript file
	countstart = htmlpage.find('{{{WORDS}}}');
	wordstart = htmlpage.find('{{{COUNTS}}}');
	
	htmlpage2 = htmlpage[0:wordstart] + countlisted + htmlpage[wordstart + 12:countstart] + wordlisted + htmlpage[countstart + 11:len(htmlpage)];
	f.close();
	
	fname = 'd3-cloud/examples/' + str(datetime.date) + str(datetime.time) + '.html';
	f = open(fname,'w');

	f.truncate();
	f.write(htmlpage2);
	f.close();