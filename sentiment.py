# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

class Sentiment:
    def __init__(self) -> None:
        return
    def split_on_sentences(self,text,searchFor = None):
        if len(searchFor) == 0:
            searchFor = None
        m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
        if searchFor is None:
            return m
        else:
            find_list = []
            for s in m:
                if re.search(searchFor.lower(),s.lower()):
                    find_list.append(s)
            return find_list
    # function to print sentiments
    # of the sentence.
    def sentiment_scores(self,sentence):
     
        # Create a SentimentIntensityAnalyzer object.
        sid_obj = SentimentIntensityAnalyzer()
     
        # polarity_scores method of SentimentIntensityAnalyzer
        # object gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = sid_obj.polarity_scores(sentence)
        ''' 
        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
     
        print("Sentence Overall Rated As", end = " ")
        
        # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05 :
            print("Positive")
     
        elif sentiment_dict['compound'] <= - 0.05 :
            print("Negative")
     
        else :
            print("Neutral")
        '''
        
        return sentiment_dict
 