import sys
import json

def main():

    skip = ['rt','a','an','and','of','to','the','is']
    wordCount = {}
    totalCount = 0.0

    tweet_file = open(sys.argv[1])
    for line in tweet_file:
	s = json.loads(line)
	# ignore non-tweets
	if ('text' in s):
	    words = s['text'].split()
	    for word in words:
		word = word.lower().strip(' \'",\#')
		if (not ((word in skip) | word.startswith('@'))):
		    totalCount += 1
		    if (word in wordCount):
			wordCount[word] += 1
		    else:
			wordCount[word] = 1

    words = wordCount.keys()
    words.sort()
    for word in words:
	avg = wordCount[word] / totalCount
    	print word, avg

if __name__ == '__main__':
    main()

