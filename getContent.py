
import tweepy
import json
import logging
import sys


def get_content(id):
    CONSUMER_KEY = "4ZUXGrPK7swSneS3tpibBFRFp"
    CONSUMER_SECRET_KEY = "OQQlshl7PPELMPrkpbG3FJE5CFh7fk535E5xGxx2NH5bOMPFPh"
    ACCESS_TOKEN_KEY = "1457316110630797313-bsvQ61zmn08lTDtbdSSuu1NWs3wd78"
    ACCESS_TOKEN_SECRET_KEY = "sSto2S9kVFsi9kA7OYtK7UdApolqSLT9NQUvC5UM9cpck"
    with open('api_keys.json', 'w') as outfile:
        json.dump({
            "consumer_key": CONSUMER_KEY,
            "consumer_secret": CONSUMER_SECRET_KEY,
            "access_token": ACCESS_TOKEN_KEY,
            "access_token_secret": ACCESS_TOKEN_SECRET_KEY
        }, outfile)
    # auth = OAuthHandler(consumer_key,consumer_secret)
    # auth.set_access_token(access_token,access_token_secret)
    # The lines below are just to test if the twitter credentials are correct
    # Authenticate

    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # api.search_tweets()
    if (not api):
        print("Can't Authenticate")
        sys.exit(-1)
    origin_result = []
    # public_tweets = api.user_timeline(screen_name='LeoDiCaprio')
    # for tweet in public_tweets:
    # print (tweet.text)
    status = api.get_status(id, tweet_mode="extended")
    # re_tweet_ = api.retweets(id)
    try:
        result=status.retweeted_status.full_text
    except AttributeError:
        result=status.full_text
    result=str(result)
    # print(result)
    r_index=result.split("https")
    print(r_index)
    print(r_index[0])
    return  r_index[0]



