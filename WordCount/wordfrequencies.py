from collections import Counter
from nltk.tokenize import word_tokenize

## Read the input text and break it into words
def count_words(n):
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
			
			print(truncm);
			
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
	print(differences);
	print(freqs);
			
	sortedd = [];
	for w in sorted(finallist, key=finallist.get, reverse=True):
		sortedd.append({w : finallist[w]});
	for i in sortedd:
		print(i)