from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import json

from random import choice

import requests
import time

# SERVER_IP = 'localhost'
url_root = 'http://192.168.43.59/backdoor'

def blink(text = ''):

    base_mode = str(5)

    if 'hack' in text.lower():
        mode = '4'
    else:
        mode = '2'

    print('blinking with mode ', mode)

    r = requests.post(url_root, data={'playfile': mode})
    print('Changed mode {}: {}'.format(mode, r.reason))

    time.sleep(3)

    mode = base_mode
    r = requests.post(url_root, data={'playfile': mode})
    print('Changed mode {}: {}'.format(mode, r.reason))


class StdOutListener(StreamListener):

    def on_data(self, data):
        data_dict = json.loads(data)

        # pprint(data_dict)
        user = data_dict['user']['name']
        text = data_dict['text']

        print()
        print(user)
        print(text)

        blink(data_dict['text'])

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    print('Start')

    r = requests.post(url_root, data={'playfile': '5'})
    print('Changed to initial mode (0): {}'.format(r.reason))

    print('test initial blink')    
    blink()

    if True:
        #Variables that contains the user credentials to access Twitter API 
        access_token = ""
        access_token_secret = ""
        consumer_key = ""
        consumer_secret = ""

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['protopixel', 'hackaton', 'hackaton19', 'protopx', 'llumbcn19', 'llumbcn2019', 'llumbcn'])

    osc_terminate()    



