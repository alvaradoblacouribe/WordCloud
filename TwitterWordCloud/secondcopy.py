'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
Need!
Tweet file can be downloaded from here:
https://drive.google.com/open?id=1F7kzxvfidrwWmzExPty7QoW6eXwDTj7w
'''

from textblob import TextBlob
import json
import matplotlib.pyplot as plt
#Get the JSON data
tweetFile = open("/Users/girlswhocode/Desktop/gwc/GWCTestingSummer18/TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Selecting the tweets out of the data

#for tweet in range(len(tweetData)):
    #print("Tweet text: " + tweetData[tweet]["text"])
    #testimonial= TextBlob(tweetData[tweet]["text"])
    #print(testimonial.sentiment.polarity)
#ListTweets=[]
#def TweetsStrings():
    #for tweet in range(len(tweetData)):
        #Tweet= TextBlob(tweetData[tweet]["text"])
        #return(Tweet)
#ListTweets= TweetsStrings()

#ListTweets.append(Tweet)
print "-".join(tweetData)
#ListTweets= TweetsStrings()
#print(ListTweets)

TweetPolarity=tweetData.sentiment.polarity #X values
#The Histogram

plt.hist(TweetPolarity, [1,2,3,4], histtype = 'bar', facecolor='green')
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Polarity of Tweets")
plt.axis([-1.0,1.0,0,1000])
plt.grid(True)
plt.show()
