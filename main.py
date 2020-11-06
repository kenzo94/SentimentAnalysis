#import libraries
import pandas as pd
import csv
import tweepy
from tweepy import OAuthHandler

#twitter credentials
consumer_key = "pvjiXZ4ojM4lf6fkMNDDWCfMl"
consumer_secret = "VRps2wCrowQtt3PsVRm2fXt2K4OUA3MXhvONex7fdPapHyxlj3"
access_token = "1298262098124787713-0ahmPtCpMAFtenOcv1gEHnlGDexTFq"
access_secret = "2dCzzBJRl0I6C9fl8zTFhqBIybeI1n6uu1uNK0oNK7EDT"

#Authenticate credentials
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

corpus_file = open("corpus_v1.0.tsv","r+")
read_tsv = csv.reader(corpus_file, delimiter="\t")

list = []


for row in read_tsv:
    try:
        tweet = api.get_status(int(row[0]))
        print(tweet.text)
        row[0] = tweet.text
        list.append(row[0:2])
    except tweepy.error.TweepError as e:
        print(e)

corpus_file.close()

with open('test.tsv', 'wt', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for row in list:
        tsv_writer.writerow(row)



