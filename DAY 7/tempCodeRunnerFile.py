import tweepy
import time

auth = tweepy.OAuthHandler('api key','api secret key')
auth.set_access_token('Access token ','Access token secret')


api=tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

print(user.screen_name)


for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
    #if follower.name=='name':
        #follower.follow()   #follows back


search='Python'
numTweets=50

for tweet in tweepy.Cursor(api.search,search).items(numTweets):
    try:
        print('Tweet Liked')
         print('Tweet Retweeted')
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break