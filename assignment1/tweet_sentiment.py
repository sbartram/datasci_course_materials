import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
	term, score  = line.split("\t")
	scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
	s = json.loads(line)
	if ('text' in s):
	    count = 0
	    words = s['text'].split()
	    for word in words:
		if (word in scores):
		    count += scores[word]
	    print count

if __name__ == '__main__':
    main()
