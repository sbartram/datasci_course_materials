import sys
import json
import re
from collections import defaultdict

empty = {}

def get_state(s):
    #print "s: ", s
    m = re.search('[^,]*,\s*([A-Z][A-Z])\s*$', s)
    if (m):
	return m.group(1)
    return None

def location(tweet):
    loc = None
    if ('place' in tweet):
    	if (tweet['place']):
	    if ('full_name' in tweet['place']):
		loc = get_state(tweet['place']['full_name'])
    if (not loc):
	if ('user' in tweet):
	    if ('location' in tweet['user']):
		loc = get_state(tweet['user']['location'])
    return loc

def main():

    skip = ['rt','a','an','and','of','to','the','is']
    states = defaultdict(int)

    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
	term, score  = line.split("\t")
	scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
	s = json.loads(line)
	# ignore non-tweets
	if ('text' in s):
	    state = location(s)
	    if (state):
		count = 0
		words = s['text'].split()
		for word in words:
		    word = word.lower().strip(' \'",\#')
		    if (not ((word in skip) | word.startswith('@'))):
			if (word in scores):
			    count += scores[word]
		#print state, count
		states[state] += count

    max = -99999
    maxstate = None
    for state in states.keys():
	if states[state] > max:
	    maxstate = state
	    max = states[state]
    print maxstate

if __name__ == '__main__':
    main()

