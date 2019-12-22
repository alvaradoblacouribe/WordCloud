'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
Need!
Tweet file can be downloaded from here:
https://drive.google.com/open?id=1F7kzxvfidrwWmzExPty7QoW6eXwDTj7w
'''
from wordcloud import WordCloud
from os import path
from textblob import TextBlob
import json
import matplotlib.pyplot as plt
#Get the JSON data
tweetFile = open("/Users/icalvaradoblanco/Desktop/gwc/otherWork/TwitterData/WordCloud/TwitterWordCloud/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


#Step 1: Graph the polarity

# Selecting the tweets out of the data

def TweetsStrings():
    TweetStringList=[]
    for tweet in range(len(tweetData)):
        Tweet= (tweetData[tweet]["text"])
        TweetStringList.append(Tweet)
    return TweetStringList


#Calculating Polarity of TweetString

def PolarityofTweets(TweetStringList):
    TweetPolarity=[]
    for tweet in range(len(TweetStringList)):
        testimonial= TextBlob(TweetStringList[tweet])
        Polarity= testimonial.sentiment.polarity
        TweetPolarity.append(Polarity) #X values
    return(TweetPolarity)

#Step 2: Visualize the tweetData

#Getting the frequencies of words
def TopWords(TweetStringStringB): #freq>10
    print("----------------------")
    Popularity=[]
    for tweet in range(len(TweetStringStringB.words)):
        word= TweetStringStringB.words[tweet]
        numberpopularity=(TweetStringStringB.word_counts[word])
        if (numberpopularity>5):
            if (word!='https'):
                if word.isalpha():
                    Popularity.append(word)
    return(Popularity) #You want redundancy to see the frequency in the wordcloud


#Making the Word Cloud
def MakeWordCloud(filename):
    d = path.dirname(__file__)
    text = open(path.join(d,filename)).read() #Reads the file
    wordcloud = WordCloud().generate(text) #Generates the WordCloud
    #This displays the image
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    #This deals with font size
    plt.show()

#Let's make wordclouds for positive,neutral,and negative
def PositiveWords(TweetStringStringB,TweetStringString):
    PositiveWords=[]
    for tweet in range(len(TweetStringStringB.words)):
        word=(TweetStringStringB.words[tweet])
        if (word.isalpha()):
            word=TextBlob(word)
            polarityofword= word.sentiment.polarity
            word=(TweetStringStringB.words[tweet])
            if ((polarityofword>0.3)) :
                PositiveWords.append(word)
    return PositiveWords


def NeutralWords(TweetStringStringB,TweetStringString):
    NeutralWords=[]
    for tweet in range(len(TweetStringStringB.words)):
        word=TweetStringStringB.words[tweet]
        if (word!='https'):
            if (word.isalpha()):
                word=TextBlob(word)
                polarityofword= word.sentiment.polarity
                word=(TweetStringStringB.words[tweet])
                if ((polarityofword<0.3) & (polarityofword>-0.3)):
                        NeutralWords.append(word)
    return NeutralWords

def NegativeWords(TweetStringStringB,TweetStringString):
    NegativeWords=[]
    for tweet in range(len(TweetStringStringB.words)):
        word=TweetStringStringB.words[tweet]
        if(word.isalpha()):
            word=TextBlob(word)
            polarityofword= word.sentiment.polarity
            word=(TweetStringStringB.words[tweet])
            if ((polarityofword<-0.3)) :
                print("NEGATIVE YEAH")
                NegativeWords.append(word)
    return NegativeWords


#Flow

#gets the tweet text
TweetStringList= TweetsStrings()
#polarity of tweets
TweetPolarity= PolarityofTweets(TweetStringList)
#graphs the polarity in a Histogram
plt.hist(TweetPolarity,100, facecolor='green')
plt.xlabel("Polarity")
plt.ylabel("Number of Tweets")
plt.title("Polarity of Tweets")
plt.axis([-1.0,1.0,0,50])
plt.show()
#Makes tweets into TextBlobs
TweetStringString= " ".join(TweetStringList)
TweetStringStringB= TextBlob(TweetStringString)
#gets the most popular words and storing them
Popularity=" ".join(TopWords(TweetStringStringB))
f= open("PopularityStringGeneral.txt","w+")
f.write(Popularity)
#popularity of neutral words 
NeutralWords= NeutralWords(TweetStringStringB,TweetStringString)
NeutralWords= " ".join(NeutralWords)
f= open("PopularityNeutralWords.txt","w+")
f.write(NeutralWords)
#popularity of negative words 
NegativeWords=NegativeWords(TweetStringStringB,TweetStringString)
NegativeWords= " ".join(NegativeWords)
f= open('PopularityNegativeWords.txt',"w+")
f.write(NegativeWords)
#Popularity of the word clouds 
print("POSITIVE")
MakeWordCloud('PopularityPositiveWords.txt')
print("NEUTRAL")
MakeWordCloud('PopularityNeutralWords.txt')

#currently not working as expected 
#MakeWordCloud('PopularityNegativeWords.txt')

