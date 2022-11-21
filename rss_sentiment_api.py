from fastapi import FastAPI
from rss_helper import RSSHelper
from sentiment import Sentiment
import pprint

app = FastAPI()

@app.get("/rss_sentiment")
def rss_sentiment(rss_url,query="",beforeDays = 1,searchIn="title"):
    rsh = RSSHelper()
    links = rsh.get_posts_details(rss_url,beforeDays,searchIn,query)
    sum_compount = 0.0
    s  = Sentiment()
    
    for link in links["posts"]:
        l = s.split_on_sentences(link[searchIn],query)
        sum_compount += float(s.sentiment_scores(l)["compound"])
        #pprint.pprint(s.sentiment_scores(l)["compound"])
        #pprint.pprint("Compound Sentiment is :" + str(sum_compount))
    dict = {"rss_url":rss_url,"q":query,"searchFor":searchFor,"overall_sentiment":round(sum_compount,2)}