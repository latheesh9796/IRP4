import json
import tweepy
import datetime as dt
import time
import os
import sys
import pprint
import re
import config

from twitter import tweepy
from tweepy import OAuthHandler

# handle = {
# 	"USA": ["HillaryClinton","BernieSanders","BenSasse","KamalaHarris","JoeBiden"],
# 	"INDIA": ["narendramodi","RahulGandhi","ShashiTharoor","ArvindKejriwal","Swamy39"],
# 	"BRAZIL": ["dilmabr","CarlosBolsonaro","Haddad_Fernando","cirogomes","jairbolsonaro"]
# }

# for handle in handle["USA"]:
handle="myogiadityanath"
max_tweets = 3000

result = {}

if __name__ == "__main__":
	tweepy.initialize(1)
	tweets = tweepy.collect_tweets(handle, max_tweets)
	# replies = tweepy.collect_replies(handle)
	result["tweets"]=tweets
	with open("/Users/latheesh/Downloads/Project_1-Shasha/data/tweets/" + handle + "_replies.json", "a+", encoding="utf8") as f:
		json.dump(result, f,ensure_ascii=False)


	# with open("data/tweets/" + handle + ".json","r",encoding="utf8") as f:
	# 	result=json.load(f,ensure_ascii=False)

	# result["replies"] = replies

	# with open("data/tweets/" + handle + ".json", "w", encoding="utf8") as f:
	# 	json.dump(result, f,ensure_ascii=False)
