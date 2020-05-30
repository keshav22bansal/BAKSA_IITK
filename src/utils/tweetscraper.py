from bs4 import BeautifulSoup
import requests
import fileinput
import emoji

all_tags = {"N":"0", "NONE":"1", "P":"2"}
cnt = 0
f_out = open("spanglish_train_converted.txt", "a")
# https://twitter.com/anyuser/status/id

with open("spanglish_tweets_corpus", "r") as f:
	line = f.readline()
	while (line):
		line = line.split()
		if (len(line) >= 2):
			tweet_id = line[0]
			tweet_tag = all_tags[line[1]]
			page = requests.get("https://twitter.com/anyuser/status/"+str(tweet_id))
			soup = BeautifulSoup(page.content, 'html.parser')
			elem = soup.find("p", {"class" : "TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text"})
			if elem:
				#print(elem.findAll(text=True))
				tweet_text = "".join(elem.findAll(text=True)).replace('\n', '').replace('\r', '').replace('\t', '')
				tweet_emojis = "".join(list(map(lambda x: x.get("alt"), elem.findAll("img"))))
				#print(str(cnt)+'\t'+tweet_text + tweet_emojis+'\t'+str(tweet_tag)+'\t'+str(tweet_tag))
				f_out.write(str(cnt)+'\t'+tweet_text + tweet_emojis+'\t'+str(tweet_tag)+'\t'+str(tweet_tag)+'\n')
				print(str(cnt)+'\t'+str(tweet_id))
				cnt += 1
		line = f.readline()

f_out.close()