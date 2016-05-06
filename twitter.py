# -*- coding: utf-8 -*-
"""
First attempt at mining from Twitter's social media data
Created on Tue Apr 19 17:01:18 2016

Consumer Key (API Key)	UpYK7f6BuJq7HC9q9rgkrcoSt
Consumer Secret (API Secret)	DbDvK68LcrRml5hCXp9XT9BebfeDy6wFVJ1iNIwIQQRkb7y26m
Access Level	Read and write (modify app permissions)
Owner	xalapao
Owner ID	48219109

Access Token	48219109-2Bcy9An5xPfGZQkJ775jvrxXXWFDjDNQDJrCfaRe7
Access Token Secret	wvn5m5Z6DLT1ebX9OfhB1HjCptSkD7voEqE2Ugwnggnp4

@author: psinchaisri
"""

import tweepy
import json
import nltk

from tweepy import OAuthHandler

consumer_key = 'UpYK7f6BuJq7HC9q9rgkrcoSt'
consumer_secret = 'DbDvK68LcrRml5hCXp9XT9BebfeDy6wFVJ1iNIwIQQRkb7y26m'
access_token = '48219109-2Bcy9An5xPfGZQkJ775jvrxXXWFDjDNQDJrCfaRe7'
access_secret = 'wvn5m5Z6DLT1ebX9OfhB1HjCptSkD7voEqE2Ugwnggnp4'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    process_or_store(status._json) 