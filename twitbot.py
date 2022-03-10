import tweepy
import webbrowser
import time

api_key="jZyFze427zvNEqIaL0GhAtzfZ"
api_secret="y3ulE8rx7Ulq6AREuc8sWCuo2eAfsIpmiCYxZ5NkooK3UbNk14"
access_token="1438647874947006465-HBQAeDsWZPy6rdxFtnDwwqzo6q7xb4"
access_secret="pItbvdLKFZa8s4Y3qOHZ5lm5i4s4wvParVG0UwLq8Cm8L"
bearer_token="AAAAAAAAAAAAAAAAAAAAAIEKZwEAAAAA7Wsk%2BSJWU7Uzmml%2FuOToKlZbCBQ%3DCNmVZLABgKcw8Jio2uz0OSY77wgloWXGpTOGprX5k5xgAqQS2Q"
            
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_secret)
api.create_tweet(text="This was tweeted from a bot. Just testing some Twitter API shit.")