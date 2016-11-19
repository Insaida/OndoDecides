#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "334666101-XMyXeLXcgSc8NdkCm4aaQIZpoDTYbAOQJ4TvQASm"
access_token_secret = "mGLnqWUAaiMF1CcIYihBiUMrm2K5ofHLs6HeiBAvMpHLV"
consumer_key = "CO96QF8nawbiBdAZqpzER293s"
consumer_secret = "Hh8a8awImJslPQuF5SxtdpsSfrqFwyxTNPpHJrQ9pufKUffOgJ"

 #This handles Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print "Error on _data: %s ";             
        return True


    def on_error(self, status):
        print status
        return True

if __name__ == '__main__':

       l = StdOutListener()
       stream = Stream(auth, l)
       stream.filter(track=['#BallotLive', '#OndoDecides', 'Nigeria', 'Akeredolu', 'Aketi', 'PDP', 'APC'])

