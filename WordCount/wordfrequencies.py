from collections import Counter
import nltk, string
from nltk.tokenize import word_tokenize
import datetime
from operator import itemgetter

## Read the input text and break it into words
def count_words_array(n):
	remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

	n[:] = [i.translate(remove_punctuation_map) for i in n];
	n[:] = [word_tokenize(i) for i in n];

	return count_words(n);

def count_words_string(n):
	remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
	words = n.translate(remove_punctuation_map)
	words = word_tokenize(words)
	return count_words([words]);
	
def count_words(n):
	words = n
	tweetindex = 0;
	keywordtweetindices = {};
	freq = {};
	
	for i in words:
		c = Counter(i)
		for j in c:
			tempn = []
			try:
				tempn = keywordtweetindices[j];
			except KeyError:
				tempn = [];
			tempn.append(tweetindex);
			keywordtweetindices[j] = tempn;
			try:
				freq[j] += c[j];
			except KeyError:
				freq[j] = c[j];
		tweetindex += 1;
					
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
	return {"frequencies" : sortedd, "tweetindices" : keywordtweetindices};
	
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
	
	returnlist = [];
	for key in finallist:
		returnlist.append([key, finallist[key], float(m[key]), float(n[key])]);
	
	# Sort and normalize the return values
	returnlist = sorted(returnlist, key=itemgetter(1));
	for i in returnlist:
		try:
			i[1] = i[1] / returnlist[len(returnlist) - 1][1];
		except ZeroDivisionError:
			i[1] = 0;
	
	# Return the user 1 and user 2 percentages
	returnlist = sorted(returnlist, key=itemgetter(2));
	for i in returnlist:
		try:
			i[2] = i[2] / returnlist[len(returnlist) - 1][2];
		except ZeroDivisionError:
			i[2] = 0;
	returnlist = sorted(returnlist, key=itemgetter(3));
	for i in returnlist:
		try:
			i[3] = i[3] / returnlist[len(returnlist) - 1][3];
		except ZeroDivisionError:
			i[3] = 0;
	return returnlist;
	
# 	differences = sorted(differences);
# 	freqs = sorted(freqs);
# 	
# 	sortedd = [];
# 	for w in sorted(finallist, key=finallist.get, reverse=True):
# 		sortedd.append({w : finallist[w]});