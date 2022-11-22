import os

from flask import Flask,request,jsonify
from rss_helper import RSSHelper
from sentiment import Sentiment
import pprint
#import json

app = Flask(__name__)

JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/rss_sentiment", methods = ['GET'])
def rss_sentiment():
    token = request.args.get('t')
    if token is None:
        return jsonify({"err":"Invalid token parameters."})
    token = token.strip('\"')
    token = token.strip("\'")
    if token != JWT_SECRET_KEY:
        return jsonify({"err":"Invalid token parameters."})
    rss_url = request.args.get('rss_url')
    if rss_url is None:
        return jsonify({"err":"Invalid URL parameters."})
    query = request.args.get('q')
    beforeDays = request.args.get('bd')
    if beforeDays is None:
        beforeDays = 1
    beforeDays = beforeDays.strip('\"')
    beforeDays = beforeDays.strip("\'")
    beforeDays = int(beforeDays)
    searchIn = request.args.get('srchIn')
    if rss_url and len(rss_url) > 0:
        rss_url = rss_url.strip('\"')
        rss_url = rss_url.strip("\'")
    if query and len(query) > 0:
        query = query.strip('\"')
        query = query.strip("\'")
    if searchIn is None:
        searchIn = "title" 
    searchIn = searchIn.strip('\"')
    searchIn = searchIn.strip("\'")
    rsh = RSSHelper()
    links = rsh.get_posts_details(rss_url,beforeDays,searchIn,query)
    sum_compount = 0.0
    s  = Sentiment()
    for link in links["posts"]:
        l = s.split_on_sentences(link[searchIn],query)
        sum_compount += float(s.sentiment_scores(l)["compound"])
        #pprint.pprint(s.sentiment_scores(l)["compound"])
        #pprint.pprint("Compound Sentiment is :" + str(sum_compount))
    d = {"rss_url":rss_url,"q":query,"searchFor":query,"overall_sentiment":round(sum_compount,2)}
    return jsonify(d)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))