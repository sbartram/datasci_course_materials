import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {}
    for line in sent_file:
	term, score  = line.split("\t")
	scores[term] = int(score)

    skip = ['rt','a','an','and','of','to','the','is']
    totalScore = {}
    tweets = {}

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
	s = json.loads(line)
	# ignore non-tweets
	if ('text' in s):
	    tweetScore = 0
	    missingWords = []
	    words = s['text'].split()
	    for word in words:
		word = word.lower().strip(' \'",\#')
		if (not ((word in skip) | word.startswith('@'))):
		    if (word in scores):
			tweetScore += scores[word]
		    else:
			missingWords.append(word)
	    #print tweetScore
	    for word in missingWords:
		#print "missing ", word
		if (word in totalScore):
		    totalScore[word] += tweetScore
		    tweets[word] += 1
		else:
		    totalScore[word] = tweetScore
		    tweets[word] = 1

    words = totalScore.keys()
    words.sort()
    for word in words:
	avg = totalScore[word] / tweets[word]
    	print word, avg

if __name__ == '__main__':
    main()

