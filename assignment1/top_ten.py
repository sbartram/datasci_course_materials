import sys
import json
from collections import defaultdict

def main():
    totals = defaultdict(int)
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
	s = json.loads(line)
	if ('text' in s):
	    for tag in s.get('entities', {}).get('hashtags'):
		totals[tag['text']] += 1

    for key in sorted(totals, key=totals.__getitem__, reverse=True)[0:10]:
	print key, totals[key] * 1.0

if __name__ == '__main__':
    main()
