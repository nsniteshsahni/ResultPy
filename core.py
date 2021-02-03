import urllib2
import time
import tweepy
import os

# API keys decleration starts

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# declaration ends

date = 0101    # Date of result declaration
year = '2016'  # Your year of examination
tweet_string = 'twitter set @nsniteshsahni Result for %s %s declared.'
result_url = 'http://www.ipu.ac.in/exam/ExamResults/'
url = result_url + year + '/' + str(date) + year + '/027_CSE_5th%20Sem.pdf'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
t = tweepy.API(auth)
id_start = 2765
id_ = id_start
while True:
    url_socket = urllib2.urlopen(url % id_)
    temp = url_socket.read().lower()
    if temp.find('no such exam!!') < 0:
        if temp.find('computer') > 0:
            print(tweet_string % (id_, True))
            # os.system(tweet_string % (id_, True))
            os.system("vlc ~/01.mp3")
        else:
            print(tweet_string % (id_, False))
            # os.system(tweet_string % (id_, False))
        id_ += 1
    else:
        time.sleep(300)
